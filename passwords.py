attempts = 0
while True:
    correct = ["111111", "1488", "abc123"]
    a = (input("Пароль! : "))
    if a in correct:
        print("Добро Пожаловать, сударь!")
        break
    else:
        attempts += 1
        if attempts >= 3:
            print("Всё! Попытки закончились.")
            break
        else:
            print(f"Неверно! Осталось попыток: {3 - attempts}")