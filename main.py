from datetime import date
from botcommands import commands
from bot_config.properties import *
from bot_config.messages import *

import telebot
import gspread
from aiogram import types


#приветствуем пользователя и рассказываем о бот
def send_welcome(message):
    return send_welcome(message)

@bot.message_handler(commands=['returnItem'])
def list(message):
    bot.send_message(message.chat.id, 'Вот список ваших заказов:')
    sh = gc.open_by_key(googlesheet_id)
    for items in sh.sheet1.col_values(2):
        bot.send_message(message.chat.id, items)



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        today = date.today().strftime("%d.%m.%y")

        # разделяю сообщение на 2 части, категрия цена
        category, price = message.text.split("-", 1)
        text_message = f'На {today} в таблицу расходов добавлена запись: категория {category}, сумму{price} сум'
        bot.send_message(message.chat.id, text_message)

        #открываем  Google таблицу и добавляем запись
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, category, price])

    except:
        #если пользователь ввел не верную информацию мы его оповещаем, и просим ввести повторно
        bot.send_message(message.chat.id, errorMessage)

    bot.send_message(message.chat.id,messageForAddingDataAgain)

if __name__ == '__main__':
     bot.polling(none_stop=True)