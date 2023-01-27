
import random
import csv
import json

with open('names.json') as f:
    names = json.load(f)
f.close()

column = ["id", "name", "age", "phone"]
persons = []

for x, y in enumerate(names):
    persons.append([y])
    for z in names.get(y):
        persons[x].append(z)

operators = ["039", "067", "068", "096", "097", "098"]

list1 = []
for x in range(0, 10):
    list1.append(x)

for x in range(len(persons)):
    r = "+38" + random.choice(operators)
    for y in range(7):
        r += str(random.choice(list1))
    persons[x].append(r)

with open('names.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(column)
    for x in persons:
        writer.writerow(x)
f.close()
