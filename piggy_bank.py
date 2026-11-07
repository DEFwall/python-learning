#---------------Начало-кода-----------------
stop = int(input('Введите цель в «₽»:'))
print('_____________________________________________')
money = 0
days = 1
while money <= stop - 1:
    s = int(input(f'Введите вклад за {days} день: '))
    money += s
    days += 1
    if stop > money:
        print(f'Еще осталось {stop - money}₽!')
print('_____________________________________________')
print(f'Ураа, вы достигли своей цели в {stop}₽!')
days -= 1
if days % 10 == 1 and days % 100 != 11:
    print(f'Всего прошел {days} день!')
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    print(f'Всего прошло {days} дня!')
else:
    print(f'Всего прошло {days} дней!')
#---------------Конец-кода-By-DEFwall-:)---------------
