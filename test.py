import gspread

gc = gspread.service_account()
sh = gc.open_by_key("154Y1awRqDm1vrNDcEkBxG0zyYAWZiGBZjSWX1KcMKyk")
print(sh.sheet1.get("A2:D1"))