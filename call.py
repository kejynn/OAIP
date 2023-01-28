t = int(input("Время начала разговора (час)"))
tm = int(input("Время начала разговора (минута)"))
dt = int(input("Время разговора в минутах"))
s = int(input("Стоимость минуты разговора"))
d = int(input("День недели (от 1 до 7)"))
stf = 0

for i in range(dt):
    if 7 < t < 22 and d < 6:
        st = s
    elif 7 < t < 22 and d >= 6:
        st = s
        st = st - st * 0.1
    elif (22 <= t <= 23 or 0 <= t <= 7) and d < 6:
        st = s
        st = st - st * 0.2
    elif (22 <= t <= 23 or 0 <= t <= 7) and d >= 6:
        st = s
        st = st - st * 0.2
        st = st - st * 0.1

    tm = tm + 1
    if tm == 60:
        t = t + 1
    else:
        t = t

    stf = stf + st

print("Стоимость", dt, "минут разговора - ", stf)