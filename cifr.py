def chis(a, b):
    while a > 0:
        b = b + 1
        a = a // 10
    print("Количесвто цифр в числе: ", b)


x = int(input("Введите число: "))
col = 0
chis(x, col)
