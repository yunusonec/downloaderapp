<div align="center">

🚇 Lokal Medya İndirici v1.0
Kendi lokal ağınızda çalışan, Twitter (X) gibi sosyal medya platformlarından video, GIF ve fotoğrafları kolayca indirmenizi sağlayan kişisel web uygulamanız.


</div>

✨ Temel Özellikler
📱 Mobil Uyumlu Tasarım: Karanlık modlu şık arayüz, her cihazda (iPhone, Android, PC) mükemmel görünür ve çalışır.

▶️ Canlı Video Önizleme: Linki getirilen videoları indirmeden önce doğrudan sayfada oynatma imkanı.

🚀 Tek Tuşla İndirme: Önizlemenin altındaki buton ile videoyu doğrudan tarayıcının indirme yöneticisine gönderme.

🔒 Gizli İçerik Desteği: Tarayıcı cookie'leri sayesinde yaş kısıtlamalı, korumalı veya sadece giriş yapmış kullanıcılara açık videolara tam erişim.

🔐 Güvenli (HTTPS): mkcert ile oluşturulan yerel SSL sertifikası sayesinde güvenli bağlantı ve panodan yapıştırma gibi modern tarayıcı özelliklerini kullanma.

🏠 Yerel Ağ Üzerinden Erişim: Evinizdeki Wi-Fi ağına bağlı tüm cihazlarınızdan uygulamaya kolayca erişim.

🛠️ Kullanılan Teknolojiler
Backend: Python, Flask

Video Çekirdeği: yt-dlp

Güvenlik: mkcert (Yerel SSL için)

Frontend: HTML5, CSS3, JavaScript (Fetch API, Clipboard API)

🚀 Kurulum ve Yapılandırma
Bu adımları, sunucu olarak kullanacağınız Windows bilgisayarınızda yapmanız gerekmektedir.

🔧 Adım 1: Ortamı Hazırlama (Sadece İlk Kurulum)
PowerShell'i Yönetici Olarak Açın:
Başlat menüsüne sağ tıklayın → "Terminal (Yönetici)" veya "PowerShell (Yönetici)" seçeneğine tıklayın.

Chocolatey ve mkcert'i Kurun:
Aşağıdaki komutu yapıştırıp çalıştırarak Chocolatey paket yöneticisini kurun.

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('[https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)'))

Yeni bir Yönetici PowerShell penceresi açın ve mkcert'i kurun. Bu, tarayıcıların güvenmesi için gereklidir.

choco install mkcert -y
mkcert -install

📦 Adım 2: Proje Kurulumu ve Yapılandırma
Projeyi Klonlayın ve Kütüphaneleri Yükleyin:
cd komutu ile projenin kurulmasını istediğiniz dizine gidin ve aşağıdaki komutları çalıştırın.

# Projeyi GitHub'dan indirin ve klasörüne girin
git clone [https://github.com/yunusonec/downloaderapp.git](https://github.com/yunusonec/downloaderapp.git)
cd downloaderapp

# Gerekli Python kütüphanelerini yükleyin
pip install -r requirements.txt

Kendi Ağınıza Özel SSL Sertifikası Oluşturun:

Komut İstemi'ne ipconfig yazın → IPv4 Address değerini bulun (örnek: 192.168.1.8).

Aşağıdaki komutta <IP-ADRESINIZ> kısmını kendi IP adresinizle değiştirerek çalıştırın:

# Örnek: mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 192.168.1.8
mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 ::1 <IP-ADRESINIZ>

Bu komut, proje klasörünüzde app.py'nin kullanacağı cert.pem ve key.pem dosyalarını oluşturacaktır.

🍪 Adım 3: (Opsiyonel) Kısıtlı İçerikler için Cookie Ayarı
Tarayıcı Eklentisini Kurun:
Chrome veya Firefox için "Get cookies.txt LOCALLY" eklentisini yükleyin.

Cookie Dosyasını Dışa Aktarın:

x.com (Twitter) hesabınıza giriş yapın.

Eklenti simgesine tıklayıp "Export" seçeneğini seçin.

Dosyayı cookies.txt adıyla proje klasörüne (app.py'nin yanına) kaydedin. app.py bu dosyayı otomatik olarak bulup kullanacaktır.

▶️ Adım 4: Sunucuyu Başlatma
Proje klasöründeyken aşağıdaki komutu çalıştırın:

python app.py

Terminal çıktısı şuna benzer olacaktır:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on [https://127.0.0.1:5000](https://127.0.0.1:5000)
 * Running on https://<IP-ADRESINIZ>:5000
Press CTRL+C to quit

Sunucunun çalışmaya devam etmesi için bu pencereyi kapatmayın.

📱 Uygulamaya Erişim
Sunucu çalışırken, aynı Wi-Fi ağına bağlı herhangi bir cihazdan (telefon, tablet, bilgisayar) tarayıcıyı açıp şu adresi girin:

https://<IP-ADRESINIZ>:5000

Örnek: https://192.168.1.8:5000

💡 İpucu:
Eğer router ayarlarınızda bir Local DNS kaydı oluşturduysanız (örnek: indirici -> 192.168.1.8), https://indirici:5000 şeklinde de erişebilirsiniz. Bu durumda sertifikanızı oluştururken o DNS ismini de mkcert komutuna eklemeniz gerekir.

⚠️ Sorun Giderme
Hata

Açıklama

ERROR: No video could be found...

Video Twitter’a ait değil, özel bir hesaba ait veya telif hakkı kısıtlaması var.

ERROR: Could not copy Chrome cookie...

Sunucuyu başlatmadan önce tüm tarayıcı pencerelerini kapatın veya cookies.txt yöntemini kullanın.

'mkcert' is not recognized...

mkcert kurulmamış veya komutu çalıştırmak için yeni bir terminal penceresi açılmamış olabilir.

📄 Lisans
Bu proje, MIT Lisansı altında lisanslanmıştır.
Detaylı bilgi için LICENSE dosyasına göz atabilirsiniz.

<div align="center">

Geliştirici: Yunus Emre Öneç

</div>
