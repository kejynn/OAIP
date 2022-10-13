x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))


def minim(a, b, c):
    return min(a, b, c)


print("Минимальное число: ", minim(x, y, z))
