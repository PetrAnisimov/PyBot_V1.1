from bot_config.messages import *
from bot_config.properties import *

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,startMesssage)