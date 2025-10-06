<div align="center">

🚇 Lokal Medya İndirici
Kendi lokal ağınızda çalışan, Twitter (X) ve benzeri sosyal medya platformlarından video, GIF ve fotoğrafları kolayca indirmenizi sağlayan kişisel web uygulamanız.

</div>



<p align="center">
<em>Uygulamanın karanlık modlu modern arayüzü.</em>
</p>
<p align="center">
<!-- 💡 İPUCU: Uygulamanın ekran görüntüsünü alıp (örn: https://imgur.com/upload) yükledikten sonra bu linki güncelleyebilirsiniz. -->
<img src="https://www.google.com/search?q=https://i.imgur.com/your-screenshot-url.png" alt="Uygulama Ekran Görüntüsü" width="80%">
</p>

✨ Temel Özellikler
Modern ve Kullanışlı Arayüz: Şık bir karanlık moda sahip, mobil cihazlarla tam uyumlu (responsive) tasarım.

Canlı Video Önizleme: Linki getirilen videoları indirmeden önce doğrudan sayfada oynatma.

Tek Tuşla İndirme: Önizlemenin altındaki buton ile videoyu doğrudan tarayıcının indirme yöneticisine gönderme.

Gizli İçerik Desteği: Tarayıcı cookie'leri sayesinde yaş kısıtlamalı, korumalı veya sadece giriş yapmış kullanıcılara açık videolara tam erişim.

Güvenli (HTTPS): mkcert ile oluşturulan yerel SSL sertifikası sayesinde güvenli bağlantı ve modern tarayıcı özelliklerini (örneğin panoya erişim) kullanma imkanı.

Ev Ağı Üzerinden Erişim: Sunucu olarak kurduğunuz bilgisayar çalışırken, aynı Wi-Fi ağına bağlı tüm cihazlarınızdan (iPhone, Android, tablet, laptop vb.) uygulamaya erişebilirsiniz.

🛠️ Kullanılan Teknolojiler
Backend: Python, Flask

Video Çekirdeği: yt-dlp

Güvenlik: mkcert (Yerel SSL için)

Frontend: HTML5, CSS3, JavaScript

🚀 Kurulum ve Yapılandırma
Bu adımları, sunucu olarak kullanacağınız Windows bilgisayarınızda yapmanız gerekmektedir.

Adım 1: Ortamı Hazırlama (Sadece İlk Kurulum)
Öncelikle gerekli araçları sisteminize kuralım. Bu adımları sadece bir kereliğine yapmanız yeterlidir.

PowerShell'i Yönetici Olarak Açın: Başlat menüsüne sağ tıklayın ve "Terminal (Yönetici)" veya "PowerShell (Yönetici)" seçeneğine tıklayın.

Aşağıdaki komutları sırasıyla çalıştırarak Chocolatey (paket yöneticisi) ve onun aracılığıyla mkcert'i kurun:

# Chocolatey Kurulumu
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('[https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)'))

# mkcert Kurulumu (Yeni bir Yönetici PowerShell penceresi açıp bu komutu çalıştırın)
choco install mkcert -y

mkcert'i Sisteme Tanıtın: Bilgisayarınızın mkcert tarafından oluşturulan sertifikalara güvenmesi için aşağıdaki komutu çalıştırın:

mkcert -install

Adım 2: Projeyi Kurma ve Yapılandırma
Projeyi Klonlayın ve Gerekli Kütüphaneleri Yükleyin: Normal bir Komut İstemi (cmd) penceresi açın ve aşağıdaki komutları çalıştırın:

# Projeyi GitHub'dan indirin ve klasörüne girin
git clone [https://github.com/yunusonec/downloaderapp.git](https://github.com/yunusonec/downloaderapp.git)
cd downloaderapp

# Gerekli Python kütüphanelerini yükleyin
pip install Flask yt-dlp requests

Kendi Ağınıza Özel SSL Sertifikası Oluşturun:

Lokal IP adresinizi öğrenmek için ipconfig yazın ve IPv4 Address satırını bulun (örn: 192.168.1.8).

Aşağıdaki komutta <IP-ADRESINIZ> yazan yeri kendi IP adresinizle değiştirerek çalıştırın.

# Örnek: mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 192.168.1.8
mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 <IP-ADRESINIZ>

Bu komut, proje klasörünüzde cert.pem ve key.pem adında iki dosya oluşturacaktır.

Adım 3: (Önerilir) Kısıtlı İçerikler için Cookie Ayarı
Yaş kısıtlamalı veya korumalı hesaplara ait videoları indirebilmek için bu adımı uygulayın.

Tarayıcı Eklentisi: Kullandığınız tarayıcıya (Chrome, Firefox vb.) Get cookies.txt LOCALLY gibi bir cookie dışa aktarma eklentisi kurun.

Dosyayı İndirme:

Tarayıcınızda x.com'a gidin ve hesabınıza giriş yapın.

Eklenti simgesine tıklayıp "Export" seçeneği ile cookie dosyasını indirin.

İndirdiğiniz dosyayı projenin ana klasörüne cookies.txt adıyla kaydedin.

▶️ Sunucuyu Başlatma
Kurulum tamamlandıktan sonra, sunucuyu başlatmak için proje klasöründeyken Komut İstemi'ne şunu yazın:

python app.py
