
while True:
    n = input("Введите целое число: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Вы ввели не целое число")

cycle = input("Выберите цикл For(f)/While(w): ")

while True:
    cycle = cycle.lower()
    if cycle == "f" or cycle == "w":
        break
    else:
        cycle = input("Выберите цикл For(f)/While(w): ")

listt = [0]
k = 1

if cycle == "w":
    while k in range(1, n + 1):
        if not k % 3 == 0:
            listt.append(k**3)
        k = k + 1
    print(sum(listt))

if cycle == "f":
    for k in range(1, n + 1):
        if not k % 3 == 0:
            listt.append(k ** 3)
    print(sum(listt))
