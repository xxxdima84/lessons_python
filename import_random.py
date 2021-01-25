import random
trice=0
print ('отгадайте число от 1 до 50 - у вас 6 попыток')
a = random.randint(1,50)
while trice < 6:
    b=int(input('введите пожалуста число '))
    trice=trice +1
    
    if b > a:
        print ('компютер загадал меньшее число')
        
    if b < a:
        print ('компютер загадал большее число')
        
    if b==a:
        print(f'Поздравляю вы отгадали число за {trice} попыток')
        break
        
    if a!=b and trice == 6:
        print(f'Вы исчерпали количество попыток я загадал {a}')
        break
input()