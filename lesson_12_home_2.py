# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Объекты класса truck имеют дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Объекты класса car имеют дополнительный обязательный атрибут max_speed и при
# вызове метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибума max_load. Создать по 2 объекта для каждого из
# классов truck и car, проверить все их методы и атрибуты.

import time


class Auto(object):
    brand = "Volkswagen"
    age = 7
    color = "Red"
    mark = "Volkswagen"
    weight = 2300

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        return print("move")

    def stop(self):
        return print("stop")

    def birthday(self):
        Auto.age += 1


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color, weight):
        super().__init__(self, brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color, weight):
        super().__init__(self, brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("Max speed is ", self.max_speed)
