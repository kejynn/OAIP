def sum(a, n):
    for i in range(n + 1):
        a = a + i
    print("Сумма чисел от 1 до ", n, ": ", a)


x = int(input("Введите число: "))
summ = 0
sum(summ, x)
