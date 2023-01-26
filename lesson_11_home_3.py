# -*- coding: utf-8 -*-
#  Прочитать сохранённый csv-файл из задания №2
#  и сохранить данные в excel-файл,
#  кроме возраста – столбец с этими данными не нужен.
#  Высылаю пример как должно выглядеть содержания итогового файла.\


import openpyxl
import csv


with open("names.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
f.close()

for x in data:
    if x[0] == "age":
        data.remove(x)

print data

# with open("names.csv", encoding="utf-8") as f