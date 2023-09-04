time = int(input())

if time >= 5 and time <= 10:
    print("Утро")
elif time >= 11 and time <= 17:
    print("День")
elif time >= 18 and time <=22:
    print("Вечер")
elif time >= 0 and time <= 4:
    print("Ночь")
else:
    print("ошибка")