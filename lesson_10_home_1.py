
string = b'r\xc3\xa9sum\xc3\xa9'

new_string = string.decode()
print(new_string)
new_string = new_string.encode('latin1')
print(new_string)
new_string = new_string.decode('latin1')
print(new_string)
