# Создаём функцию приветствия
def greetings():
    print()
    print()
    print("      Привет!  ")
    print("     Это игра       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" Для игры вводите координаты через пробел: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


# Функция вывода поля
def show_field():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


# Выбор действия пользователя (ввод координат для установки Х и 0)
def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


# Проверка победителя
def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл Нолик!!!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл Нолик!!!")
            return True

    for i in range(3):
        symbols = []
        for i in range(3):
            symbols.append((field[i][i]))
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл Нолик!!!")
            return True

    for i in range(3):
        symbols = []
        for i in range(3):
            symbols.append((field[i][2 - i]))
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл Нолик!!!")
            return True
    return False

# Ход игры
greetings()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print(" Игрок Крестик ходи!")
    else:
        print(" Игрок Нолик ходи!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break