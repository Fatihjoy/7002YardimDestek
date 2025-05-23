import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Yardım komutu → butonlu menü
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

# Butonlara basıldığında cevap
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
        "afis": "636x362",
        "profil": "800x800",
        "hesap": "Profil → Ayarlar → Hesap → Hesabı Sil\n30 gün giriş yapılmazsa hesap silinir.",
        "cokonemli": "1- Cinsiyet değişimi yapılmaz\n2- Klan hakkında bilgi verilmez\n3- Çekim bilgisi verilmez, 7010 ID 66 Şifre'li odaya yönlendirilir.",
        "yardimkurallari": "1- Mikrofon paylaşılmaz\n2- Yayın devri admin izniyle olur\n3- Nick dışında hitap edilmez\n...",
        "atilmasure": "AFK: 10 dk\nYayını sabote: 10 dk\nKüfür: 10 dk",
        "ulkeler": "Azerbaycan, Türkmenistan, Özbekistan, Tacikistan → 7007 ID'li odaya yönlendirilir.",
        "meyveneden": "Meyve oyununun açılması için onur ve cazibe seviyesi 3. seviyeye gelmelidir.",
        "meyveodul": "1. olup aristokrasi alamayanlar Yusuf veya Kumru’ya yönlendirilir.",
        "hesapbagla": "Profilim > Ayarlar > Hesap > Bağlantılar üzerinden bağlan/kaldır işlemi yapılır.",
        "klansikayet": "Klan bilgisi verilmez. Yalnızca başvuru alınır.",
        "aristokrasi": "7010 ID – 66 Şifreli odaya yönlendiriniz.",
        "ifsa": "Tarihli kağıt + anlık selfie gönderilmeli. Profil SS’leriyle birlikte panel admini etiketlenmelidir.",
        "yurtdisi": "iPhone & Android: https://youtu.be/uQxuilRNtuc",
        "androidmuzik": "https://www.snaptube.com/tr/",
        "superadmin": "Elif, Yusufcan, Kumru, Kadir, Furkan, Adelph"
    }

    if call.data == "gifvideo":
        with open("gif_nasil_yapilir.mp4", "rb") as video:
            bot.send_video(call.message.chat.id, video)
    else:
        bot.send_message(call.message.chat.id, cevaplar.get(call.data, "Bu konuda bilgi bulunamadı."))

    bot.answer_callback_query(call.id)

# Metin mesajlarına özel cevap
@bot.message_handler(content_types=['text'])
def yanitla(message):
    text = message.text.strip().lower()

    if text == "/yardim":
        yardim_mesaji(message)
        return

    elif text == "cp seviyeleri":
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

# Webhook endpoint
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'OK', 200

# Flask sunucusu
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
