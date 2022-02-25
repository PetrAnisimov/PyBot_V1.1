
from bot_config.messages import *
from bot_config.properties import *
from bot_config.botfunctions.functionsForBot import openAndAddlineInSheet
from datetime import date


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,startMesssage)

@bot.message_handler(commands=['returnPrice'])
def listPrice(message):
    bot.send_message(message.chat.id, itemsPrice)
    sh = gc.open_by_key(googlesheet_id)
    for price in sh.sheet1.col_values(rowPrice):
        bot.send_message(message.chat.id, price)

@bot.message_handler(commands=['returnItem'])
def listItem(message):
    bot.send_message(message.chat.id,itemsList)
    sh = gc.open_by_key(googlesheet_id)
    for items in sh.sheet1.col_values(rowItem):
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
        openAndAddlineInSheet(today,category,price)

    except:
        #если пользователь ввел не верную информацию мы его оповещаем, и просим ввести повторно
        bot.send_message(message.chat.id, errorMessage)

    bot.send_message(message.chat.id,messageForAddingDataAgain)

