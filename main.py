import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# /yardim ana menü
@bot.message_handler(commands=['yardim'])
def yardim_index(message):
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("📘 Yardım 1", callback_data="yardim1"),
        InlineKeyboardButton("📗 Yardım 2", callback_data="yardim2")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Yardım bölümlerinden birini seçin:", reply_markup=markup)

# /yardim1 detaylı yardım 1
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

# /yardim2 detaylı yardım 2
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

# /hazir ana menü
@bot.message_handler(commands=['hazir', 'hazır', 'hazirbildirimler', 'hazırbildirimler'])
def hazir_index(message):
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("📘 Hazır 1", callback_data="hazir1"),
        InlineKeyboardButton("📗 Hazır 2", callback_data="hazir2")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Hazır bildirim bölümlerinden birini seçin:", reply_markup=markup)

# /hazir1 detaylı hazır 1
@bot.message_handler(commands=['hazir1'])
def hazir1(message):
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
        InlineKeyboardButton("🗳️ Siyasi Profil", callback_data="siyasi")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📘 Hazır Bildirim 1:", reply_markup=markup)

# /hazir2 detaylı hazır 2
@bot.message_handler(commands=['hazir2'])
def hazir2(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("👑 Kötüye Kullanılan Aristokrasi", callback_data="kotu_aristo"),
        InlineKeyboardButton("💢 Panel Argo", callback_data="panelargo"),
        InlineKeyboardButton("📍 Panel Türkiye", callback_data="paneltr"),
        InlineKeyboardButton("🔇 Yayın Sabotaj", callback_data="sabotaj"),
        InlineKeyboardButton("📄 Uygunsuz Biyografi", callback_data="biyografi"),
        InlineKeyboardButton("🖼️ Uygunsuz Profil Resmi", callback_data="profilresmi"),
        InlineKeyboardButton("🆔 Uygunsuz Nick", callback_data="nick"),
        InlineKeyboardButton("🙋 Yusuf Bey Bilgi", callback_data="yusuf"),
        InlineKeyboardButton("🗯️ Panel Argo Kullanımı", callback_data="panelargo2"),
        InlineKeyboardButton("💢 Oda Kaosu", callback_data="kaos")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📗 Hazır Bildirim 2:", reply_markup=markup)

# Yardım ve hazır yönlendirme
@bot.callback_query_handler(func=lambda call: True)
def buton_yonlendir(call):
    if call.data == "yardim1":
        yardim1(call.message)
    elif call.data == "yardim2":
        yardim2(call.message)
    elif call.data == "hazir1":
        hazir1(call.message)
    elif call.data == "hazir2":
        hazir2(call.message)
    else:
        bot.answer_callback_query(call.id, text="Yükleniyor...")

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
