from random import randint
print("Введите количество цифр")
num = int(input())
sumpol = 0
sumotr = 0
spisok = []
for i in range(num):
    rnd = randint(-100, 100)
    if rnd == 0:
        while rnd == 0:
            rnd = randint(-100, 100)
    if rnd > 0:
        sumpol = sumpol + rnd
    elif rnd < 0:
        sumotr = sumotr + rnd
    spisok.append(rnd)
print("Сумма положительных чисел равна: ", sumpol)
print("Сумма отрицательных чисел равна: ", sumotr)
print("Полный список чисел: ", spisok)
