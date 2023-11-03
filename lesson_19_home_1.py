
import tkinter

window = tkinter.Tk()
window.title("Введите домашний адресс")

frame_1 = tkinter.Frame()
frame_2 = tkinter.Frame()
frame_3 = tkinter.Frame()
frame_4 = tkinter.Frame()
frame_5 = tkinter.Frame()
frame_6 = tkinter.Frame()
frame_7 = tkinter.Frame()
frame_8 = tkinter.Frame()
frame_9 = tkinter.Frame()

ent_name = tkinter.Entry(master=frame_1, width=20)
lbl_name = tkinter.Label(master=frame_1, text="Имя:")
ent_name.pack(side=tkinter.RIGHT)
lbl_name.pack()
frame_1.pack()

ent_surname = tkinter.Entry(master=frame_8, width=20)
lbl_surname = tkinter.Label(master=frame_8, text="Фамилия:")
ent_surname.pack(side=tkinter.RIGHT)
lbl_surname.pack()
frame_8.pack()

ent_address1 = tkinter.Entry(master=frame_2, width=20)
lbl_address1 = tkinter.Label(master=frame_2, text="Адрес 1:")
ent_address1.pack(side=tkinter.RIGHT)
lbl_address1.pack()
frame_2.pack()

ent_address2 = tkinter.Entry(master=frame_3, width=20)
lbl_address2 = tkinter.Label(master=frame_3, text="Адрес 2:")
ent_address2.pack(side=tkinter.RIGHT)
lbl_address2.pack()
frame_3.pack()

ent_city = tkinter.Entry(master=frame_4, width=20)
lbl_city = tkinter.Label(master=frame_4, text="Город:")
ent_city.pack(side=tkinter.RIGHT)
lbl_city.pack()
frame_4.pack()

ent_reg = tkinter.Entry(master=frame_5, width=20)
lbl_reg = tkinter.Label(master=frame_5, text="Регион:")
ent_reg.pack(side=tkinter.RIGHT)
lbl_reg.pack()
frame_5.pack()

ent_index = tkinter.Entry(master=frame_6, width=20)
lbl_index = tkinter.Label(master=frame_6, text="Почтовый индекс:")
ent_index.pack(side=tkinter.RIGHT)
lbl_index.pack()
frame_6.pack()

ent_country = tkinter.Entry(master=frame_7, width=20)
lbl_country = tkinter.Label(master=frame_7, text="Страна:")
ent_country.pack(side=tkinter.RIGHT)
lbl_country.pack()
frame_7.pack()

info = open("info.json", "w")


def send_command():
    if (ent_name.get() == ""
            or ent_surname.get() == ""
            or ent_address1.get() == ""
            or ent_city.get() == ""
            or ent_reg.get() == ""
            or ent_index.get() == ""
            or ent_country.get() == ""):
        window.title(string="Не все поля заполнены!")
    else:
        info_list = [" Name:", ent_name.get(),
                     " Surname: ", ent_surname.get(),
                     " Address1: ", ent_address1.get(),
                     " Address2:", ent_address2.get(),
                     " City:", ent_city.get(),
                     " Region:", ent_reg.get(),
                     " Index:", ent_index.get(),
                     " Country:", ent_country.get()]
        for i in info_list:
            info.write(str(i))
        window.title(string=ent_name.get()+", Ваши данные успешно отправлены")


button_send = tkinter.Button(master=frame_9, text="Отправить", command=send_command)
button_clear = tkinter.Button(master=frame_9, text="Очистить")
button_clear.pack(side=tkinter.LEFT)
button_send.pack(side=tkinter.RIGHT)
frame_9.pack()

window.mainloop()
