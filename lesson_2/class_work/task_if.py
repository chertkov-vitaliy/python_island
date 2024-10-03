"""
Дан номер месяца (1 — январь, 2 — февраль, ...).
Вывести название соответствующего времени года
("зима", "весна" и т.д.).
"""
month = 1
match month:
    case 1 | 2:
         print("winter")
    case 3:
         print("winter 2")
    case _:
        pass

""" Задано целое число от 10 до 99 ,
нобходимо найти сумму и произведение
его цифр
"""

_number = 99
def _summ( l_num):
    summ = l_num % 10 + l_num // 10
    return summ

result = _summ(_number)
print(result)
# test result
assert 18 == result


def adam( ):
    belok = "ATG"* 1000
    print(belok)

adam()


# https://pythonim.ru/osnovy/pobitovye-operatory-bitwise-v-python
