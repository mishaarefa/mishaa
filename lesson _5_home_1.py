while True:
   a = input("Введите ваше имя: ")
   b = input("Введите ваш возраст: ")
   while not b.isdigit() or int(b) <= 0:
      print("Ошибка, повторите ввод")
      b = input("Введите ваш возраст: ")
   if ( 0 < int(b) <= 10 ):
      print("Привет, шкет ", a)
   elif ( 10 < int(b) <= 18 ):
      print("Как жизнь", a, "?")
   elif ( 18 < int(b) < 100 ):
      print("Что желаете ", a, "?")
   elif ( int(b) > 100 ):
      print(a, ",вы лжете - в наше время столько не живут...")
   k = input("Желаете выйти? (Д/Y):")
   if k.lower() == "y" or k.lower() == "д":
      break