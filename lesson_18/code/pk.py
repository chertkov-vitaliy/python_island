import pickle
import random
import os

obj = {'random_number': None,
       'attempt': None,
       'name_save_game': None}


def init(rn=random.randint(1, 100), atmp=5):
    random_number = rn
    print(random_number)
    attempt = atmp
    return (attempt, random_number)


def run(attempt, random_number):
    global obj
    while attempt > 0:
        input_number = int(input('Введите любое число'))
        attempt -= 1
        if input_number == random_number:
            print('Вы угадали!')
            exit(0)
        elif input_number > random_number:
            print(f'Искомое число меньше! Количество оставшихся попыток: {attempt}')
        elif input_number == 0:
            name_save_game = str(input('Сохранить как: '))
            obj['random_number'] = random_number
            obj['attempt'] = attempt
            obj['name_save_game'] = name_save_game
            with open('./savegame/' + name_save_game + '.pkl', 'wb') as fp:
                pickle.dump(obj, fp)
                print("Ваша игра записана!")
            exit(0)
        else:
            print('Искомое число больше')

    print('Вы исчерпали количество попыток')
    print(random_number)
    print(input_number)

menu = """
    1. Начать игру 
    2. Загрузить игру
    0. Сохранить игру
"""
print(menu)
пункт_меню = int(input('Введите пункт меню: '))
match пункт_меню:
    case 1:
        res = init()
        run(*res)
    case 2:
        dir_ = os.listdir('./savegame')
        for file in dir_:
            print(file)
        name_save_game = str(input('Введите файл: '))
        with open('./savegame/' + name_save_game, "rb") as f:
            obj = pickle.load(f)
        res = init(obj['random_number'], obj['attempt'])
        print(f"Игра {obj['name_save_game']} восстановлена! ")
        run(*res)


