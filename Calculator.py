import math

Vibor = """Выберите действие:
1. Сложение 
2. Умножение
3. Деление 
4. Вычитание 
5. Квадратное уравнение"""
print(Vibor)
zadacha = int(input())
if zadacha == 1:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    otvet = x + y
    stroka = str(otvet)
    print("Ответ: ", stroka)
if zadacha == 2:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    otvet = x * y
    stroka = str(otvet)
    print("Ответ: ", stroka)
if zadacha == 3:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    if y == 0:
        print("На ноль делить нельзя")
    else:
        otvet = x / y
        stroka = str(otvet)
        print("Ответ: ", stroka)
if zadacha == 4:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    otvet = x - y
    stroka = str(otvet)
    print("Ответ: ", stroka)
if zadacha == 5:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    print("Введите третье число")
    z = int(input())
    disc = (y ** 2) - (4 * x * z)
    if disc < 0:
        print("Корней нет")
    if disc == 0:
        otvet = -y / (2 * x)
        stroka = str(otvet)
        print("Корень уравнения: ", stroka)
    if disc > 0:
        koren1 = (-y + math.sqrt(disc)) / (2 * x)
        koren2 = (-y - math.sqrt(disc)) / (2 * x)
        stroka1 = str(koren1)
        stroka2 = str(koren2)
        print("Корни квадратного уравнения: ", stroka1, " и ", stroka2)
if zadacha < 1 or zadacha > 5:
    print("Ошибка: введите число от 1 до 5")
