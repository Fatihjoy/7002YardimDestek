import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(content_types=['text'])
def yanitla(message):
    text = message.text.strip().lower()
    if text == "cp seviyeleri":
        yanit = (
            "CP Seviyeleri ve Gereken Hediyeler:\n\n"
            "0 - 1 → 1.000.000\n"
            "1 - 2 → 5.000.000\n"
            "2 - 3 → 10.000.000\n"
            "3 - 4 → 20.000.000\n"
            "4 - 5 → 50.000.000\n"
            "5 - 6 → 100.000.000\n\n"
            "Toplam: 186.000.000"
        )
        bot.reply_to(message, yanit)
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

# /yardim komutu → inline butonlu yardım menüsü
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
        InlineKeyboardButton("🗑️ Hesap Silme", callback_data="hesap")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Yardım menüsünden bir konu seçin:", reply_markup=markup)

# Butona basıldığında cevabı göster
@bot.callback_query_handler(func=lambda call: True)
def cevapla(call):
    cevaplar = {
        "cp": "📊 CP Seviyeleri ve Gereken Hediyeler:\n\n0 - 1 → 1.000.000\n1 - 2 → 5.000.000\n2 - 3 → 10.000.000\n3 - 4 → 20.000.000\n4 - 5 → 50.000.000\n5 - 6 → 100.000.000\n\nToplam: 186.000.000",
        "klan": "🏰 Klan Oluşturma:\nMevcut klanı dağıttıktan sonra, yeni bir klan için bir sonraki ayın başına kadar beklemeniz gerekir.",
        "muzik": "🎵 Müzik İndirme:\nhttps://mp3indirdur.life/",
        "sansli": "📦 Şanslı Paket:\nCihaz olağandışı kullanıldığı için sistem tarafından riskli cihaz olarak tanımlanmış olabilir. Normal kullanım sonrası 24 saat içinde paket tekrar açılabilir.",
        "cinsiyet": "👤 Cinsiyet Değişikliği:\nKayıttan itibaren 30 gün içinde değiştirilebilir. Bu süreden sonra yapılan talepler işleme alınmaz.",
        "dogrulama": "📱 Doğrulama Kodu:\n24 saat içinde en fazla 3 kez alınabilir. Aksi durumda 24 saat beklenmelidir.",
        "eposta": "📧 E-Posta Doğrulama:\nHer saat en fazla 5 kez alınabilir. 1 saat sonra tekrar denenebilir.",
        "afis": "🖼️ Etkinlik Afişi Boyutu:\n636x362 piksel",
        "profil": "👥 Oda ve Kişi Profil Fotoğrafı:\n800x800 piksel",
        "hesap": "🗑️ Hesap Silme:\nProfil > Ayarlar > Hesap > Hesabı Sil\nSilme başvurusundan sonra 30 gün giriş yapılmazsa hesap silinir. Giriş yapılırsa iptal olur."
    }

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, cevaplar.get(call.data, "Bu konuda bilgi bulunamadı."))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
