
def func(val):
    ret = ""
    val = val.replace(",", ".")
    if not val.replace("-", "", 1).replace(".", "", 1).strip().isdigit():
        ret = "Вы ввели не корректное число: " + val
    else:
        if "-" in val:
            ret = "Вы ввели отрицательное "
        if "-" not in val:
            ret = "Вы ввели положительное "
        if "." not in val:
            ret += "целое число: "
        if "." in val:
            ret += "дробное число: "
        ret += val
    return ret


while True:
    value = input("Введите число либо значение для выхода: ")
    e = value.lower()
    if e == "выход" or e == "exit" or e == "quit" or e == "e" or e == "q":
        break
    else:
        print(func(value))
