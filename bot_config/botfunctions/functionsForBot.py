from bot_config.properties import *

# открываем  Google таблицу и добавляем запись
def openAndAddlineInSheet(today=None,category=None,price=None):
    sh = gc.open_by_key(googlesheet_id)
    sh.sheet1.append_row([today, category, price])

