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


bot = telebot.TeleBot(config.token_admin)

@bot.message_handler(commands=['help'])
def start_message(message):
	bot.send_message(message.chat.id, "/soat soatni bilish uchun")
	bot.send_message(message.chat.id, "/maylimi ruhsat birishim bermasligim uchun")
	bot.send_message(message.chat.id, "/info uzingiz haqingizda malumon uchun")
    # bot.send_message(message.chat.id, "/man_qaytta uzingiz haqingizda malumon uchun")

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

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "нахуй":
        bot.send_message(message.chat.id, message.from_user.first_name+" Сукинма !!!")
    if message.text == "Пашол":
        bot.send_message(message.chat.id, message.from_user.first_name+" Сукинма !!!")
    
    if message.text == "салом":
        # bot.send_message(message.chat.id, message.from_user.first_name+" салом !!!")
        bot.send_message(message.chat.id, message.from_user.first_name+" салом !!!")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши Привет")
    else:
        bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()