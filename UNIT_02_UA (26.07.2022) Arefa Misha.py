
a = input("Введите предложение состоящее из двух слов: ")

b = a.split()[0]
c = a.split()[1]

d = (b + " " + c)[-1::-1]
h = b.upper() + " " + c.capitalize()
g = "!" + b + " " + c + "?"

source_file = open("python.txt", "w")

print(d, h, g, sep="<<<>>>", file=source_file)

source_file.close()
