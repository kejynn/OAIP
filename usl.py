vibor = int(input("1. Только одно четное \n"
                  "2. 3 числа кратны трем \n"))

if vibor == 1:
    A = int(input("Введите число A"))
    B = int(input("Введите число B"))
    if A % 2 == 0 and B % 2 == 0 or A % 2 == 1 and B % 2 == 1:
        print("Неверно")
    else:
        print("Верно")

elif vibor == 2:
    A = int(input("Введите число A"))
    B = int(input("Введите число B"))
    C = int(input("Введите число C"))
    if A % 3 == 0 and B % 3 == 0 and C % 3 == 0:
        print("Верно")
    else:
        print("Неверно")