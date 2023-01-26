
import openpyxl
import csv

with open("names.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
f.close()

for x in data:
    if x[0] == "age":
        data.remove(x)

wb = openpyxl.Workbook()
sheet = wb['Sheet']

for x in data:
    for y in x:
        cell = sheet.cell(row=int(data.index(x))+1, column=int(x.index(y))+1)
        cell.value = y

wb.save("Names1.xlsx")
