import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Yardım başlıkları (25’ten fazla ise gruplanacak)
yardim_butonlari = [
    ("📊 CP Seviyeleri", "cp"),
    ("🏰 Klan Oluşturma", "klan"),
    ("🎵 Müzik İndirme", "muzik"),
    ("📦 Şanslı Paket", "sansli"),
    ("👤 Cinsiyet Değişikliği", "cinsiyet"),
    ("📱 Doğrulama Kodu", "dogrulama"),
    ("📧 E-Posta Doğrulama", "eposta"),
    ("🖼️ Afiş Boyutu", "afis"),
    ("👥 Profil Boyutu", "profil"),
    ("🗑️ Hesap Silme", "hesap"),
    ("🎬 GIF Nasıl Yapılır?", "gifvideo"),
    ("📌 Çok Önemli", "cokonemli"),
    ("📋 Yardım Kuralları", "yardimkurallari"),
    ("⏱️ Atılma Süreleri", "atilmasure"),
    ("🌍 Panel Ülkeler", "ulkeler"),
    ("🍇 Meyve Sorunu", "meyveneden"),
    ("🍇 Meyve Ödülleri", "meyveodul"),
    ("🎓 Hesap Bağlama", "hesapbagla"),
    ("📢 Klan Şikayetleri", "klansikayet"),
    ("⭐ Aristokrasi", "aristokrasi"),
    ("📸 Özelden İfşa", "ifsa"),
    ("🌐 Yurtdışı Uygulama", "yurtdisi"),
    ("🎧 Android Müzik", "androidmuzik"),
    ("👑 Süper Adminler", "superadmin")
]

# Hazır bildirim butonları (20’yi aşarsa gruplanacak)
hazir_butonlari = [
    ("🕓 Afk", "afk"),
    ("📱 Uygulama Reklamı", "reklam"),
    ("📞 Görüntülü Sohbet", "goruntulu"),
    ("📸 İfşa Bildirimi", "ifsa_bildirim"),
    ("👥 Klon Kullanıcı", "klon"),
    ("🗣️ Argo ve Küfür", "kufur"),
    ("🛡️ Klan Başvurusu", "klanbasvuru"),
    ("📷 Uygunsuz Arka Plan", "arka"),
    ("🚫 Şiddet Profil", "siddet"),
    ("🗳️ Siyasi Profil", "siyasi"),
    ("👑 Kötüye Aristokrasi", "kotu_aristo"),
    ("💢 Panel Argo", "panelargo"),
    ("📍 Panel Türkiye", "paneltr"),
    ("🔇 Yayın Sabotaj", "sabotaj"),
    ("📄 Uygunsuz Biyografi", "biyografi"),
    ("🖼️ Uygunsuz Profil Resmi", "profilresmi"),
    ("🆔 Uygunsuz Nick", "nick"),
    ("🙋 Yusuf Bey Bilgi", "yusuf"),
    ("🗯️ Panel Argo Kullanımı", "panelargo2"),
    ("💢 Oda Kaosu", "kaos"),
    ("🚫 Pornografik Görsel", "porno"),
    ("🚫 Aristo Satışı", "aristosatis"),
    ("🔞 Oyun Argo", "oyunargo"),
    ("🌑 Karartılmış Profil", "karartma"),
    ("👤 Kişisel Bilgi İfşası", "kisiselifsa"),
    ("📱 Oyun Reklamı", "oyunreklam"),
    ("🎵 Siyasi Şarkı", "sarkiprop"),
    ("⚠️ Tekrar Aristo Satışı", "aristo2")
]

def grup_gonder(chat_id, liste, komut_baslik, prefix):
    toplam = len(liste)
    gruplar = [liste[i:i+20] for i in range(0, toplam, 20)]
    for index, grup in enumerate(gruplar):
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(*[InlineKeyboardButton(text, callback_data=callback) for text, callback in grup])
        baslik = f"{komut_baslik} {index + 1}/{len(gruplar)}:"
        bot.send_message(chat_id, baslik, reply_markup=markup)

@bot.message_handler(commands=["yardim"])
def yardim_mesaji(message):
    grup_gonder(message.chat.id, yardim_butonlari, "📘 Yardım", "yardim")

@bot.message_handler(commands=["hazir", "hazır", "hazirbildirimler", "hazırbildirimler"])
def hazir_mesaji(message):
    grup_gonder(message.chat.id, hazir_butonlari, "📝 Hazır Bildirim", "hazir")

@bot.callback_query_handler(func=lambda call: True)
def cevapla(call):
    cevaplar = {
        # Yardım cevapları
        "cp": "📊 CP Seviyeleri ve Gereken Hediyeler:\n0 - 1 → 1.000.000\n1 - 2 → 5.000.000\n2 - 3 → 10.000.000\n3 - 4 → 20.000.000\n4 - 5 → 50.000.000\n5 - 6 → 100.000.000\nToplam: 186.000.000",
        "klan": "🏰 Mevcut klanı dağıttıktan sonra, yeni klan için bir sonraki ayın başına kadar beklemelisiniz.",
        "muzik": "🎵 Müzik İndirme:\nhttps://mp3indirdur.life/",
        "sansli": "📦 Şanslı Paket:\nCihaz olağandışı kullanıldıysa sistem tarafından riskli olarak işaretlenmiş olabilir. Normal kullanım sonrası 24 saat içinde yeniden denenebilir.",
        "cinsiyet": "👤 Cinsiyet Değişikliği:\n30 gün içerisinde değiştirilebilir. Süre sonrası talep geçersiz olur.",
        "dogrulama": "📱 Doğrulama Kodu:\n24 saatte en fazla 3 kez alınabilir. Aksi durumda 24 saat bekleyin.",
        "eposta": "📧 E-Posta Doğrulama:\nSaatte en fazla 5 kez alınabilir. 1 saat sonra tekrar deneyin.",
        "afis": "🖼️ Etkinlik Afiş Boyutu: 636x362 piksel",
        "profil": "👥 Oda ve Kişi Profil Fotoğrafı: 800x800 piksel",
        "hesap": "🗑️ Hesap Silme:\nProfil > Ayarlar > Hesap > Hesabı Sil → 30 gün giriş yapılmazsa hesap silinir.",
        "cokonemli": "📌 Çok Önemli:\n1- Cinsiyet değişimi yapılmaz\n2- Klan hakkında bilgi verilmez\n3- Çekim bilgisi verilmez, sadece link yönlendirilir (7010 ID, 66 Şifre).",
        "yardimkurallari": "📋 Yardım Odası Kuralları:\n1. Mikrofona sadece tek kişi alınır.\n2. Yayın devri admin izniyle yapılır.\n3. Nick dışında hitap edilmez.\n4. Kaosa katılınmaz.",
        "atilmasure": "⏱️ Destek Odasından Atılma Süreleri:\nAFK: 10 dk\nYayını sabote: 10 dk\nKüfür: 10 dk\nNot: Elif Hanım bilgisi olmadan uzun atım yapılmaz.",
        "ulkeler": "🌍 Panel Ülkeleri:\nAzerbaycan, Türkmenistan, Özbekistan, Tacikistan → 7007 ID'li odaya yönlendirilir.",
        "meyveneden": "🍇 Meyve Oyunu Sorunu:\nYeni kullanıcılar için Onur ve Cazibe seviyesi 3 olmalıdır.",
        "meyveodul": "🍇 Meyve Oyunu Ödülleri:\n1. olup aristokrasi alamayan kullanıcılar Yusuf Bey veya Kumru Hanım’a yönlendirilir.",
        "hesapbagla": "🎓 Hesap Bağlama:\nProfilim > Ayarlar > Hesap → Bağla/Kaldır menüsünden yapılabilir.",
        "klansikayet": "📢 Klan Şikayetleri:\nKlan bilgisi verilmez. Sadece başvuru alınır, RCS adminlerine yönlendirilir.",
        "aristokrasi": "⭐ Aristokrasi Hediye Etme:\nDetaylı bilgi için 7010 ID ve 66 Şifreli Vip Yardım Odası'na yönlendirin.",
        "ifsa": "📸 Özelden İfşa:\nTarihli kağıt + selfie ile teyit alınır. İfşa edilen kişinin profil SS’i ile admin etiketlenir.",
        "yurtdisi": "🌐 Yurtdışı Uygulama İndirme:\niPhone & Android:\nhttps://youtu.be/uQxuilRNtuc",
        "androidmuzik": "🎧 Android Müzik İndirme:\nhttps://www.snaptube.com/tr/",
        "superadmin": "👑 Süper Adminlerimiz:\nElif (Genel)\nYusufcan & Kumru (VIP)\nKadir (Klanlar)\nFurkan (Reklam)\nAdelph (Türkî Devletler)",

        # Hazır bildirimler aşağıya eklenmiştir:
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
        "nick": "ID :\nUygunsuz nick name.\n@",
        "yusuf": "ID :\nYusuf Bey kullanıcı bilgi almak istiyor ama VIP odasındaki asistanlar yardımcı olmuyor.\n@Yusufcan31",
        "panelargo2": "ID :\nPanelde Argo Kullanımı.\n@",
        "kaos": "ID :\nOda içinde küfür eden diğer kullanıcılar ile adminleri kışkırtıyor.\n@",
        "porno": "ID :\nPanel üzerinde pornografik görsel paylaşımı.\n@",
        "aristosatis": "ID :\nKural dışı aristokrasi satışı.\n@",
        "oyunargo": "ID :\nOyun aktifken argo ve küfür kullanımı mevcut.\n@",
        "karartma": "ID :\n\"Karartılmış profil resmi\"\n@",
        "kisiselifsa": "İfşa Yapan Hesap:\nİfşası Yapılan Hesap:\nKişisel bilgi paylaşımı.\n@",
        "oyunreklam": "ID :\nFarklı uygulama oyunları gösterimi.\n@",
        "sarkiprop": "ID :\nPropaganda amaçlı mikrofonda siyasi şarkı çalmak.\n@",
        "aristo2": "ID :\nTekrar kural dışı aristokrasi satışı.\n@"
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
