from datetime import date
from bot_config.properties import *
from bot_config.messages import *
import telebot
import gspread
from aiogram import types

#приветствуем пользователя и рассказываем о боте
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,startMesssage)


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