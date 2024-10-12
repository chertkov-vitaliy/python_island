from random import randint as ri
words: None
desc_: None
attempt = 0
def init():
    global words, desc_
    words = ["operator", "constract", "object"]
    desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования.",
               "Это синтаксическая структура, которая определяет способ организации кода.",
               "Это сущность, представляющая собой экземпляр класса." ]
def get_attemt():
    return attempt

def set_attemt():
    global attempt
    attempt += 1

def get_word():
    global words
    word_index = ri(0, len(words) - 1)
    print_(word_index)
    return words[word_index]

def print_(word_index):
    global desc_
    print("Угадайте слово по подсказке: " + desc_[word_index] + "\n")

def get_field(word_for_play):
     return [" ▒"] * len(word_for_play)

def get_letter():
    letter = input(f"\nУ вас осталось {10 - get_attemt()} попыток! \nВведите букву: ")
    return letter

def engine(word_for_play,player_word):
    pass

def game():
    init()
    word_for_play = get_word()
    player_word = get_field(word_for_play)
    print("".join(player_word))
    engine(word_for_play, player_word )


print('''
*******************************
********* ПОЛЕ ЧУДЕС **********

1. Начать игру !
2. Выйти.

''')

key = int(input('Ваш выбор % '))

match key:
    case 1:
        game()
    case 2:
        exit(0)