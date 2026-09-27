#начало кода
import math
import random

print('DEFwall MultiTool')
print()

#цикл
while True:
    print('___________________________________________________________________')
    print()

#вывод команд
    print('1. Сумма «+»')
    print('2. Разность «-»')
    print('3. Умножение «*»')
    print('4. Деление «/»')
    print('  4.1. Деление без остатка «//»')
    print('  4.2. Остаток от деления «%»')
    print('5. Степень числа «**»')
    print('6. Произведение с числом пи «π»')
    print('7. Корень из числа «√»')
    print('8. Синус числа «sin»')
    print('9. Косинус числа «cos»')
    print('10. Тангенс числа «tan»')
    print('11. Факториал числа «!»')
    print('12. Случайное число «random»')
    print('13. Случайное число от 1 до 100 «random»')
    print('14. Случайное число от x до y «random»')
    print('15. Модуль «||»')
    print('16. Перевод в двоичную систему')
    print('17. Перевод в восьмеричную систему')
    print('18. Перевод в шестнадцатеричную систему')
    print('19. Перевод текста в UNICODE')
    print('20. Перевод числа UNICODE в символ')
    print('21. Остановка программы «STOP»')
    print()

#ввод команд
    operation = (input('Выберите номер операции:'))
    print()
    
#операция суммы
    if operation == '1':
        first_num = float(input('Введите первое число:'))
        last_num = float(input('Введите второе число:'))
        print()
        if first_num == int(first_num) and last_num == int(last_num):
            print(f'{int(first_num)} + {int(last_num)} =', int(first_num + last_num))
            print()
        elif first_num == int(first_num):
            print(f'{int(first_num)} + {last_num} =', first_num + last_num)
            print()
        elif last_num == int(last_num):
            print(f'{first_num} + {int(last_num)} =', first_num + last_num)
            print()
        else:
            print(f'{first_num} + {last_num} =', first_num + last_num)
            print()

#операция разности
    if operation == '2':
        first_num = float(input('Введите первое число:'))
        last_num = float(input('Введите второе число:'))
        print()
        if first_num == int(first_num) and last_num == int(last_num):
            print(f'{int(first_num)} - {int(last_num)} =', int(first_num - last_num))
            print()
        elif first_num == int(first_num):
            print(f'{int(first_num)} - {last_num} =', first_num - last_num)
            print()
        elif last_num == int(last_num):
            print(f'{first_num} - {int(last_num)} =', first_num - last_num)
            print()
        else:
            print(f'{first_num} - {last_num} =', first_num - last_num)
            print()

#операция умножения
    if operation == '3':
        first_num = float(input('Введите первое число:'))
        last_num = float(input('Введите второе число:'))
        print()
        if first_num == int(first_num) and last_num == int(last_num):
            print(f'{int(first_num)} * {int(last_num)} =', int(first_num * last_num))
            print()
        elif first_num == int(first_num):
            print(f'{int(first_num)} * {last_num} =', first_num * last_num)
            print()
        elif last_num == int(last_num):
            print(f'{first_num} * {int(last_num)} =', first_num * last_num)
            print()
        else:
            print(f'{first_num} * {last_num} =', first_num * last_num)
            print()

#операция деления
    if operation == '4':
        first_num = float(input('Введите первое число:'))
        last_num = float(input('Введите второе число:'))
        print()
        if last_num == 0:
            print('Неправильный ввод: на ноль делить нельзя!')
            print()
        elif first_num == int(first_num) and last_num == int(last_num):
            print(f'{int(first_num)} / {int(last_num)} =', first_num / last_num)
            print()
        elif first_num == int(first_num):
            print(f'{int(first_num)} / {last_num} =', first_num / last_num)
            print()
        elif last_num == int(last_num):
            print(f'{first_num} / {int(last_num)} =', first_num / last_num)
            print()
        else:
            print(f'{first_num} / {last_num} =', first_num / last_num)
            print()

#операция деления без остатков
    if operation == '4.1':
        first_num = float(input('Введите первое число:'))
        last_num = float(input('Введите второе число:'))
        print()
        if last_num == 0:
            print('Неправильный ввод: на ноль делить нельзя!')
            print()
        elif first_num == int(first_num) and last_num == int(last_num):
            print(f'{int(first_num)} // {int(last_num)} =', int(first_num // last_num))
            print()
        elif first_num == int(first_num):
            print(f'{int(first_num)} // {last_num} =', first_num // last_num)
            print()
        elif last_num == int(last_num):
            print(f'{first_num} // {int(last_num)} =', first_num // last_num)
            print()
        else:
            print(f'{first_num} // {last_num} =', first_num // last_num)
            print()

#операция вывода остатка деления
    if operation == '4.2':
        first_num = float(input('Введите первое число:'))
        last_num = float(input('Введите второе число:'))
        print()
        if last_num == 0:
            print('Неправильный ввод: на ноль делить нельзя!')
            print()
        elif first_num == int(first_num) and last_num == int(last_num):
            print(f'{int(first_num)} % {int(last_num)} =', int(first_num % last_num))
            print()
        elif first_num == int(first_num):
            print(f'{int(first_num)} % {last_num} =', first_num % last_num)
            print()
        elif last_num == int(last_num):
            print(f'{first_num} % {int(last_num)} =', first_num % last_num)
            print()
        else:
            print(f'{first_num} % {last_num} =', first_num % last_num)
            print()

#операция возведения в степень
    if operation == '5':
        first_num = float(input('Введите первое число:'))
        last_num = int(input('Введите второе число:'))
        print()
        if first_num == int(first_num):
            print(f'{int(first_num)} ** {last_num} =', int(first_num ** last_num))
            print()
        else:
            print(f'{first_num} ** {last_num} =', first_num ** last_num)
            print()

#операция произведения с числом π
    if operation == '6':
        first_num = float(input('Введите число:'))
        print()
        if first_num == int(first_num):
            print(f'π * {int(first_num)} =', math.pi * int(first_num))
            print()
        else:
            print(f'π * {first_num} =', math.pi * first_num)
            print()

#операция вывода квадратного корня числа
    if operation == '7':
        first_num = float(input('Введите число:'))
        print()
        if first_num < 0:
            print('Неправильный ввод: корень из отрицательного числа нельзя найти!')
            continue
        if first_num == int(first_num):
            print(f'√{int(first_num)} =', math.sqrt(first_num))
            print()
        else:
            print(f'√{first_num} =', math.sqrt(first_num))
            print()

#операция вывода синуса числа
    if operation == '8':
        first_num = float(input('Введите число:'))
        print()
        if first_num == int(first_num):
            print(f'sin{int(first_num)}° =', math.sin(math.radians(first_num)))
            print()
        else:
            print(f'sin{first_num}° =', math.sin(math.radians(first_num)))
            print()

#операция вывода косинуса числа
    if operation == '9':
        first_num = float(input('Введите число:'))
        print()
        if first_num == int(first_num):
            print(f'cos{int(first_num)}° =', math.cos(math.radians(first_num)))
            print()
        else:
            print(f'cos{first_num}° =', math.cos(math.radians(first_num)))
            print()

#операция вывода тангенса числа
    if operation == '10':
        first_num = float(input('Введите число:'))
        print()
        if first_num == int(first_num):
            print(f'tan{int(first_num)}° =', math.tan(math.radians(first_num)))
            print()
        else:
            print(f'tan{first_num}° =', math.tan(math.radians(first_num)))
            print()

#операция вывода факториала числа
    if operation == '11':
        first_num = int(input('Введите число:'))
        print()
        if first_num < 0:
            print('Неправильный ввод: факториал из отрицательного числа нельзя найти!')
        else:
            print(f'{first_num}! =', math.factorial(first_num))
            print()

#операция вывода случайного числа
    if operation == '12':
        randchar = random.randint(-9999999999999, 9999999999999)
        print(randchar)
        print()
        
#операция вывода случайного числа от 1 до 100
    if operation == '13':
        randchar = random.randint(1, 100)
        print(randchar)
        print()
       
#операция вывода случайного числа от x до y
    if operation == '14':
        x = int(input('Введите число «x»:'))
        y = int(input('Введите число «y»:'))
        print()
        randchar = random.randint(x, y)
        print(randchar)
        print()
        
#операция модуль
    if operation == '15':
        modul = float(input('Введите число:'))
        print(abs(modul))
        print()
        
#перевод в двоичную систему счисления
    if operation == '16':
        char = int(input('Введите число:'))
        print(bin(char)[2:])
        print()
        
#перевод в восьмеричную систему счисления
    if operation == '17':
        char = int(input('Введите число:'))
        print(oct(char)[2:])
        print()
        
#перевод в шестнадцатеричную систему счисления')
    if operation == '18':
        char = int(input('Введите число:'))
        print(hex(char)[2:])
        print()
        
#перевод текста в unicode
    if operation == '19':
        text = input('Введите текст:')
        for i in range(len(text)):
            char = text[i]
            print(ord(char), end = ' ')
        print()
        
#перевод числа unicode в символ
    if operation == '20':
        char = int(input('Введите число:'))
        print(chr(char))
        print()
    
#операция остановки кода
    if operation == '21':
        print('___________________________________________________________________')
        print()
        print('Калькулятор остановлен')
        print('by DEFwall :)')
        break

#исключения ввода операции
    if operation != '1' and operation != '2' and operation != '3' and operation != '4' and operation != '4.1' and operation != '4.2' and operation != '5' and operation != '6' and operation != '7' and operation != '8' and operation != '9' and operation != '10' and operation != '11' and operation != '12' and operation != '13' and operation != '14' and operation != '15' and operation != '16' and operation != '17' and operation != '18' and operation != '19' and operation != '20' and operation != '21':
        print('Неверный ввод номера операции')
#конец кода by DEFwall :)
