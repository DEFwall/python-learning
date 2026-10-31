#переменные, списки и ввод
password = input('Введите пароль:')
print()
list_password = []
upperslowers = 0
notchars = '@$%&#!*^$'

#тест пароля
if len(password) >= 8:
    list_password.append('size')
for i in range(len(password)):
    if password[i].isdigit():
        list_password.append('digits')
        break
for j in range(len(password)):
    if password[j].isalpha():
        list_password.append('chars')
        break
for k in range(len(password)):
    if password[k].isupper():
        upperslowers += 1
        break
for h in range(len(password)):
    if password[h].islower():
        upperslowers += 1
        break
if upperslowers == 2:
    list_password.append('upperslowers')
for l in range(len(notchars)):
    if notchars[l] in password:
        list_password.append('notchars')
        break

#результаты теста
if 'size' in list_password:
    print('Длина пароля больше или равно 8: есть')
else:
    print('Длина пароля больше или равно 8: нет')
if 'digits' in list_password:
    print('Наличие цифр: есть')
else:
    print('Наличие цифр: нет')
if 'chars' in list_password:
    print('Наличие букв: есть')
else:
    print('Наличие букв: нет')
if 'upperslowers' in list_password:
    print('Наличие больших и маленьких букв одновременно: есть')
else:
    print('Наличие больших и маленьких букв одновременно: нет')
if 'notchars' in list_password:
    print('Наличие других символов: есть')
else:
    print('Наличие других символов: нет')

#вывод теста
print()    
print(f'Уровень пароля: {len(list_password)}/5', end = ' ')
if len(list_password) == 1:
    print('(очень слабо)')
if len(list_password) == 2:
    print('(слабо)')
if len(list_password) == 3:
    print('(среднее)')
if len(list_password) == 4:
    print('(хорошее)')
if len(list_password) == 5:
    print('(отличное)')
#конец кода by DEFwall :)
