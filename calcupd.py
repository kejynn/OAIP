import math

Vibor = """Выберите действие:
1. Сложение 
2. Умножение
3. Деление 
4. Вычитание 
5. Квадратное уравнение"""
print(Vibor)
zadacha = int(input())
if 0 < zadacha < 5:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    def sum(a, b):
        return a + b
    def raz(a, b):
        return a - b
    def pr(a, b):
        return a * b
    def chast(a, b):
        return a / b
    if zadacha == 1:
        print("Ответ: ", sum(x, y))
    elif zadacha == 2:
        print("Ответ: ", pr(x, y))
    elif zadacha == 3:
        if y == 0:
            print("На ноль делить нельзя")
        else:
            print("Ответ: ", chast(x, y))
    elif zadacha == 4:
        print("Ответ: ", raz(x, y))
elif zadacha == 5:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    z = int(input("Введите третье число: "))
    def disc (a, b, c):
        return (b ** 2) - (4 * a * c)
    def disc0 (a, b):
        return -b / (2 * a)
    def koren (a, b, dis):
        return (-b + math.sqrt(dis)) / (2 * a), (-b - math.sqrt(dis)) / (2 * a)
    disk = disc(x, y, z)
    if disk < 0:
        print("Корней нет.")
    if disk == 0:
        print("Корень уравнения: ", disc0(x, y))
    if disk > 0:
        print("Корни уравнения:", koren(x, y, disk))
else:
    print("Ошибка: введите число от 1 до 5")