# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на
# экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

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
        self.age += 1
