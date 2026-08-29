#Ввод
sim ="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890=<>&#$%_-+/*!?"
print("Добро пожаловать в генератор паролей")
x = ""
#Генерация и вывод
while True:
    rezim = input('Выберите режим "Сложный"(12 символов),"Простой"(6 цифр):')
    if rezim == "Простой" or rezim == "простой":
        import random
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        d = random.randint(1, 9)
        e = random.randint(1, 9)
        f = random.randint(1, 9)
        print()
        print()
        print("Пароль:", a, b, c, d, e, f, sep = "")
        print("by DEFFwall")
        print()
        print()
        print()    
        x = input('Сгенерировать еще?"Да","Нет":')
    if rezim =="Сложный" or rezim =="сложный":
        import random
        q = random.choice(sim)
        w = random.choice(sim)
        r = random.choice(sim)
        t = random.choice(sim)
        y = random.choice(sim)
        u = random.choice(sim)
        i = random.choice(sim)
        o = random.choice(sim)
        p = random.choice(sim)
        s = random.choice(sim)
        g = random.choice(sim)
        h = random.choice(sim)
        print()
        print()
        print("Пароль:", q, w, r, t, y, u, i, o, p, s, g, h, sep = "")        
        print("by DEFFwall")
        print()
        print()
        print()
        x = input('Сгенерировать еще?"Да","Нет":')
    if rezim != "Простой" and rezim != "простой" and rezim != "Сложный" and rezim != "сложный":
        print()
        print()
        print('Введи режим правильно, например "Простой"')        
        print("by DEFFwall")
        print()
        print()
        print()
        x = input('Сгенерировать еще?"Да","Нет":')
    if x == "Нет" or x == "нет":
        print("Программа завершена")
        break
#Конец 
