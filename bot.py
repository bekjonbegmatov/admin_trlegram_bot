import config
import telebot
import requests
import urllib
from io import BytesIO
from PIL import Image
from telebot import types 
import random
from datetime import datetime
import youtube_dl

# Vorebls 
sukinishla = ['']
hazilla = [
    'Salom boja, qalaysiz,\nNega moylov silaysiz?\nАytgancha, moylov oshni,\nOsmasdan qovoq-qoshni,\nQilib bersangiz tezroq,\nOzidan kopi sozroq.' , 
    'Bazi qogozdagi hisobotlar strelkasiz soatga oxshaydi.\nRaqamlar boru, manosi yoq!', 
    'Nega kopchilik onalar instagramda farzandlarini yuzlarini berkitib qoyishadi-yu, kinozalga kirganda ogzilari berkita olishmaydi.',
    'Pul – insonga hech qachon vafo qilmaydi.\nKochaga pul bilan chiqib ketasan, uyga nuqul yolgiz qaytasan!',
    '— Ayrim raqamlarni ataylab, shu raqamdan boladigan qongiroqlarni kotarmaslik uchungina telefonga saqlab qoyaman.',
    '— Oyliklarni oshirib bering!— Oshdi-ku!\n— Bizlarnikini degandik...\n Ozingiznikini emas!',
    'Yozgi ish jadvali:\nPashshalar uchun - 05:00dan 20:00 gacha.\nChivinlar uchun - 20:00dan 05:00 gacha.',
    '— Jarohatlovchi qurolingizni ozingiz bilan olvoldingizmi?\n— Ha, albatta. Mana, tilim joyida turibdi.',
    '— Vanihoyat, "jinnini yoqish"ni organib oldim. Juda foydali ekan.\n— Sen "ochirishni" organishing kerak edi-ku!',
    'Dam olish uchun Limpopoga borishga pulingiz yetmasa, Turkiyaga boring...!',
    '2-3 yildan keyin umuman kasal bolmasligimiz kerak. Chunki hozir onlayn oqigan talaba vrachlar institutni bitirib ish boshlashadi',
    '— Qoshnilarda nima gaplar?\n— Yana odatdagidek, sanksiyalar olishdi.\n— Paketga solib berishdimi?',
    'Shu kunlarda odamlar latifa va hazillarni tushunmay qolishdi. Ular buni narx-navodagi yana bir yangilik deb oylashmoqda.',
]
    # echo bot setting defoult value is False
is_echo = True
    # Our bot 
bot = telebot.TeleBot(config.token_admin)
    # url for random image
url='https://random.imagecdn.app/500/150'
    # url for weather
locaturl = "https://api.weatherapi.com/v1/current.json?key=f68b6746b6504d11ad2124737223004&q=Gulakandoz&aqi=no"
# function retutns time 
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return str(current_time)

#funny function
def funny():
    num = round(random.uniform(0, 1000))
    print(num)
    n = int(num%len(hazilla))
    return hazilla[n]

# function for command maylimi 
def rendo():
    num = round(random.uniform(1,100))
    print(num)
    if num%2==0:
        return "Mayli"
    else:
        return "YOQ !!!"

# Send instruction about this bot
@bot.message_handler(commands=['help'])
def start_message(message):

	bot.send_message(message.chat.id, "/soat soatni bilish uchun ⏱ \n/maylimi ruhsat birishim bermasligim uchun 🆗🚫 \n/info uzingiz haqingizda malumon uchun 💁‍♂️💁 \n/man_qaytta qayrdaligingizni bilish uchun ℹ️ \n/img randomni rasim tashlayman 🏞🗾🌁🌃\n/ummon_link ummonni qushiqlarini silkasini beraman 😎 \n/sinifdoshlar_instagrami sinifdoshlani instagramdaygi profillari 📱\n/hazil Birorta hazil tashlayman 😂 \n/havo Gulakandozdaygi obu havoni bilish uchin 🌤🌥 ")


# --------------- commands------------#
@bot.message_handler(commands=['havo'])
def start_message(message):


    data = requests.get(locaturl)
    c = data.json()['current']
    temp_c = c['temp_c']
    temp_f = c['temp_f']
    condition = c['condition']
    text = condition['text']
    icon = condition['icon']

    img_url = "https:" + str(icon)
    img = requests.get(img_url).content
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.chat.id)
    bot.send_message(message.chat.id, "Hozzir havo : \nSelsi buyicha : " + str(temp_c) +'\nFarangeyt buyicha :'+ str(temp_f) +'\nHozzir havo '+ str(text) +'\n')


    # bot.send_message(message.chat_id, str(temp_c) +'\n'+ str(temp_f) +'\n'+ str(text) +'\n'+ str(icon))
    # pass

@bot.message_handler(commands=['soat'])
def start_message(message):
	bot.send_message(message.chat.id,'хозир соат ' + time()  )

# Return Funny str 

@bot.message_handler(commands=['hazil'])
def start_message(message):
	bot.send_message(message.chat.id, funny() + '\n 😂😂😂😂😂😂')

# Confirm for you yes or no and send 

@bot.message_handler(commands=['maylimi'])
def start_message(message):
	bot.send_message(message.chat.id, rendo() )

# Send information about yor location 

@bot.message_handler(commands=['man_qaytta'])
def start_message(message):

    if message.from_user.first_name == "Samandar" or message.from_user.first_name == 'Усмонжон':
	    bot.send_message(message.chat.id, "Toshloq" )
    if message.from_user.first_name == "_{=B©b¥®=}_":
        bot.send_message(message.chat.id, "Hoshim Qishloq" )
    else:
	    bot.send_message(message.chat.id, "Qishloq" )

# Returt button for link to my site

@bot.message_handler(commands=['site']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Behruz movie", url='https://bekjonbegmatov.github.io/movies')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markupkup)

# Return information about your account

@bot.message_handler(commands=['info'])
def start_message(message):
	bot.send_message(message.chat.id, "Sani oting " +  str(message.from_user.first_name))
	bot.send_message(message.chat.id, "Sani familang " + str(message.from_user.last_name))
	bot.send_message(message.chat.id, "San hozzir  " + str(message.chat.title) + "gruppada san")
	bot.send_message(message.chat.id, "Sani levling " + str(message.chat.type))

# Send rendom image to the chat 

@bot.message_handler(commands=['img'])
def image_message(message):
    img_url = "https://random.imagecdn.app/500/150"
    img = requests.get(img_url).content
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.chat.id)
    bot.send_message(message.chat.id, "Mana rasm " +  str(message.from_user.first_name))

# The command for exiting in echo bot 

@bot.message_handler(commands=['stop'])
def stop_echo_message(message):
    is_echo = False
    bot.send_message(message.chat.id, str(is_echo))

# The command for starting echo bot 

@bot.message_handler(commands=['start'])
def stop_echo_message(message):
    is_echo = True
    bot.send_message(message.chat.id, str(is_echo))

# Sent Ummon songs

@bot.message_handler(commands=['ummon_link'])
def send_ummon_link(message):
    bot.send_message(message.chat.id, 'OOOO mana haqiqy bola ' + str(message.from_user.first_name) + ' \nUmmon busa Ummon da \nhttp://zamonaviy.com/index/0-4 \n👆👆👆Ummonni barcha qushiqlari \n https://play.google.com/store/apps/details?id=umon.qoshiqlar&hl=ru&gl=US\n👆👆👆 Ummon qushiqlari 2022 programmasi \nhttps://www.youtube.com/watch?v=5bEChjylcEQ \n 👆👆👆 Qnady unutting !!')

#  Sent instagram account links  

@bot.message_handler(commands=['sinifdoshlar_instagrami'])
def sinifdoshlar_ingtagtami(message):
	bot.send_message(message.chat.id, 'SINIGDOSHLAR INSTAGRAMI 📺 \nBehruz😎 👉 https://www.instagram.com/behruz_1106_/ \nSanandar(Khabib)😏 👉 https://www.instagram.com/samandar_h0813/ \n Samandar 😃 👉 https://www.instagram.com/_samandar_haydarov_/ \n Bobur 🤠 👉 https://www.instagram.com/bobur_gr88/ \n Usmonjon 🤑 👉 https://www.instagram.com/usmonjo_2005_/ \n Behzod 🙂 👉 https://www.instagram.com/behzod_2005_/ \n Husan 🤨 👉 https://www.instagram.com/bokievkhusanzhon/ \n Ohunjon 😊 👉 https://www.instagram.com/ohun.jon09/ \n Mehruz 🧑‍💻 👉 https://www.instagram.com/mehruz_rahimi/ \n Ekhson 😝 👉 https://www.instagram.com/ekhson8146/' )

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

@bot.message_handler(commands=['ytdl'])
def down(msg):
    args = msg.text.split()[1]
    try:
        with ydl:
            result = ydl.extract_info(
                args,
                download=False  # We just want to extract the info
            )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        
        for i in video['formats']:
            link = '<a href=\"' + i['url'] + '\">' + 'link' + '</a>'
            if i.get('format_note'):
                bot.reply_to(msg, 'Quality-' + i['format_note'] + ': ' + link, parse_mode='HTML')
            else:
                bot.reply_to(msg, link, parse_mode='HTML', disable_notification=True)
    except:
        bot.reply_to(msg, 'This can\'t be downloaded by me')

# text commands 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "нахуй" or message.text == "Пашол" or message.text == "Хе онени" or message.text == "далбаёб" or message.text == "пидарас":
        bot.send_message(message.chat.id, message.from_user.first_name+" Сукинма !!! 😡🤬")

    if message.text == "салом" or message.text == 'salom' or message.text == 'alo':
        bot.send_message(message.chat.id, message.from_user.first_name+" салом !!! \n bormi sanam bitta uzim ziriktim ku \n qolganla qaytta ? 🤨")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши Привет")
    print(message)
    # else:
    #     if is_echo == True:
    #         bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()