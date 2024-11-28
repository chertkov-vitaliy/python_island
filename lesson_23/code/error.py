result = None
try:
     result = 100/0
     print("Расчёт проведён успешно")

except KeyError as e:
     print("Ошибка обращения по ключу произошла:", e)

except Exception as e:
     print("Ошибка ", e.__class__)
     result = 0

except ZeroDivisionError as e:
     result = 0
     print("Ошибка деления произошла", e)


