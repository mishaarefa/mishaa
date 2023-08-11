# Написать класс Car в котором есть 3 атрибута класса:
# - FUEL_TYPES (список) в котором находится перечень доступных значений
# типов авто, например: ['бензин', 'дизель', 'электричество', 'гибрид']
# - COLORS (пустой список) - в котором хранятся все уникальные значения
# цветов созданных по этому классу объектов
# - NUMBER_OF_CARS - кол-во созданных объектов.
#
# Конструктор принимает 4 обязательных аргумента: model, year, color, fuel_type.
# Первые 3-и аргумента присваиваются 3-м атрибутам объекта. В атрибут fuel_type
# объекта присваивается результат статического метода is_valid_fuel_type в
# который передаётся аргумент fuel_type и атрибут класса FUEL_TYPES. Данный
# метод проверяет, находится ли значение fuel_type в список FUEL_TYPES. Если
# входит, то это значение возвращается статическим методом is_valid_fuel_type,
# если нет, то возвращается первое значение списка FUEL_TYPES.
# Так же в конструкторе необходимо увеличить атрибут класса NUMBER_OF_CARS на
# единицу, а так же внести в атрибут класса COLORS аргумент color, если такое
# значение в атрибуте класса COLORS отсутствует. Кроме этого у объекта должен
# появиться атрибут number, в который будет записано значение какой по счёту
# этот объект был произведён (грубо говоря значение NUMBER_OF_CARS на момент
# создания объекта).
#
# Так же необходимо предусмотреть, чтобы при печати объекта распечатывалось
# бы: "модель год_выпуска тип_двигателя цвет" .
#
# У класса должен быть метод numbers который бы вёл себя как атрибут. При
# его вызове car.numbers должно выдаваться, например: "2 from 4". То есть
# это второй автомобиль из 4-х произведённых.
#
# Кроме этого в классе должны быть ещё 2 метода класса get_used_colors и
# get_number_of_cars. Первый из которых возвращает количество уникальных
# цветов произведённых автомобилей, грубо говоря длину списка COLORS.
# Второй же метод возвращает количество всего произведённых автомобилей.
#
#
# class Car:
# FUEL_TYPES = ['бензин', 'дизель', 'электричество', 'гибрид']
# COLORS = []
# NUMBER_OF_CARS = 0
#
# ...
#
#
# car_1 = Car('Zaz', 1979, 'дизель', 'black')
# car_2 = Car('BMW', 2000, 'бензин', 'red')
# car_3 = Car('VOLVO', 2012, 'электричествоcccc', 'black')
# car_4 = Car('Mersedes', 2012, 'гибрид', 'black')
#
# print('COLORS:', Car.get_used_colors())
# print('NUMBER_OF_CARS:', Car.get_number_of_cars())
# for item in (car_1, car_2, car_3, car_4):
# print('item:', item)
# print('numbers:', item.numb


class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'электричество', 'гибрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        if fuel_type in Car.FUEL_TYPES:
            return fuel_type
        else:
            return Car.FUEL_TYPES[0]

    def __init__(self, model, year, color, fuel_type):
        Car.NUMBER_OF_CARS += 1
        self.model = model
        self.year = year
        self.color = color
        if color not in Car.COLORS:
            Car.COLORS.append(color)
        self.fuel_type = Car.is_valid_fuel_type(fuel_type)
        self.number = Car.NUMBER_OF_CARS

    def __str__(self):
        return f'{self.model}, {self.year}, {self.fuel_type}, {self.color}'

    @property
    def numbers(self):
        return f'{self.number} from {Car.NUMBER_OF_CARS}'

    @staticmethod
    def get_used_colors():
        a = 0
        for i in Car.COLORS:
            a += 1
        return a

    @staticmethod
    def get_number_of_cars():
        return Car.NUMBER_OF_CARS


car_1 = Car('Zaz', 1979, 'black', 'дизель')
car_2 = Car('BMW', 2000, 'red', 'бензин')
car_3 = Car('VOLVO', 2012, 'black', 'электричествоcccc')
car_4 = Car('Mersedes', 2012, 'black', 'гибрид')

print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())
for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
