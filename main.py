import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['yardim'])
def yardim_index(message):
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("📘 Yardım 1", callback_data="yardim1"),
        InlineKeyboardButton("📗 Yardım 2", callback_data="yardim2")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Yardım bölümlerinden birini seçin:", reply_markup=markup)

@bot.message_handler(commands=['yardim1'])
def yardim1(message):
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
        InlineKeyboardButton("📋 Yardım Kuralları", callback_data="yardimkurallari"),
        InlineKeyboardButton("⏱️ Atılma Süreleri", callback_data="atilmasure"),
        InlineKeyboardButton("🌍 Panel Ülkeler", callback_data="ulkeler"),
        InlineKeyboardButton("🍇 Meyve Sorunu", callback_data="meyveneden"),
        InlineKeyboardButton("🍇 Meyve Ödülleri", callback_data="meyveodul"),
        InlineKeyboardButton("🎓 Hesap Bağlama", callback_data="hesapbagla"),
        InlineKeyboardButton("📢 Klan Şikayetleri", callback_data="klansikayet")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📘 Yardım 1:", reply_markup=markup)

@bot.message_handler(commands=['yardim2'])
def yardim2(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("⭐ Aristokrasi Hediyesi", callback_data="aristokrasi"),
        InlineKeyboardButton("📸 Özelden İfşa", callback_data="ifsa"),
        InlineKeyboardButton("🌐 Yurtdışı Uygulama", callback_data="yurtdisi"),
        InlineKeyboardButton("🎧 Android Müzik", callback_data="androidmuzik"),
        InlineKeyboardButton("👑 Süper Adminler", callback_data="superadmin")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📗 Yardım 2:", reply_markup=markup)

@bot.message_handler(commands=['hazir', 'hazır', 'hazirbildirimler', 'hazırbildirimler'])
def hazir_index(message):
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("📘 Hazır 1", callback_data="hazir1"),
        InlineKeyboardButton("📗 Hazır 2", callback_data="hazir2")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Hazır bildirim bölümlerinden birini seçin:", reply_markup=markup)

@bot.message_handler(commands=['hazir1'])
def hazir1(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("🕓 Afk", callback_data="afk"),
        InlineKeyboardButton("📱 Uygulama Reklamı", callback_data="reklam"),
        InlineKeyboardButton("📞 Görüntülü Sohbet", callback_data="goruntulu"),
        InlineKeyboardButton("📸 İfşa", callback_data="ifsa_bildirim"),
        InlineKeyboardButton("👥 Klon Kullanıcı", callback_data="klon"),
        InlineKeyboardButton("🗣️ Argo ve Küfür", callback_data="kufur"),
        InlineKeyboardButton("🛡️ Klan Başvurusu", callback_data="klanbasvuru"),
        InlineKeyboardButton("📷 Uygunsuz Arka Plan", callback_data="arka"),
        InlineKeyboardButton("🚫 Şiddet Profil", callback_data="siddet"),
        InlineKeyboardButton("🗳️ Siyasi Profil", callback_data="siyasi")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📘 Hazır Bildirim 1:", reply_markup=markup)

@bot.message_handler(commands=['hazir2'])
def hazir2(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("👑 Kötüye Kullanılan Aristokrasi", callback_data="kotu_aristo"),
        InlineKeyboardButton("💢 Panel Argo", callback_data="panelargo"),
        InlineKeyboardButton("📍 Panel Türkiye", callback_data="paneltr"),
        InlineKeyboardButton("🔇 Yayın Sabotaj", callback_data="sabotaj"),
        InlineKeyboardButton("📄 Uygunsuz Biyografi", callback_data="biyografi"),
        InlineKeyboardButton("🖼️ Profil Resmi", callback_data="profilresmi"),
        InlineKeyboardButton("🆔 Uygunsuz Nick", callback_data="nick"),
        InlineKeyboardButton("🙋 Yusuf Bilgi", callback_data="yusuf"),
        InlineKeyboardButton("🗯️ Panel Argo 2", callback_data="panelargo2"),
        InlineKeyboardButton("💢 Oda Kaosu", callback_data="kaos")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📗 Hazır Bildirim 2:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def buton_yonlendir(call):
    cevaplar = {
        "cp": "📊 CP Seviyeleri ve Gereken Hediyeler:\n0 - 1 → 1.000.000...",
        "klan": "Klan Oluşturma hakkında bilgi...",
        "muzik": "🎵 Müzik indirme: https://mp3indirdur.life",
        "sansli": "📦 Şanslı Paket durumu...",
        "cinsiyet": "👤 Cinsiyet bilgisi değişimi...",
        "dogrulama": "📱 Doğrulama Kodu açıklaması...",
        "eposta": "📧 E-Posta doğrulama bilgisi...",
        "afis": "🖼️ Afiş Boyutu: 636x362",
        "profil": "👥 Profil Boyutu: 800x800",
        "hesap": "🗑️ Hesap Silme adımları...",
        "cokonemli": "📌 Çok önemli bilgiler...",
        "yardimkurallari": "📋 Yardım kuralları...",
        "atilmasure": "⏱️ Atılma süreleri açıklaması...",
        "ulkeler": "🌍 Yönlendirilen ülkeler: ...",
        "meyveneden": "🍇 Meyve oyunu sorunu...",
        "meyveodul": "🍇 Meyve oyunu ödülleri...",
        "hesapbagla": "🎓 Hesap bağlama işlemleri...",
        "klansikayet": "📢 Klan şikayetleri...",
        "aristokrasi": "⭐ Aristokrasi hediyesi hakkında...",
        "ifsa": "📸 Özelden ifşa prosedürü...",
        "yurtdisi": "🌐 Yurtdışı uygulama indirme...",
        "androidmuzik": "🎧 Android müzik indirme: https://www.snaptube.com/tr/",
        "superadmin": "👑 Süper admin listesi...",
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
        "kaos": "ID :\nOda içinde diğer kullanıcılar da küfür etmekte. Ancak bu kullanıcı, adminleri kışkırtıyor.\n@"
    }
    if call.data == "gifvideo":
        with open("gif_nasil_yapilir.mp4", "rb") as video:
            bot.send_video(call.message.chat.id, video)
    elif call.data in ["yardim1", "yardim2"]:
        yardim1(call.message) if call.data == "yardim1" else yardim2(call.message)
    elif call.data in ["hazir1", "hazir2"]:
        hazir1(call.message) if call.data == "hazir1" else hazir2(call.message)
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
