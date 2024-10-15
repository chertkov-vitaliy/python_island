#todo: Написать функцию logger() которая принимает в качестве аргумента
#  текст сообщения который дописывается в файл error.log
#  Новое сообщение должно распологаться на новой строчки.
import datetime

FILE_LOG = 'test.log'

def logger(message_, error_type, line, code, file):
    time = datetime.datetime.now()
    fd = open( FILE_LOG, 'at', encoding="utf-8")
    error = f"{error_type}: {time}: {code}: {line}: {__file__}: {message_} "
    fd.write(error + '\n')
    fd.close()


if __name__ == '__main__':
    logger(error_type='WARNING',
           code=777,
           file=__file__,
           line=12,
           message_="File is locking")