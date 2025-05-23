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

# Metinli cevaplar
@bot.callback_query_handler(func=lambda call: True)
def cevapla(call):
    cevaplar = {
        # Yardım cevapları (kısaltıldı örnek için)
        "cp": "CP Seviyeleri:\n0 - 1 → 1.000.000\n1 - 2 → 5.000.000...",
        "klan": "Klan Oluşturma: Mevcut klanı dağıttıktan sonra yeni klan için süre beklenmeli.",
        "muzik": "Müzik indirme:\nhttps://mp3indirdur.life/",
        "gifvideo": None,  # özel video
        # Hazır bildirimler örnek
        "afk": "ID :\nAfk kaldığı için 10 dakika uzaklaştırıldı\n@elifdn61",
        "reklam": "ID :\nFarklı uygulama reklamı.\n@",
        "goruntulu": "ID :\nGörüntülü Sohbet Talep Ediyor.\n@elifdn61",
        "ifsa_bildirim": "İfşa Yapan Hesap :\nİfşası Yapılan Hesap :\nTeyit Resmi özelinize gönderildi.\n@",
        "klon": "Klonlanan Kullanıcı ID:\nKlonlama Yapan Kullanıcı ID:\n@",
        "kufur": "ID :\nMikrofonda argo ve küfür.\n@",
        "klanbasvuru": "Klan Başvurusu\nOda ID :\nKullanıcı ID :\n@",
        "arka": "ID :\nUygunsuz arka plan resmi.\n@",
        "siddet": "ID :\nŞiddet içerikli profil resmi.\n@",
        "siyasi": "ID :\nSiyasi profil resmi.\n@",
        "kotu_aristo": "Oda ID :\nAristokrasisini kötüye kullanan kullanıcı mevcut.\n@",
        "panelargo": "ID :\nPanel üzerinde argo ve küfür.\n@",
        "paneltr": "ID :\nPanel Türkiye olarak güncellenecek.\n@elifdn61",
        "sabotaj": "ID :\nYayını sabote ettiği için 10 dakika uzaklaştırıldı\n@elifdn61",
        "biyografi": "ID :\nUygunsuz biyografi.\n@",
        "profilresmi": "ID :\nUygunsuz Profil resmi.\n@",
        "nick": "ID :\nUygunsuz nick name .\n@",
        "yusuf": "ID :\nYusuf Bey kullanıcı bilgi almak istiyor ama VIP odasındaki asistanlar yardımcı olmuyor.\n@Yusufcan31",
        "panelargo2": "ID :\nPanelde Argo Kullanımı.\n@",
        "kaos": "ID :\nOda içinde diğer kullanıcılar da küfür etmekte. Ancak bu kullanıcı, adminleri kışkırtıyor.\n@",
        "porno": "ID :\nPanel üzerinde pornografik görsel paylaşımı.\n@",
        "aristosatis": "ID :\nKural dışı aristokrasi satışı.\n@",
        "oyunargo": "ID :\nOyun aktifken argo ve küfür kullanımı mevcut.\n@",
        "karartma": "ID :\n\"Karartılmış profil resmi\"\n@",
        "kisiselifsa": "İfşa Yapan Hesap :\nİfşası Yapılan Hesap :\nKişisel bilgi paylaşımı .\n@",
        "oyunreklam": "ID :\nFarklı uygulama oyunları gösterimi.\n@",
        "sarkiprop": "ID :\nPropaganda yapmak amaçlı Mikrofonda siyasi şarkı çalmak.\n@",
        "aristo2": "ID :\nKural dışı aristokrasi satışı.\n@"
    }

    if call.data == "gifvideo":
        with open("gif_nasil_yapilir.mp4", "rb") as video:
            bot.send_video(call.message.chat.id, video)
    else:
        yanit = cevaplar.get(call.data, "Bu konuda bilgi bulunamadı.")
        bot.send_message(call.message.chat.id, yanit)
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
