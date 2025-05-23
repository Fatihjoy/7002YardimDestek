import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

yardim_butonlari = [
    ("📊 CP Seviyeleri", "cp"), ("🏰 Klan Oluşturma", "klan"), ("🎵 Müzik İndirme", "muzik"),
    ("📦 Şanslı Paket", "sansli"), ("👤 Cinsiyet Değişikliği", "cinsiyet"), ("📱 Doğrulama Kodu", "dogrulama"),
    ("📧 E-Posta Doğrulama", "eposta"), ("🖼️ Afiş Boyutu", "afis"), ("👥 Profil Boyutu", "profil"),
    ("🗑️ Hesap Silme", "hesap"), ("🎬 GIF Nasıl Yapılır?", "gifvideo"), ("📌 Çok Önemli", "cokonemli"),
    ("📋 Yardım Kuralları", "yardimkurallari"), ("⏱️ Atılma Süreleri", "atilmasure"),
    ("🌍 Panel Ülkeler", "ulkeler"), ("🍇 Meyve Sorunu", "meyveneden"), ("🍇 Meyve Ödülleri", "meyveodul"),
    ("🎓 Hesap Bağlama", "hesapbagla"), ("📢 Klan Şikayetleri", "klansikayet"), ("⭐ Aristokrasi", "aristokrasi"),
    ("📸 Özelden İfşa", "ifsa"), ("🌐 Yurtdışı Uygulama", "yurtdisi"), ("🎧 Android Müzik", "androidmuzik"),
    ("👑 Süper Adminler", "superadmin")
]

hazir_butonlari = [
    ("🕓 Afk", "afk"), ("📱 Uygulama Reklamı", "reklam"), ("📞 Görüntülü Sohbet", "goruntulu"),
    ("📸 İfşa Bildirimi", "ifsa_bildirim"), ("👥 Klon Kullanıcı", "klon"), ("🗣️ Argo ve Küfür", "kufur"),
    ("🛡️ Klan Başvurusu", "klanbasvuru"), ("📷 Uygunsuz Arka Plan", "arka"), ("🚫 Şiddet Profil", "siddet"),
    ("🗳️ Siyasi Profil", "siyasi"), ("👑 Kötüye Aristokrasi", "kotu_aristo"), ("💢 Panel Argo", "panelargo"),
    ("📍 Panel Türkiye", "paneltr"), ("🔇 Yayın Sabotaj", "sabotaj"), ("📄 Uygunsuz Biyografi", "biyografi"),
    ("🖼️ Uygunsuz Profil Resmi", "profilresmi"), ("🆔 Uygunsuz Nick", "nick"), ("🙋 Yusuf Bey Bilgi", "yusuf"),
    ("🗯️ Panel Argo Kullanımı", "panelargo2"), ("💢 Oda Kaosu", "kaos"), ("🚫 Pornografik Görsel", "porno"),
    ("🚫 Aristo Satışı", "aristosatis"), ("🔞 Oyun Argo", "oyunargo"), ("🌑 Karartılmış Profil", "karartma"),
    ("👤 Kişisel Bilgi İfşası", "kisiselifsa"), ("📱 Oyun Reklamı", "oyunreklam"),
    ("🎵 Siyasi Şarkı", "sarkiprop")
]

def gonder_buton_gruplu(chat_id, butonlar, baslik_emoji, grup_baslik):
    gruplar = [butonlar[i:i+20] for i in range(0, len(butonlar), 20)]
    for index, grup in enumerate(gruplar):
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(*[InlineKeyboardButton(text, callback_data=callback) for text, callback in grup])
        bot.send_message(chat_id, f"{baslik_emoji} {grup_baslik} {index + 1}/{len(gruplar)}:", reply_markup=markup)
@bot.message_handler(commands=["yardim"])
def yardim(message):
    gonder_buton_gruplu(message.chat.id, yardim_butonlari, "📘", "Yardım")

@bot.message_handler(commands=["hazir", "hazır", "hazirbildirimler", "hazırbildirimler"])
def hazir(message):
    gonder_buton_gruplu(message.chat.id, hazir_butonlari, "📝", "Hazır Bildirim")

@bot.callback_query_handler(func=lambda call: True)
def cevapla(call):
    cevaplar = {
        # BURAYA TÜM CEVAPLAR EKLENECEK
    }

    if call.data == "gifvideo":
        with open("gif_nasil_yapilir.mp4", "rb") as video:
            bot.send_video(call.message.chat.id, video)
    else:
        bot.send_message(call.message.chat.id, cevaplar.get(call.data, "Bu konuda bilgi bulunamadı."))
    bot.answer_callback_query(call.id)

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    cevaplar = {
        "cp": """📊 CP Seviyeleri ve Gereken Hediyeler:

0 - 1 → 1.000.000

1 - 2 → 5.000.000

2 - 3 → 10.000.000

3 - 4 → 20.000.000

4 - 5 → 50.000.000

5 - 6 → 100.000.000

Toplam: 186.000.000""",

        "klan": """🏰 Klan Oluşturma:

Mevcut klanını dağıttıktan sonra, yeni bir klan oluşturmak için bir sonraki ayın başına kadar beklemeniz gerekmektedir.""",

        "muzik": "🎵 Müzik İndirme:\n\nhttps://mp3indirdur.life/",

        "sansli": """📦 Şanslı Paket:

Cihaz olağandışı kullanıldığı için sistem tarafından riskli cihaz olarak tanımlanmıştır.

Kullanıcı cihazını olağandışı koşullarda kullanmaktan kaçınmalıdır.

Sistem cihazın 24 saat içinde normal kullanımda olduğunu tespit ederse, paket tekrar alınabilir hâle gelecektir.""",

        "cinsiyet": """👤 Cinsiyet Değişikliği:

Kullanıcılar, kayıt tarihinden itibaren 30 gün içerisinde cinsiyet bilgilerini kendileri değiştirebilirler.

Bu sürenin aşılması durumunda yapılan talepler işleme alınmayacaktır.""",

        "dogrulama": """📱 Doğrulama Kodu:

24 saat içinde en fazla 3 kez doğrulama kodu alınabilir.

Kod alamama durumu bulunduğunuz bölgedeki yerel operatör ve ağ sinyaliyle ilgili olabilir.

Alternatif olarak e-posta adresinizi bağlayarak kodları e-posta yoluyla alabilirsiniz.""",

        "eposta": """📧 E-Posta Doğrulama:

Her saat en fazla 5 kez doğrulama kodu alınabilir.

1 saat sonra tekrar alınabilir.""",

        "afis": "🖼️ Etkinlik Afişi Boyutu:\n\n636x362",

        "profil": "👥 Oda ve Kişi Profil Fotoğrafı:\n\n800x800",

        "hesap": """🗑️ Hesap Silme:

Profilim → Ayarlar → Hesap → Hesabı Sil yolunu izleyin.

Başvuru yapıldığında sistem 30 gün sonra hesabı otomatik olarak silecektir.

Bu süre zarfında hesaba giriş yapılmazsa hesap silinir. Giriş yapılırsa işlem iptal olur.""",

        "cokonemli": """📌 Çok Önemli:

1 - Cinsiyet değişimi yapılmamaktadır.

2 - Klan bilgisi verilmez, sadece RCS admin yönlendirmesi yapılır.

3 - Çekim bilgisi verilmez, kullanıcılar 7010 ID 66 şifreli odaya yönlendirilir.""",

        "yardimkurallari": """📋 Yardım Odası Kuralları:

1 - Mikrofon paylaşılamaz.

2 - Mikrofonda aynı anda 2 kişi bulunamaz.

3 - Yayın devri admin izniyle yapılmalıdır.

4 - Kullanıcılara nick dışında hitap edilmemelidir.

5 - Yayın saatine dikkat edilmeli, 10 dakika geçince yayın verilmez.

6 - Kullanıcılara karşı ses yükseltilmemelidir.

7 - Yardımcı olan 2 admin varsa biri sessiz kalmalıdır.

8 - JoyMi amblemli görsel zorunludur.""",

        "atilmasure": """⏱️ Destek Odasından Atılma Süreleri:

AFK Bildirimi: 10 Dakika

Yayını Sabote: 10 Dakika

Küfür/Kayıt alınamama: 10 Dakika

Yazma yasağı uygulanmaz, uzun süreli atmalar yalnızca Elif Hanım bilgisiyle yapılır.""",

        "ulkeler": """🌍 Panel Yönlendirme Ülkeler:

Azerbaycan

Türkmenistan

Özbekistan

Tacikistan

→ 7007 ID'li odaya yönlendirilir.""",

        "meyveneden": """🍇 Meyve Oyunu Sorunu:

Yeni kullanıcıların meyve oyunu açabilmesi için Onur ve Cazibe seviyeleri eşit şekilde 3. seviyeye ulaşmalıdır.""",

        "meyveodul": """🍇 Meyve Oyunu Ödülleri:

1. sırada yer alan kullanıcı aristokrasi alamazsa doğrudan Yusuf Bey'e veya Kumru Hanım'a yönlendirilmelidir.""",

        "hesapbagla": """🎓 Hesap Bağlama / Kaldırma:

Ayarlar > Hesap > Bağlantılar → Telefon, E-Posta, Google veya Apple ile bağlanılabilir.

Google/Apple kaldırılabilir. Telefon ve e-posta sadece değiştirilebilir.""",

        "klansikayet": """📢 Klan Şikayetleri:

Klanlar hakkında bilgi verilmez.

Sadece başvuru ve RCS admin yönlendirmesi yapılır.""",

        "aristokrasi": """⭐ Aristokrasi Hediye Etme:

Bilgi verilmez. VIP yardım destek odasına yönlendirme yapılır.

Oda ID: 7010 — Şifre: 66""",

        "ifsa": """📸 Özelden İfşa:

Tarihli bir kağıt + yüz görünen anlık selfie çekilmeli.

Teyit resmi panel adminine gönderilmeli.

İfşası yapılan profil SS’i ve ifşa yapılan yer SS’i panelde bildirilmelidir.""",

        "yurtdisi": """🌐 Yurtdışı Uygulama İndirme:

iPhone: https://youtu.be/uQxuilRNtuc

Android: https://youtu.be/uQxuilRNtuc""",

        "androidmuzik": "🎧 Android Müzik İndirme:\n\nhttps://www.snaptube.com/tr/",

        "superadmin": """👑 Süper Adminlerimiz:

Elif Hanım — Genel Şikayetler

Yusuf Bey — Çekim, VIP

Kumru Hanım — VIP

Kadir Bey — Klanlar

Furkan Bey — Reklam / Promosyon

Adelph Bey — Türkî Devletler"""
    }
        ,
        "afk": """ID :

Afk kaldığı için 10 dakika uzaklaştırıldı

@elifdn61""",

        "reklam": """ID :

Farklı uygulama reklamı

@""",

        "goruntulu": """ID :

Görüntülü Sohbet Talep Ediyor

@elifdn61""",

        "ifsa_bildirim": """İfşa Yapan Hesap :

İfşası Yapılan Hesap :

Teyit Resmi özelinize gönderildi

@""",

        "klon": """Klonlanan Kullanıcı ID :

Klonlama Yapan Kullanıcı ID :

@""",

        "kufur": """ID :

Mikrofonda argo ve küfür

@""",

        "klanbasvuru": """Klan Başvurusu

Oda ID :

Kullanıcı ID :

@""",

        "arka": """ID :

Uygunsuz arka plan resmi

@""",

        "siddet": """ID :

Şiddet içerikli profil resmi

@""",

        "siyasi": """ID :

Siyasi profil resmi

@""",

        "kotu_aristo": """Oda ID :

Aristokrasisini kötüye kullanan kullanıcı mevcut

@""",

        "panelargo": """ID :

Panel üzerinde argo ve küfür

@""",

        "paneltr": """ID :

Panel Türkiye olarak güncellenecek

@elifdn61""",

        "sabotaj": """ID :

Yayını sabote ettiği için 10 dakika uzaklaştırıldı

@elifdn61""",

        "biyografi": """ID :

Uygunsuz biyografi

@""",

        "profilresmi": """ID :

Uygunsuz profil resmi

@""",

        "nick": """ID :

Uygunsuz nick name

@""",

        "yusuf": """ID :

Yusuf Bey kullanıcı bilgi almak istiyor ama VIP odasındaki asistanlar yardımcı olmuyor

@Yusufcan31""",

        "panelargo2": """ID :

Panelde Argo Kullanımı

@""",

        "kaos": """ID :

Oda içinde diğer kullanıcılar da küfür etmekte. Ancak bu kullanıcı, adminleri kışkırtıyor.

@""",

        "porno": """ID :

Panel üzerinde pornografik görsel paylaşımı

@""",

        "aristosatis": """ID :

Kural dışı aristokrasi satışı

@""",

        "oyunargo": """ID :

Oyun aktifken argo ve küfür kullanımı mevcut

@""",

        "karartma": """ID :

Karartılmış profil resmi

@""",

        "kisiselifsa": """İfşa Yapan Hesap :

İfşası Yapılan Hesap :

Kişisel bilgi paylaşımı

@""",

        "oyunreklam": """ID :

Farklı uygulama oyunları gösterimi

@""",

        "sarkiprop": """ID :

Propaganda yapmak amaçlı Mikrofonda siyasi şarkı çalmak

@"""
