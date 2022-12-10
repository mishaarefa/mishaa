# Написать декоратор к 2-м любым функциям,
# который бы считал и выводил время их выполнения
# now = datetime.now()


from datetime import datetime


def decorator(x_function):
    def x():
        print("Время выполнения:")
        b = datetime.now()
        x_function()
        print(datetime.now() - b)
    return x

@decorator
def plus():
    a = (1 + 5 + 8 + 9 + 10)**100


@decorator
def minus():
    a = (1 - 5 - 8 - 9 - 10)**100


plus()
minus()
