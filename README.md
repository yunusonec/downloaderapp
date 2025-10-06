# Lokal Medya İndirici

Twitter (X) gibi sosyal medya platformlarından video/GIF indirmek için Python Flask ile geliştirilmiş, kendi ev ağınızda çalışan basit bir web uygulaması.

![Uygulama Ekran Görüntüsü](https://i.imgur.com/your-screenshot-url.png)

## ✨ Özellikler

- **Modern Web Arayüzü:** Karanlık modlu, şık ve mobil uyumlu (responsive) tasarım.
- **Video Önizleme:** İndirme linki bulunan videolar için sayfada anlık önizleme.
- **Kolay İndirme:** Tek tuşla videoyu tarayıcının indirme yöneticisine gönderme.
- **Kısıtlamalı İçerik Desteği:** `cookies.txt` dosyası aracılığıyla yaş kısıtlamalı veya giriş gerektiren videolara erişim.
- **Güvenli (HTTPS):** `mkcert` ile oluşturulan yerel sertifika sayesinde güvenli bağlantı.
- **Platform Bağımsız:** Sunucu Windows/Mac/Linux üzerinde çalışır, arayüze tarayıcısı olan her cihazdan (iPhone, Android, PC vb.) erişilebilir.

## 🚀 Kurulum ve Çalıştırma

Bu adımları, sunucu olarak kullanacağınız bilgisayarda yapmanız gerekmektedir.

### Adım 1: Projeyi İndirin ve Gerekli Araçları Yükleyin

Önce projeyi klonlayın, ardından gerekli tüm Python kütüphanelerini ve `mkcert` aracını yükleyin.

```bash
# Projeyi klonlayın ve klasörüne girin
git clone [https://github.com/yunusonec/downloaderapp.git](https://github.com/yunusonec/downloaderapp.git)
cd downloaderapp

# Gerekli Python kütüphanelerini yükleyin
pip install Flask yt-dlp requests

# (Windows için) PowerShell'i Yönetici olarak açıp aşağıdaki komutlarla mkcert'i kurun
# Chocolatey paket yöneticisini kur
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('[https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)'))
# mkcert'i kur
choco install mkcert -y
Adım 2: Sertifika Ortamını Ayarlayın
mkcert'in oluşturacağı sertifikalara bilgisayarınızın güvenmesi için bu komutu sadece bir kereliğine çalıştırmanız gerekir.

PowerShell

# PowerShell'i Yönetici olarak açıp çalıştırın
mkcert -install
Adım 3: Projeyi Kendi Ağınıza Göre Yapılandırın
Şimdi, kendi lokal IP adresinize özel bir SSL sertifikası oluşturacağız.

a. Lokal IP Adresinizi Öğrenin: Komut İstemi'ne ipconfig yazın ve IPv4 Address satırındaki adresinizi (örn: 192.168.1.8) not alın.

b. Sertifikayı Oluşturun: Komut satırında, proje klasörünüzdeyken aşağıdaki komutu çalıştırın. <IP-ADRESINIZ> kısmını az önce bulduğunuz kendi IP adresinizle değiştirmeyi unutmayın.

Bash

# Örnek: mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 192.168.1.8
mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 <IP-ADRESINIZ>
Bu komut, proje klasörünüzde cert.pem ve key.pem adında iki dosya oluşturacaktır.

Adım 4: (Opsiyonel) Kısıtlı İçerikler için Cookie Ayarı
Yaş kısıtlamalı veya sadece giriş yapmış kullanıcılara görünen videoları indirmek istiyorsanız bu adımı uygulayın.

a. Tarayıcı Eklentisi: Kullandığınız tarayıcıya (Chrome, Firefox vb.) Get cookies.txt LOCALLY gibi bir cookie dışa aktarma eklentisi kurun.

b. Dosyayı İndirme:

Tarayıcınızda x.com'a gidin ve hesabınıza giriş yapın.

Eklenti simgesine tıklayıp "Export" veya "Download" seçeneği ile cookie dosyasını indirin.

İndirdiğiniz dosyayı projenin ana klasörüne cookies.txt adıyla kaydedin.

Adım 5: Sunucuyu Başlatın
Artık her şey hazır. Proje klasöründeyken komut satırında aşağıdaki komutu çalıştırarak uygulamayı başlatın:

Bash

python app.py
Sunucu başladığında * Running on https://<IP-ADRESINIZ>:5000 gibi bir çıktı göreceksiniz.

📱 Kullanım
Sunucu çalışırken, aynı Wi-Fi ağına bağlı herhangi bir cihazdan (telefon, tablet vb.) tarayıcıyı açın ve adres çubuğuna şunu yazın:

httpss://<IP-ADRESINIZ>:5000

Örneğin: httpss://192.168.1.8:5000

Eğer router'ınızda Local DNS ayarı yaptıysanız, belirlediğiniz ismi de kullanabilirsiniz (örn: httpss://indirici:5000).
