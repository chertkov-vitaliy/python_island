#!/usr/bin/env python
#todo: Дописать проверку на именование файлов, сделать транслитерацию с
# русского на английский язык. Заменить в названиях пробелы на нижнее подчеркивание.

import os
# folder path
DIR_PATH = '/home/vitaliy/download'
os.chdir(DIR_PATH)

# Функция возвращает множество расширений файлов
def get_files_list():
    # list to store files
    res = []
    # Iterate directory
    for path in os.listdir(DIR_PATH):
        # check if current path is a file
        if os.path.isfile(os.path.join(DIR_PATH, path)):
            res.append(path.split('.').pop(-1))
    else:
        return  set(res)


def mk_dir_and_move(dirs):
    for i in dirs:
        if not os.path.exists(i):
            os.mkdir(i)
        os.system(f"mv *.{i}  {i}")


def run():
    dirs = get_files_list()
    mk_dir_and_move(dirs)

if __name__ == "__main__":
    run()
