def fac(a, n):
    for i in range(1, n + 1):
        a = a * i
    print("Факториал ", n, ": ", a)


x = int(input("Введите число: "))
facc = 1
fac(facc, x)
