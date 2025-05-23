import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# /yardim komutu – kullanıcı destek menüsü
@bot.message_handler(commands=['yardim'])
def yardim_mesaji(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("📊 CP Seviyeleri", callback_data="cp"),
        InlineKeyboardButton("🏰 Klan Oluşturma", callback_data="klan"),
        InlineKeyboardButton("🎵 Müzik İndirme", callback_data="muzik"),
        InlineKeyboardButton("📦 Şanslı Paket", callback_data="sansli"),
        InlineKeyboardButton("👤 Cinsiyet Değişikliği", callback_data="cinsiyet"),
        InlineKeyboardButton("📱 Doğrulama Kodu", callback_data="dogrulama"),
        InlineKeyboardButton("📧 E-Posta Doğrulama", callback_data="eposta"),
        InlineKeyboardButton("🖼️ Afiş Boyutu", callback_data="afis"),
        InlineKeyboardButton("👥 Profil Boyutu", callback_data="profil"),
        InlineKeyboardButton("🗑️ Hesap Silme", callback_data="hesap"),
        InlineKeyboardButton("🎬 GIF Nasıl Yapılır?", callback_data="gifvideo"),
        InlineKeyboardButton("📌 Çok Önemli", callback_data="cokonemli"),
        InlineKeyboardButton("📋 Yardım Odası Kuralları", callback_data="yardimkurallari"),
        InlineKeyboardButton("⏱️ Destek Atılma Süreleri", callback_data="atilmasure"),
        InlineKeyboardButton("🌍 Panel Yönlendirme Ülkeler", callback_data="ulkeler"),
        InlineKeyboardButton("🍇 Meyve Oyunu Sorunu", callback_data="meyveneden"),
        InlineKeyboardButton("🍇 Meyve Oyunu Ödülleri", callback_data="meyveodul"),
        InlineKeyboardButton("🎓 Hesap Bağlama", callback_data="hesapbagla"),
        InlineKeyboardButton("📢 Klan Şikayetleri", callback_data="klansikayet"),
        InlineKeyboardButton("⭐ Aristokrasi Hediyesi", callback_data="aristokrasi"),
        InlineKeyboardButton("📸 Özelden İfşa", callback_data="ifsa"),
        InlineKeyboardButton("🌐 Yurtdışı Uygulama", callback_data="yurtdisi"),
        InlineKeyboardButton("🎧 Android Müzik İndirme", callback_data="androidmuzik"),
        InlineKeyboardButton("👑 Süper Adminlerimiz", callback_data="superadmin")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Yardım menüsünden bir konu seçin:", reply_markup=markup)

# /hazir komutu – admin bildirim şablonları
@bot.message_handler(commands=['hazir', 'hazır', 'hazirbildirimler', 'hazırbildirimler'])
def hazir_mesaji(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("🕓 Afk", callback_data="afk"),
        InlineKeyboardButton("📱 Farklı Uygulama Reklamı", callback_data="reklam"),
        InlineKeyboardButton("📞 Görüntülü Sohbet", callback_data="goruntulu"),
        InlineKeyboardButton("📸 İfşa Bildirimi", callback_data="ifsa_bildirim"),
        InlineKeyboardButton("👥 Klon Kullanıcı", callback_data="klon"),
        InlineKeyboardButton("🗣️ Argo ve Küfür", callback_data="kufur"),
        InlineKeyboardButton("🛡️ Klan Başvurusu", callback_data="klanbasvuru"),
        InlineKeyboardButton("📷 Uygunsuz Arka Plan", callback_data="arka"),
        InlineKeyboardButton("🚫 Şiddet Profil", callback_data="siddet"),
        InlineKeyboardButton("🗳️ Siyasi Profil", callback_data="siyasi"),
        InlineKeyboardButton("👑 Kötüye Kullanılan Aristokrasi", callback_data="kotu_aristo"),
        InlineKeyboardButton("💢 Panel Argo", callback_data="panelargo"),
        InlineKeyboardButton("📍 Panel Türkiye", callback_data="paneltr"),
        InlineKeyboardButton("🔇 Yayın Sabotaj", callback_data="sabotaj"),
        InlineKeyboardButton("📄 Uygunsuz Biyografi", callback_data="biyografi"),
        InlineKeyboardButton("🖼️ Uygunsuz Profil Resmi", callback_data="profilresmi"),
        InlineKeyboardButton("🆔 Uygunsuz Nick", callback_data="nick"),
        InlineKeyboardButton("🙋 Yusuf Bey Bilgi", callback_data="yusuf"),
        InlineKeyboardButton("🗯️ Panel Argo Kullanımı", callback_data="panelargo2"),
        InlineKeyboardButton("💢 Oda Kaosu", callback_data="kaos"),
        InlineKeyboardButton("🚫 Pornografik Görsel", callback_data="porno"),
        InlineKeyboardButton("🚫 Aristo Satışı", callback_data="aristosatis"),
        InlineKeyboardButton("🔞 Oyun Argo", callback_data="oyunargo"),
        InlineKeyboardButton("🌑 Karartılmış Profil", callback_data="karartma"),
        InlineKeyboardButton("👤 Kişisel Bilgi İfşası", callback_data="kisiselifsa"),
        InlineKeyboardButton("📱 Oyun Reklamı", callback_data="oyunreklam"),
        InlineKeyboardButton("🎵 Siyasi Şarkı", callback_data="sarkiprop"),
        InlineKeyboardButton("⚠️ Tekrar Aristo Satışı", callback_data="aristo2")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📝 Hazır bildirim şablonlarından birini seçin:", reply_markup=markup)

# Callback'ler
@bot.callback_query_handler(func=lambda call: True)
def cevapla(call):
    cevaplar = {
        # yardım cevapları (uzun halleri)
        "cp": "📊 CP Seviyeleri ve Gereken Hediyeler:\n\n0 - 1 → 1.000.000\n1 - 2 → 5.000.000\n2 - 3 → 10.000.000\n3 - 4 → 20.000.000\n4 - 5 → 50.000.000\n5 - 6 → 100.000.000\n\nToplam: 186.000.000",
        "klan": "🏰 Mevcut klanı dağıttıktan sonra, yeni bir klan için bir sonraki ayın başına kadar beklemeniz gerekir.",
        "muzik": "🎵 Müzik İndirme:\nhttps://mp3indirdur.life/",
        "sansli": "📦 Şanslı Paket:\nCihaz olağandışı kullanıldığı için sistem tarafından riskli cihaz olarak tanımlanmış olabilir. Normal kullanım sonrası 24 saat içinde tekrar kullanılabilir.",
        "cinsiyet": "👤 Cinsiyet Değişikliği:\nKayıttan itibaren 30 gün içinde değiştirilebilir. Bu süreden sonra yapılan talepler işleme alınmaz.",
        "dogrulama": "📱 Doğrulama Kodu:\n24 saat içinde en fazla 3 kez alınabilir. Aksi durumda 24 saat beklenmelidir.",
        "eposta": "📧 E-Posta Doğrulama:\nHer saat en fazla 5 kez alınabilir. 1 saat sonra tekrar denenebilir.",
        "afis": "🖼️ Etkinlik Afişi Boyutu:\n636x362 piksel",
        "profil": "👥 Oda ve Kişi Profil Fotoğrafı:\n800x800 piksel",
        "hesap": "🗑️ Hesap Silme:\nProfil > Ayarlar > Hesap > Hesabı Sil\nSilme başvurusundan sonra 30 gün giriş yapılmazsa hesap silinir. Giriş yapılırsa iptal olur.",
        "cokonemli": "📌 1 - Cinsiyet değişimi 1 Aralık itibarıyla artık kesinlikle yapılmamaktadır.\n2 - Klan ile alakalı bilgi verilmez. Sadece RCS admin talebi alınır.\n3 - Çekim ve Svip hakkında bilgi verilmez. Sadece 7010 ID 66 Şifreli odaya yönlendirilir.",
        "yardimkurallari": "📋 Yardım Odası Kuralları:\n1 - Mikrofon paylaşımı yapılmaz.\n2 - Yayın teslimi admin izniyle olur.\n3 - Nick dışında hitap edilmez.\n4 - Kaosa karışılmaz.\n5 - 10 dakikayı geçen yayın alınmaz.",
        "atilmasure": "⏱️ Destek Odası Atılma Süreleri:\nAfk: 10 dk\nYayını Sabote Eden: 10 dk\nKüfür Eden: 10 dk",
        "ulkeler": "🌍 Panel Yönlendirme Ülkeler:\nAzerbaycan, Türkmenistan, Özbekistan, Tacikistan → 7007 ID'li odaya yönlendirilir.",
        "meyveneden": "🍇 Meyve Oyunu Sorunu:\nYeni kullanıcılarda meyve oyunlarının açılması için Onur ve Cazibe seviyeleri 3. seviye olmalıdır.",
        "meyveodul": "🍇 Meyve Oyunu Ödülleri:\n1. olup aristokrasisini alamayan kullanıcılar Yusuf Bey'e veya Kumru Hanım'a yönlendirilmelidir.",
        "hesapbagla": "🎓 Hesap Bağlama ve Kaldırma:\nAyarlar > Hesap > Telefon/E-posta/Google/Apple seçin > Bağla veya Bağlantıyı Kaldır.",
        "klansikayet": "📢 Klan Şikayetleri:\nKlan hakkında bilgi verilmez. Sadece başvuru ve RCS talebi alınır.",
        "aristokrasi": "⭐ Aristokrasi Hediye:\nDetaylı bilgi için kullanıcılar VIP yardım destek odası (7010 ID, 66 Şifre) yönlendirilir.",
        "ifsa": "📸 Özelden İfşa:\nTarihi kağıda yazıp anlık selfie çekilecek. Ardından profil SS'leri ile birlikte panel adminine bildirim sağlanacak.",
        "yurtdisi": "🌐 Yurtdışı Uygulama:\niPhone: https://youtu.be/uQxuilRNtuc\nAndroid: https://youtu.be/uQxuilRNtuc",
        "androidmuzik": "🎧 Android Müzik:\nhttps://www.snaptube.com/tr/",
        "superadmin": "👑 Süper Adminlerimiz:\nElif Hanım, Yusufcan Bey, Kumru Hanım, Kadir Bey, Furkan Bey, Adelph Bey",

        # özel video butonu
        "gifvideo": None,

        # hazır bildirim örnekleri
        "afk": "ID :\nAfk kaldığı için 10 dakika uzaklaştırıldı\n@elifdn61",
        # diğerleri için de uzun cevaplar eklenebilir
    }

    if call.data == "gifvideo":
        with open("gif_nasil_yapilir.mp4", "rb") as video:
            bot.send_video(call.message.chat.id, video)
    else:
        yanit = cevaplar.get(call.data, "Bu konuda bilgi bulunamadı.")
        bot.send_message(call.message.chat.id, yanit)

    bot.answer_callback_query(call.id)

# webhook endpoint
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'OK', 200

# local çalıştırma
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
