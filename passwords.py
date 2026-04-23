attempts = 0
while True:
    correct = ["111111", "1488", "abc123"]
    a = (input("Пароль! : "))
    if a in correct:
        print("Добро Пожаловать, сударь!")
        break
    else:
        print("Неверно! Попробуй ещё раз.")
        attempts += 1
        if attempts == 3:
            print("Всё! Попытки закончились.")
            break