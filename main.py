import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

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
        InlineKeyboardButton("🎬 GIF Nasıl Yapılır?", callback_data="gifvideo")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Yardım menüsünden bir konu seçin:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def cevapla(call):
    cevaplar = {
        "cp": "📊 CP Seviyeleri:\n0 - 1 → 1M\n1 - 2 → 5M\n2 - 3 → 10M\n3 - 4 → 20M\n4 - 5 → 50M\n5 - 6 → 100M\nToplam: 186M",
        "klan": "Klan dağıtımından sonra yeni klan başvurusu için 1 ay beklenmeli.",
        "muzik": "https://mp3indirdur.life/",
        "sansli": "Cihaz olağandışı kullanımda → riskli cihaz. 24 saat içinde tekrar alınabilir.",
        "cinsiyet": "Kayıttan itibaren 30 gün içinde değiştirilebilir.",
        "dogrulama": "24 saatte en fazla 3 kez SMS kodu alınabilir.",
        "eposta": "Saatte en fazla 5 kez e-posta doğrulama kodu alınabilir.",
        "afis": "Etkinlik Afişi Boyutu: 636x362",
        "profil": "Oda/Kişi Profil Boyutu: 800x800",
        "hesap": "Profil → Ayarlar → Hesap → Hesabı Sil\n30 gün giriş yapılmazsa hesap silinir.",
        "gif": "🎬 GIF yapımı hakkında bilgi için aşağıdaki videoyu izleyin."
    }

    if call.data == "gifvideo":
        try:
            with open("gif_nasil_yapilir.mp4", "rb") as video:
                bot.send_video(call.message.chat.id, video)
        except Exception as e:
            bot.send_message(call.message.chat.id, f"⚠️ Video gönderilemedi: {e}")
    elif call.data in cevaplar:
        bot.send_message(call.message.chat.id, cevaplar[call.data])
    else:
        bot.send_message(call.message.chat.id, "Bu konuda bilgi bulunamadı.")

@bot.message_handler(func=lambda message: True)
def yanitla(message):
    text = message.text.strip().lower()

    manuel_cevaplar = {
        "cp seviyeleri": "📊 CP Seviyeleri:\n0 - 1 → 1M\n1 - 2 → 5M\n2 - 3 → 10M\n3 - 4 → 20M\n4 - 5 → 50M\n5 - 6 → 100M\nToplam: 186M",
        "klan oluşturma": "Klan dağıtımından sonra yeni klan başvurusu için 1 ay beklenmeli.",
        "müzik indirme programı": "https://mp3indirdur.life/",
        "şanslı paket": "Cihaz olağandışı kullanımda → riskli cihaz. 24 saat içinde tekrar alınabilir.",
        "cinsiyet değişikliği": "Kayıttan itibaren 30 gün içinde değiştirilebilir.",
        "neden doğrulama kodu alınamıyor": "24 saatte en fazla 3 kez SMS kodu alınabilir.",
        "e-posta doğrulama kodu": "Saatte en fazla 5 kez e-posta doğrulama kodu alınabilir.",
        "etkinlik afişi boyutu": "Etkinlik Afişi Boyutu: 636x362",
        "oda ve kişi profili": "Oda/Kişi Profil Boyutu: 800x800",
        "hesap silme": "Profil → Ayarlar → Hesap → Hesabı Sil\n30 gün giriş yapılmazsa hesap silinir.",
        "gif nasıl yapılır": "🎬 GIF yapımı hakkında bilgi için /yardim yazarak butona tıklayın."
    }

    if text in manuel_cevaplar:
        bot.reply_to(message, manuel_cevaplar[text])
    elif text == "/yardim":
        yardim_mesaji(message)
    else:
        bot.reply_to(message, "Bu konuda bilgi bulunamadı.")

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'OK', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
