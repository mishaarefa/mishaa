# Сделать программу в виде функций в которой нужно будет угадывать число.

import random

def guess(namber):
    while True:
        namber = input("Угадайте число от 1 до 5: ")
        if namber.isdigit() and (1 <= namber <= 5):
            break
        else:
            print("Неправильное число")
    return(int(namber))

while True:
    a = random.randint(1, 5)
    if a == guess():
        print("Вы угадали число")
        break
    else:
        print("Вы не угадали число")
