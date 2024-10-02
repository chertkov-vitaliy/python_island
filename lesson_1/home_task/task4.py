# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15
x = 10
y = 15
z = 2
print(max(x,y,z))
# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130
#1.1
x = 77
y = 9
z = 130
if x>y>z:
  print(x)
#1.2
if x>y>z or x>z>y:
  print(x)
elif y>z>x or y>x>z:
  print(y)
else:
    z>y>x or z>x>y
    print(z)
  
