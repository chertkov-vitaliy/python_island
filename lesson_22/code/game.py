import pickle
import random
import os


class Game:
    def __init__(self, rn=random.randint(1, 100), atmp=5):
        obj = {'random_number': None,
               'attempt': None,
               'name_save_game': None}
        self.random_number = rn
        self.attempt = atmp
        print(self.random_number)

    def __del__(self):
        print("Ваша песенка спета!")

        #return (attempt, random_number)

    def engine(self):
        while self.attempt > 0:
            input_number = int(input('Введите любое число'))
            self.attempt -= 1
            if input_number == self.random_number:
                print('Вы угадали!')
                exit(0)
            elif input_number > self.random_number:
                print(f'Искомое число меньше! Количество оставшихся попыток: {self.attempt}')
            elif input_number == 0:
                name_save_game = str(input('Сохранить как: '))

                self.obj['random_number'] = self.random_number
                self.obj['attempt'] = self.attempt
                self.obj['name_save_game'] = name_save_game
                with open('./savegame/' + name_save_game + '.pkl', 'wb') as fp:
                    pickle.dump(self.obj, fp)
                    print("Ваша игра записана!")
                break
            else:
                print('Искомое число больше')

        print('Вы исчерпали количество попыток')

    def run_(self):
        menu = """
            1. Начать игру 
            2. Загрузить игру
            0. Сохранить игру
        """
        print(menu)

        пункт_меню = int(input('Введите пункт меню: '))
        match пункт_меню:
            case 1:
                self.engine()
            case 2:
                dir_ = os.listdir('./savegame')
                for file in dir_:
                    print(file)
                name_save_game = str(input('Введите файл: '))
                with open('./savegame/' + name_save_game, "rb") as f:
                    obj = pickle.load(f)

                self.random_number = obj['random_number']
                self.attempt = obj['attempt']
                print(f"Игра {obj['name_save_game']} восстановлена! ")
                self.engine()


player1 = Game()
player1.run_()
del player1







