import telebot
import gspread

#данные для связи с google таблицей
googlesheet_id = "154Y1awRqDm1vrNDcEkBxG0zyYAWZiGBZjSWX1KcMKyk"

#данные для связи с телеграм ботом
bot_token = "5117456487:AAGPJIKWZPwfe2Crx36BIjWrmcJ0eMvOmDs"

bot = telebot.TeleBot(bot_token)
gc = gspread.service_account()

#название столбцов
rowItem = 2
rowPrice = 3