
a = (3,)
b = (3,)
c = (3,)

print(id(a))
print(id(b))
print(id(c))

d = [1]
e = [1]

print(id(d))
print(id(e))

a = list(a)
b = list(b)
c = list(c)

print(id(a))
print(id(b))
print(id(c))

d = tuple(d)
e = tuple(e)

print(id(d))
print(id(e))
