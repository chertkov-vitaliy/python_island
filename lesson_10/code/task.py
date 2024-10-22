#todo: Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных аргументов
#
max_ = lambda x, y: y if x < y else x
print((lambda x, y: y if x < y else x)(4,1))
print(max_(4,1))
#
#
# #todo: Для каждого значения из списка mass получите
# # список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
func = lambda val: val in range(1, 131)
print(list(map(func,mass)))


key = ["name", "age", "weight"]
value = ["Lilu", 25, 100 ]
set_ = [{x: y} for x in key for y in value ]
print(set_)

#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
print(list(filter( lambda val:  val%2 != 0,  list_ )))


def upload_to_yandex_disk(file):
    print(file)
    pass

files = [, 'file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
play_list = [file for file in files if file[-3:] == 'mp3']
print(list(map(upload_to_yandex_disk, play_list)))