"""
1. Game
2. Save Game
3. Exit
"""
#*******************#
# Игра "Поле чудес !"

word = "арбуз"
field = ['x'] * len(word)
m_word = list(word)

while 'x' in field:
    letter = input("Введите букву:")
    for key in range(len(word)):
        if word[key] == letter:
            field[key] = letter
    else:
        print(field)
else:
    print("Игра закончена!")

for i in 'hello world':
    if i == 'l':
        break
else:
    print('Буквы a в строке нет')

exit(0)


#*********************#
# Игра "Угадай число !"

import random
random_number = random.randint(1, 100)
print(random_number)
attempt = 5
for i in '12345'[::-1]:
    input_number = int(input("Введите число:"))
    continue
    if input_number == random_number:
        print("Win!")
        break
    elif input_number > random_number:
        print( f"Искомое число меньше ! Кол-во попыток: {int(i) - 1} ")
    else:
        print(f"Искомое число больше !  Кол-во попыток: {int(i) - 1} ")

print("Вы исчерпали кол-во попыток!")
