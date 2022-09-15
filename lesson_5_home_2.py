
n = input("(Цикл for)Введите целое число: ")

while not n.isdigit():
   print("Вы ввели не целое число")
   n = input("Введите целое число: ")

n = int(n)

for i in range(1, n+1):
   if i % 3 == 0:
      i = 0
   else:
      print(i**2)

n = input("(Цикл While)Введите целое число: ")

while not n.isdigit():
   print("Вы ввели не целое число")
   n = input("Введите целое число: ")

n = int(n)
k = 1

while k in range(1, n+1):
   if not k % 3 == 0:
      print(k**2)
   k = k + 1