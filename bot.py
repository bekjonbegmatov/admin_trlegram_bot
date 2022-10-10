import config
import telebot
import requests
import urllib
from io import BytesIO
from PIL import Image
from telebot import types 
import random
from datetime import datetime

url='https://random.imagecdn.app/500/150'

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return str(current_time)

def rendo():
    num = round(random.uniform(1,100))
    print(num)
    if num%2==0:
        return "Mayli"
    else:
        return "YOQ !!!"

is_echo = True
bot = telebot.TeleBot(config.token_admin)

@bot.message_handler(commands=['help'])
def start_message(message):
	bot.send_message(message.chat.id, "/soat soatni bilish uchun ⏱")
	bot.send_message(message.chat.id, "/maylimi ruhsat birishim bermasligim uchun 🆗🚫")
	bot.send_message(message.chat.id, "/info uzingiz haqingizda malumon uchun 💁‍♂️💁")
	bot.send_message(message.chat.id, "/man_qaytta qayrdaligingizni bilish uchun ℹ️")
	bot.send_message(message.chat.id, "/img randomni rasim tashlayman 🏞🗾🌁🌃")
	bot.send_message(message.chat.id, "/ummon_link ummonni qushiqlarini silkasini beraman 😎")

# --------------- commands------------#

@bot.message_handler(commands=['soat'])
def start_message(message):
	bot.send_message(message.chat.id,'хозир соат ' + time() )


@bot.message_handler(commands=['maylimi'])
def start_message(message):
	bot.send_message(message.chat.id, rendo() )

@bot.message_handler(commands=['man_qaytta'])
def start_message(message):

    if message.from_user.first_name == "Samandar":
	    bot.send_message(message.chat.id, "Toshloq" )
    else:
	    bot.send_message(message.chat.id, "Qishloq" )

@bot.message_handler(commands=['site']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Behruz movie", url='https://bekjonbegmatov.github.io/movies')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markupkup)
# bot.polling(none_stop=True)

@bot.message_handler(commands=['info'])
def start_message(message):
	bot.send_message(message.chat.id, "Sani oting " +  str(message.from_user.first_name))
	bot.send_message(message.chat.id, "Sani familang " + str(message.from_user.last_name))
	bot.send_message(message.chat.id, "San hozzir  " + str(message.chat.title) + "gruppada san")
	bot.send_message(message.chat.id, "Sani levling " + str(message.chat.type))
#---------------- text command -----------------#
@bot.message_handler(commands=['img'])
def image_message(message):
    img_url = "https://random.imagecdn.app/500/150"
    img = requests.get(img_url).content
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.chat.id)
    bot.send_message(message.chat.id, "Mana rasm " +  str(message.from_user.first_name))
@bot.message_handler(commands=['stop'])
def stop_echo_message(message):
    is_echo = False
    bot.send_message(message.chat.id, str(is_echo))
@bot.message_handler(commands=['start'])
def stop_echo_message(message):
    is_echo = True
    bot.send_message(message.chat.id, str(is_echo))
@bot.message_handler(commands=['ummon_link'])
def send_ummon_link(message):
    bot.send_message(message.chat.id, 'OOOO mana haqiqy bola ' + str(message.from_user.first_name) + ' \nUmmon busa Ummon da \nhttp://zamonaviy.com/index/0-4 \n👆👆👆Ummonni barcha qushiqlari \n https://play.google.com/store/apps/details?id=umon.qoshiqlar&hl=ru&gl=US\n👆👆👆 Ummon qushiqlari 2022 programmasi \nhttps://www.youtube.com/watch?v=5bEChjylcEQ \n 👆👆👆 Qnady unutting !!')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "нахуй" or message.text == "Пашол" or message.text == "Хе онени" or message.text == "далбаёб" or message.text == "пидарас":
        bot.send_message(message.chat.id, message.from_user.first_name+" Сукинма !!! 😡🤬")

    if message.text == "салом" or message.text == 'salom' or message.text == 'alo':
        bot.send_message(message.chat.id, message.from_user.first_name+" салом !!! \n bormi sanam bitta uzim ziriktim ku \n qolganla qaytta ? 🤨")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши Привет")
    else:
        if is_echo == True:
            bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()