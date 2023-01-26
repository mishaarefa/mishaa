
import csv
import json

with open('names.json') as f:
    names = json.load(f)
f.close()

print(names)
column = [" "]
for x in range(1, len(names.values())+1):
    column.append("Person" + " " + str(x))


ids = ["id"]
name = ["name"]
age = ["age"]
phone = ["phone", "097-09-32", "096-92-85", "095-34-54", "094-93-85", "090-43-53"]

for x in names.keys():
    ids.append(str(x))

for x in list(names.values()):
    name.append(str(x[0]))

for x in list(names.values()):
    age.append(str(x[1]))


with open('names.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for x in (column, ids, name, phone, age):
        writer.writerow(x)
f.close()
