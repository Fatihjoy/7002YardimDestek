import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# /yardim komutu → inline buton menüsü
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
        InlineKeyboardButton("🔔 Çok Önemli", callback_data="cok_onemli"),
        InlineKeyboardButton("📜 Destek Kuralları", callback_data="destek_kurallari"),
        InlineKeyboardButton("⏱️ Atılma Süreleri", callback_data="atilmalar"),
        InlineKeyboardButton("🌍 Panel Ülkeleri", callback_data="panel_ulkeleri"),
        InlineKeyboardButton("🍒 Meyve Açılmıyor", callback_data="meyve_acilmiyor"),
        InlineKeyboardButton("🏆 Meyve Ödülleri", callback_data="meyve_odul"),
        InlineKeyboardButton("👑 Aristokrasi", callback_data="aristokrasi"),
        InlineKeyboardButton("🔐 Hesap Bağlama", callback_data="baglama"),
        InlineKeyboardButton("📦 Sandık Patlama", callback_data="sandik"),
        InlineKeyboardButton("🚫 Özelden İfşa", callback_data="ozelden_ifsa"),
        InlineKeyboardButton("⚔️ Klan Şikayetleri", callback_data="klan_sikayet"),
        InlineKeyboardButton("👤 Süper Adminler", callback_data="adminler"),
        InlineKeyboardButton("📸 İfşa Teyit", callback_data="ifsa_teyit"),
        InlineKeyboardButton("🌍 Uygulama İndirme", callback_data="yurtdisi_indirme"),
        InlineKeyboardButton("🎵 Android Müzik", callback_data="android_muzik")
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "ℹ️ Yardım menüsünden bir konu seçin:", reply_markup=markup)

# Butonlara tıklanınca verilecek yanıtlar
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
        "cok_onemli": "1- Cinsiyet değişimi yapılmaz\n2- Klan hakkında bilgi verilmez, sadece başvuru alınır\n3- Çekim konularında sadece link verilir. 7010 ID 66 şifreli odaya yönlendirin.",
        "destek_kurallari": "1. 1. Mikrofon hariç başka mik'e alınmaz\n2. Mikrofon paylaşılmaz\n3. Yayın teslimi admin onayıyla yapılır\n4. Nick dışında hitap edilmez\n5. Yayın saati dışında kaosa girilmez\n6. 10 dakika sonra yayın alınmaz (mazeret hariç)\n7. Ses yükseltilmez\n8. Diğer admin konuşuyorsa müdahale edilmez\n9. GIF yoksa JoyMi logolu resim zorunlu\n10. Hazır bildirimler kullanılmalı",
        "atilmalar": "AFK: 10 dk\nYayını sabote: 10 dk\nKüfür: 10 dk\nElif hanım dışında 10 dakikadan fazla atılamaz. Yazma yasağı verilmez.",
        "panel_ulkeleri": "Azerbaycan, Türkmenistan, Özbekistan, Tacikistan → 7007 ID'li odaya yönlendirilir.",
        "meyve_acilmiyor": "Onur ve Cazibe seviyesi 3. seviyeye ulaşmadan meyve oyunu açılmaz.",
        "meyve_odul": "1. olan ama aristokrasi alamayan kullanıcılar Yusuf Bey veya Kumru Hanım'a yönlendirilir.",
        "aristokrasi": "Detaylı bilgi verilmez. 7010 ID 66 şifreli Vip yardım destek odasına yönlendirilir.",
        "baglama": "Profil → Ayarlar → Hesap → Telefon/E-posta/Google/Apple ile bağlan. Sadece Google/Apple bağlantısı kaldırılabilir.",
        "sandik": "Lv.1: 500K\nLv.2: 1M\nLv.3: 3.5M\nLv.4: 5M\nLv.5: 15M\nLv.6: 25M\nToplam: 50M ile tüm sandıklar patlar.",
        "ozelden_ifsa": "Video kaydı + ID görünür selfie ile kayıt alınmalı. Teyit resmi panel adminine, ifşa ve SS'ler ile bildirim yapılmalı.",
        "klan_sikayet": "Klanlara dair bilgi verilmez. Başvuru ve RCS için yönlendirme yapılır.",
        "adminler": "Elif: Genel Şikayetler\nYusufcan & Kumru: Vip ve çekim\nKadir: Klanlar\nFurkan: Reklam\nAdelph: Türk devletleri",
        "ifsa_teyit": "El yazısı tarihli selfie → panel adminine\nİfşa yapılan ve yapan hesap + ifşa yeri SS → admin etiketli bildirim",
        "yurtdisi_indirme": "📲 iPhone & Android:\nhttps://youtu.be/uQxuilRNtuc?si=w5tyseQ3AJVEndGg",
        "android_muzik": "🎵 Android müzik indir:\nhttps://www.snaptube.com/tr/"
    }

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, cevaplar.get(call.data, "Bu konuda bilgi bulunamadı."))

# Yazılı sorular için yanıtlar
@bot.message_handler(func=lambda message: True)
def yanitla(message):
    text = message.text.strip().lower()

    if text == "/yardim":
        yardim_mesaji(message)
        return

    for keyword, cevap in cevapla.__globals__['cevaplar'].items():
        if keyword in text:
            bot.reply_to(message, cevap)
            return

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

# Flask sunucusunu başlat
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
