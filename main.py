import os
import telebot

API_TOKEN = os.environ.get("BOT_TOKEN")  # ✔️ Çevresel değişkenden al
bot = telebot.TeleBot(API_TOKEN)


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

    elif text == "klan oluşturma":
        yanit = (
            "Bir kullanıcı mevcut klanını dağıttıktan sonra, yeni bir klan oluşturabilmek için "
            "bir sonraki ayın başına kadar beklemek zorundadır.\n\n"
            "Bu nedenle, klan başvurusu yapan her kullanıcıya en son ne zaman klan açtığını soruyoruz."
        )
        bot.reply_to(message, yanit)

    elif text == "müzik indirme programı":
        bot.reply_to(message, "🔗 https://mp3indirdur.life/\nAdım adım görseller aşağıda:")
        try:
            with open("gorsel1.jpg", 'rb') as img1:
                bot.send_photo(message.chat.id, img1)
            with open("gorsel2.jpg", 'rb') as img2:
                bot.send_photo(message.chat.id, img2)
        except Exception as e:
            bot.reply_to(message, f"Görseller gönderilemedi: {e}")

    elif text == "şanslı paket":
        yanit = (
            "Dünya Şans Paketi Alınamıyor\n\n"
            "Sebep:\n"
            "Kullanıcının cihazı, olağandışı şekilde kullanıldığı için sistem tarafından riskli cihaz olarak tanımlanmıştır.\n\n"
            "Çözüm:\n"
            "Kullanıcı, cihazını olağandışı koşullarda kullanmaktan kaçınmalıdır.\n"
            "Sistem, cihazın 24 saat içinde normal kullanımda olduğunu tespit ederse, paket tekrar alınabilir hâle gelecektir."
        )
        bot.reply_to(message, yanit)

    elif text == "cinsiyet değişikliği":
        yanit = (
            "Kullanıcılar, kayıt tarihinden itibaren 30 gün içerisinde cinsiyet bilgilerini kendileri değiştirebilirler.\n"
            "Bu sürenin aşılması durumunda yapılan talepler işleme alınmayacaktır."
        )
        bot.reply_to(message, yanit)

    elif text == "neden doğrulama kodu alınamıyor":
        yanit = (
            "📩 SMS Doğrulama Kodu:\n"
            "24 saat içinde en fazla 3 kez doğrulama kodu alınabilir.\n"
            "Bu sınır aşıldığında, tekrar almak için 24 saat beklemek gerekir.\n\n"
            "📡 Diğer Olası Nedenler:\n"
            "Kullanıcının doğrulama kodu alamaması, bulunduğu bölgedeki yerel operatör ve ağ sinyaliyle ilgili olabilir.\n\n"
            "Alternatif:\n"
            "Telefon yerine e-posta adresi bağlanarak, doğrulama kodları e-posta yoluyla alınabilir."
        )
        bot.reply_to(message, yanit)

    elif text == "e-posta doğrulama kodu":
        bot.reply_to(message, "Her saat en fazla 5 kez doğrulama kodu alınabilir.\n1 saat sonra tekrar alınabilir.")

    elif text == "etkinlik afişi boyutu":
        bot.reply_to(message, "📐 Etkinlik afişi boyutu: 636x362")

    elif text == "oda ve kişi profili":
        bot.reply_to(message, "📐 Oda ve kişi profil fotoğrafı boyutu: 800x800")

    elif text == "hesap silme":
        yanit = (
            "APP Üzerinden Hesap Silme Girişi:\n"
            "Profilim → Ayarlar → Hesap → Hesabı Sil yolunu izleyin. Kullanıcı, hesabını kendi başına silebilir.\n\n"
            "Başvuru başarılı olursa, sistem 30 gün sonra hesabı otomatik olarak siler. Bu sürede hesaba giriş yapılamaz. "
            "Eğer kullanıcı yeniden giriş yaparsa, silme başvurusu iptal edilir.\n\n"
            "Hesabın Silinemediği Durumlar:\n"
            "- Özel statüye sahip hesaplar (Klan Lideri/Süper Yönetici)\n"
            "- Hesap anormal durumdaysa (yasaklı, iade sürecinde, şikayet almışsa veya telefon numarası bağlı değil)"
        )
        bot.reply_to(message, yanit)

    else:
        bot.reply_to(message, "Bu konuda bilgi bulunamadı.")

if __name__ == '__main__':
    print("Bot çalışıyor...")
    bot.infinity_polling()
