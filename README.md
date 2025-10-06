# Lokal Medya İndirici

Twitter (X) gibi sosyal medya platformlarından video/GIF indirmek için Python Flask ile geliştirilmiş, kendi ev ağınızda çalışan basit bir web uygulaması.

✨ Özellikler

- **Modern Web Arayüzü:** Karanlık modlu, şık ve mobil uyumlu (responsive) tasarım.
- **Video Önizleme:** İndirme linki bulunan videolar için sayfada anlık önizleme.
- **Kolay İndirme:** Tek tuşla videoyu tarayıcının indirme yöneticisine gönderme.
- **Kısıtlamalı İçerik Desteği:** `cookies.txt` dosyası aracılığıyla yaş kısıtlamalı veya giriş gerektiren videolara erişim.
- **Güvenli (HTTPS):** `mkcert` ile oluşturulan yerel sertifika sayesinde güvenli bağlantı.
- **Platform Bağımsız:** Sunucu Windows/Mac/Linux üzerinde çalışır, arayüze tarayıcısı olan her cihazdan (iPhone, Android, PC vb.) erişilebilir.

## ⚙️ Gereksinimler

- [Python 3.7+](https://www.python.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Flask](https://flask.palletsprojects.com/)
- [mkcert](https://github.com/FiloSottile/mkcert) (HTTPS için)

## 🚀 Kurulum ve Ayarlar

Bu adımları, sunucu olarak kullanacağınız bilgisayarda yapmanız gerekmektedir.

### 1. Projeyi Klonlayın veya İndirin

```bash
git clone [https://github.com/kullanici-adiniz/proje-adiniz.git](https://github.com/kullanici-adiniz/proje-adiniz.git)
cd proje-adiniz
```

### 2. Python Kütüphanelerini Yükleyin

Proje klasöründeyken komut satırını açın ve gerekli kütüphaneleri yükleyin:

```bash
pip install Flask yt-dlp requests
```

### 3. Güvenli Bağlantı (HTTPS) için Sertifika Oluşturun

Bu adım, uygulamanın `httpss://` ile çalışmasını ve tarayıcı özelliklerinin (panoya yapıştırma gibi) aktif olmasını sağlar.

a. **`mkcert` Kurulumu:** Eğer sisteminizde yüklü değilse, [resmi `mkcert` talimatlarını](https://github.com/FiloSottile/mkcert#installation) izleyerek kurun. Windows için en kolay yol [Chocolatey](https://chocolatey.org/install) ile kurmaktır.
   ```powershell
   # PowerShell'i Yönetici olarak açın
   choco install mkcert
   mkcert -install
   ```

b. **Sertifika Oluşturma:** Komut satırında, proje klasörünüzdeyken aşağıdaki komutu çalıştırın. `<IP-ADRESINIZ>` kısmını sunucu olarak kullanacağınız bilgisayarın lokal IP adresiyle (örn: `192.168.1.8`) değiştirin.
   ```bash
   # <IP-ADRESINIZ> kısmını kendi IP'nizle değiştirin!
   mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 <IP-ADRESINIZ>
   ```
   Bu komut, proje klasörünüzde `cert.pem` ve `key.pem` adında iki dosya oluşturacaktır.

### 4. (Opsiyonel) Kısıtlamalı İçerikler için `cookies.txt` Oluşturma

Yaş kısıtlamalı veya sadece giriş yapmış kullanıcılara görünen videoları indirmek için bu adımı uygulayın.

a. **Tarayıcı Eklentisi:** Kullandığınız tarayıcıya (Chrome, Firefox vb.) `Get cookies.txt LOCALLY` gibi bir cookie dışa aktarma eklentisi kurun.

b. **Dosyayı İndirme:**
   - Tarayıcınızda `x.com`'a gidin ve hesabınıza giriş yapın.
   - Eklenti simgesine tıklayıp "Export" veya "Download" seçeneği ile cookie dosyasını indirin.
   - İndirdiğiniz dosyayı projenin ana klasörüne **`cookies.txt`** adıyla kaydedin.

## ▶️ Uygulamayı Çalıştırma

Proje klasöründeyken komut satırında aşağıdaki komutu çalıştırın:

```bash
python app.py
```

Sunucu başladığında `* Running on https://192.168.1.8:5000` gibi bir çıktı göreceksiniz.

## 📱 Kullanım

Sunucu çalışırken, aynı Wi-Fi ağına bağlı herhangi bir cihazdan (telefon, tablet vb.) tarayıcıyı açın ve adres çubuğuna şunu yazın:

`httpss://<IP-ADRESINIZ>:5000`

Örneğin: `httpss://192.168.1.8:5000`

Eğer router'ınızda Local DNS ayarı yaptıysanız, belirlediğiniz ismi de kullanabilirsiniz (örn: `httpss://indirici:5000`).
