from datetime import date
import telebot
import gspread

bot_token = "5117456487:AAGPJIKWZPwfe2Crx36BIjWrmcJ0eMvOmDs"
googlesheet_id = "154Y1awRqDm1vrNDcEkBxG0zyYAWZiGBZjSWX1KcMKyk"
bot = telebot.TeleBot(bot_token)
gc = gspread.service_account()

#приветствуем пользователя и рассказываем о боте
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,'Привет, я буду записывать твои рассходы в таблицу. Введи расход через дефис в виде [КАТЕГОРИЯ-ЦЕНА]')

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
        bot.send_message(message.chat.id, 'ОШИБКА! Неправильный формат данных')

    bot.send_message(message.chat.id,'Введи расход через дефис в виде [КАТЕГОРИЯ-ЦЕНА]')

if __name__ == '__main__':
     bot.polling(none_stop=True)