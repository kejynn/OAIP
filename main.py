x = float(input("Введите координату x "))
y = float(input("Введите координату y "))

pol = abs(x) + abs(y)

if pol < 1:
    print("Точка вне зоны")
else:
    print("Точка в зоне")