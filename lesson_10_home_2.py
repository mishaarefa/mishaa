
variable1 = input("Введите строку 1: ")
variable2 = input("Введите строку 2: ")
variable3 = input("Введите строку 3: ")
variable4 = input("Введите строку 4: ")

f = open("text123.txt", "w")
f.write(variable1)
f.write("\n")
f.write(variable2)
f.close()

f = open("text123.txt", "a")
f.write("\n")
f.write(variable3)
f.write("\n")
f.write(variable4)
f.close()
