#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      smxdfx
#
# Created:     27.02.2021
# Copyright:   (c) smxdfx 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#import telebot api
import time
from random import randrange
import telebot

# telegram bot token acquired from BotFather
bot = telebot.TeleBot("1087819020:AAG7Zoiz3I19DC7aTBzppao4u66GpOCDA0E")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "ah shit here we go again")
    bot.reply_to(message, "чтобы меня ЗАПУСТИТЬ - напиши Хомячьок")

quiz_started = bool()
reshenie = int()
@bot.message_handler(func=lambda message: message.text == "Хомячьок")
def zapusk_homyachka(m):
    global quiz_started
    quiz_started = True
    if quiz_started == True:
        print ("passed")
        print ("quiz started..")
        bot.send_message(m.chat.id, "запускаю хомячька..")
        time.sleep(3)
        bot.send_message(m.chat.id, "ХОМЯЧЬОК ЗАПУЩЕН!")
        bot.send_photo(m.chat.id, open ('zapusk.jpg', 'rb'))
        first_num = randrange(10)
        second_num = randrange(10)
        global reshenie
        reshenie = first_num + second_num
        bot.send_message(m.chat.id, ("ЧТОБЫ ПОЙМАТЬ ХОМЯЧЬКА РЕШИ ЗАДАЧЬКУ: " + ((str(str(first_num)) + "+" + (str(second_num))))))
        print (reshenie)
        @bot.message_handler(func=lambda message: message.text == str(reshenie))
        def homyachka_poymali(m):
            global reshenie
            print("making sure, solution is:" + str(reshenie))
            global quiz_started
            while quiz_started == True:
                bot.send_photo(m.chat.id, open ('success.jpg', 'rb'))
                quiz_started = False
                print ("quiz finished..")
        @bot.message_handler(func=lambda message: message.text != str(reshenie))
        def homyachok_failed(m):
            global reshenie
            global quiz_started
            while quiz_started == True:
                print("making sure, solution is:" + str(reshenie))
                bot.send_message(m.chat.id, "Вы не сумели поймать хомячька..")
                quiz_started = False
                print ("quiz finished..")

bot.polling()