#Ввод    
print("Давай сыграем в камень, ножницы, бумага.")
    while True:
    a = input('Выбери "Камень", "Ножницы" или "Бумага":')
#Переменные
    bumaga = "Бумага"
    nozhnicyi = "Ножницы"
    kamen = "Камень"
#Действие и вывод
    import random
    b = random.choice([kamen, nozhnicyi,     bumaga])
    if (a == "Бумага" or a == "бумага") and b == kamen:
        print("Ты выиграл! Я выбрал:", kamen)
    if (a == "Бумага" or a == "бумага") and b == bumaga:
        print("У нас ничья, я выбрал:", bumaga)
    if (a == "Бумага" or a == "бумага") and b == nozhnicyi:
        print("Ты проиграл, я выбрал:", nozhnicyi)
    if (a == "Камень" or a == "камень") and b == nozhnicyi:
        print("Ты выиграл! Я выбрал:", nozhnicyi)
    if (a == "Камень" or a == "камень") and b == kamen:
        print("У нас ничья, я выбрал:", kamen)
    if (a == "Камень" or a == "камень") and b == bumaga:
        print("Ты проиграл, я выбрал:", bumaga)
    if (a == "Ножницы" or a == "ножницы") and b == bumaga:
        print("Ты выиграл! Я выбрал:", bumaga)
    if (a == "Ножницы" or a == "ножницы") and b == nozhnicyi:
        print("У нас ничья, я выбрал:", nozhnicyi)
    if (a == "Ножницы" or a == "ножницы") and b == kamen:
        print("Ты проиграл, я выбрал:", kamen)
    if a != "Бумага" and a != "бумага" and a != "Камень" and a != "камень" and a != "Ножницы" and a != "ножницы":
        print('Неправильный ввод, попробуй например "Бумага"')
    c = input('Сыграем еще?"Да", "Нет":')
    if c == "Нет" or c == "нет":
        print()
        print()
        print()
        print("My first game :)")
        print("by DEFwall")
        break
#Конец
