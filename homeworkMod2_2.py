# 1
x = 35
print('Добрый день!')
if x<0:
    print('Меньше нуля')
print('До встречи!')
# 2
a, b = 10, 5
if a>b:
    print('a>b')
if a>b and a>0:
    print('Успех!1')
if a>b and (a>0 or b<1000):
    print('Успех!2')
# 3
if '34'>'123':
    print('Успех!3')
if '123'>'12':
    print('Успех!4')
if [1,2]>[1,1]:
    print('Успех!5')
# 4
if '6' != 5:
    print('Успех!6')
if '6'>5:
    print('Успех!7')
if [5,6]>5:
    print('Успех!8')

