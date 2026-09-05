print("Добро пожаловать в игру «кости» с ботом")
print()

a = input("Бросить кость? «Да», «Нет»:")

if a == "Да" or a == "да":
    while True:
        import random
        you = random.randint(1, 6)
        bot = random.randint(1, 6)

        print("У тебя:", you)
        print("У бота:", bot)

        if bot > you:
            print("Бот выиграл")
        elif you > bot:
            print("Ты выиграл")
        else:
            print("У вас ничья")

        print()
        a = input("Сыграть еще? «Да», «Нет»:")

        if a == "Нет" or a == "нет":
            break
else:
    print("Нет, значит нет(")
