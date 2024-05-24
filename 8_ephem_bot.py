"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


today = datetime.date.today()
planet_dict = {'Mars': ephem.Mars(today), 'Venus': ephem.Venus(today), 'Saturn': ephem.Saturn(today),
               'Jupiter': ephem.Jupiter(today), 'Neptune': ephem.Neptune(today), 'Uranus': ephem.Uranus(today),
               'Mercury': ephem.Mercury(today)}


def determine_the_constellation(update, context):

    planet = update.message.text.split()[1]
    update.message.reply_text(planet)
    check_planet = planet_dict.get(planet, None)
    if check_planet != None:
        constellation = ephem.constellation(planet_dict[planet])
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('Я не знаю такую планету')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater('7037713875:AAF_z0V0jj6BkIjPJBmr8MVX8KSJDz9ULz0', use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", determine_the_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
