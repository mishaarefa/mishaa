
import openpyxl
import csv

with open("names.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
f.close()

for x, y in enumerate(data):
    data[x].pop(2)
data.pop(0)

tele = ["phone"]
ids = ["id"]
names = ["name"]
person = [" "]

for m in range(len(data)):
    person.append("Person"+" "+str(m+1))

for x in data:
    if len(x) == 2:
        tele.append("")
    for y in x:
        y.rstrip()
        if y.startswith("+380"):
            tele.append(y)
        elif y.isdigit():
            ids.append(y)
        else:
            names.append(y)

wb = openpyxl.Workbook()
sheet = wb["Sheet"]

for x, y in enumerate((person, ids, names, tele)):
    for z, a in enumerate(y):
        cell = sheet.cell(row=x+1, column=z+1)
        cell.value = a

wb.save("Names1.xlsx")
