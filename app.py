import subprocess
import json
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# --- YENİ EKLENEN KISIM ---
# Hangi tarayıcıyı kullanacağımızı buradan seçiyoruz.
# Seçenekler: 'chrome', 'firefox', 'edge', 'opera', 'vivaldi'
# Lütfen bilgisayarınızda Twitter'a giriş yaptığınız tarayıcının adını yazın.
BROWSER_TO_USE = 'chrome' 
# --- BİTİŞ ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL bulunamadı'}), 400

    try:
        if not re.match(r'^(https?://)?(www\.)?(twitter\.com|x\.com)/[^/]+/status/\d+', url):
             return jsonify({'error': 'Geçerli bir Twitter (X) URL\'si değil.'}), 400
        
        # --- DEĞİŞEN KOMUT KISMI ---
        # yt-dlp komutuna --cookies-from-browser parametresini ekliyoruz.
        # Bu, yt-dlp'nin belirttiğimiz tarayıcıdaki Twitter giriş cookie'lerini
        # kullanarak istek yapmasını sağlar.
        command = [
            'yt-dlp',
            '-J', # --dump-json
            '--cookies', 'cookies.txt',
            '--no-warnings',
            '--quiet',
            url
        ]
        # --- BİTİŞ ---

        result = subprocess.run(
            command, # Yukarıda oluşturduğumuz komutu kullanıyoruz
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        
        tweet_details = json.loads(result.stdout)
        
        media_url = tweet_details.get('url')
        
        if media_url:
            return jsonify({'media_url': media_url})
        else:
            formats = tweet_details.get('formats', [])
            best_format = max(
                (f for f in formats if f.get('vcodec') != 'none'),
                key=lambda f: f.get('height', 0),
                default=None
            )
            if best_format and best_format.get('url'):
                 return jsonify({'media_url': best_format['url']})
            else:
                 if tweet_details.get('entries'):
                      first_entry = tweet_details['entries'][0]
                      if first_entry.get('url'):
                           return jsonify({'media_url': first_entry['url']})
            return jsonify({'error': 'Bu tweet\'te indirilebilir bir medya bulunamadı.'}), 404

    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip()
        print(f"yt-dlp hatası: {error_message}")
        return jsonify({'error': f'yt-dlp hatası: {error_message}'}), 500
    except Exception as e:
        print(f"Genel hata: {e}")
        return jsonify({'error': 'Beklenmedik bir hata oluştu.'}), 500

if __name__ == '__main__':
    # SSL sertifika dosyaları için standart isimler kullanıyoruz.
    # Kullanıcılar kendi sertifikalarını bu isimlerle oluşturmalı.
    try:
        ssl_context = ('cert.pem', 'key.pem')
        app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=ssl_context)
    except FileNotFoundError:
        print("="*50)
        print("HATA: SSL sertifika dosyaları (cert.pem, key.pem) bulunamadı!")
        print("Lütfen README.md dosyasındaki kurulum adımlarını takip edin.")
        print("="*50)