

def func(val):
    ret = ""
    val = val.replace(",", ".")
    if not val.replace("-", "").replace(".", "").strip().isdigit():
        ret = "Вы ввели не корректное число: " + val
    else:
        if "-" in val:
            ret = "Вы ввели отрицательное "
        elif "-" not in val:
            ret = "Вы ввели положительное "
        if "." not in val:
            ret += "целое число: "
        elif "." in val:
            ret += "дробное число: "
        ret += val
    return ret


while True:
    value = input("Введите число либо значение для выхода: ")
    if value == "выход":
        break
    else:
        print(func(value))
