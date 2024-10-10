#todo 3.2:  Известно, что сейф открывается при правильном вводе
# кода из 3 цифр 0...9. Задайте код и затем откройте сейф, ис-
# пользуя метод перебора с помощью нескольких операторов
# цикла for.
from random import randint as ri

x = ri(0,9)
y = ri(0,9)
z = ri(0,9)

code = [x, y, z]
print(x,y,z)


indx = [None]*3
for i in range(10):
    if i in code:
        start = 0
        for j in range(code.count(i)):
            indx_first =  code.index(i, start )
            indx[indx_first] = i
            start = indx_first + 1
else:
    print(indx)





#web

head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
'''

footer = '''
  </body>
  </html>
'''
elements = ["Первый пункт списка",
            "Другой пункт списка",
            "Еще один пункт списка"]

ul = "<ul>"
for li in elements:
    ul  += "\n<li>" + li + "</li>"

html = head + ul + "</ul>" + footer
print(html)

fd = open('index.html', 'w+' )
fd.write(html)
fd.close()


