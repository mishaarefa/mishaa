
import tkinter

window = tkinter.Tk()
window.title("Введите домашний адресс")
window.columnconfigure(1)
window.geometry("400x200")

frame_1 = tkinter.Frame()   # label
frame_2 = tkinter.Frame()   # enter
frame_3 = tkinter.Frame()   # button

ent_name = tkinter.Entry(master=frame_2)
lbl_name = tkinter.Label(master=frame_1, text="Имя:")
ent_name.pack(anchor="w")
lbl_name.pack(anchor="e")

ent_surname = tkinter.Entry(master=frame_2)
lbl_surname = tkinter.Label(master=frame_1, text="Фамилия:")
ent_surname.pack(anchor="w")
lbl_surname.pack(anchor="e")

ent_address1 = tkinter.Entry(master=frame_2)
lbl_address1 = tkinter.Label(master=frame_1, text="Адрес 1:")
ent_address1.pack(anchor="w")
lbl_address1.pack(anchor="e")

ent_address2 = tkinter.Entry(master=frame_2)
lbl_address2 = tkinter.Label(master=frame_1, text="Адрес 2:")
ent_address2.pack(anchor="w")
lbl_address2.pack(anchor="e")

ent_city = tkinter.Entry(master=frame_2)
lbl_city = tkinter.Label(master=frame_1, text="Город:")
ent_city.pack(anchor="w")
lbl_city.pack(anchor="e")

ent_reg = tkinter.Entry(master=frame_2)
lbl_reg = tkinter.Label(master=frame_1, text="Регион:")
ent_reg.pack(anchor="w")
lbl_reg.pack(anchor="e")

ent_index = tkinter.Entry(master=frame_2)
lbl_index = tkinter.Label(master=frame_1, text="Почтовый индекс:")
ent_index.pack(anchor="w")
lbl_index.pack(anchor="e")

ent_country = tkinter.Entry(master=frame_2)
lbl_country = tkinter.Label(master=frame_1, text="Страна:")
ent_country.pack(anchor="w")
lbl_country.pack(anchor="e")

frame_3.pack(expand=True, side=tkinter.BOTTOM)  # button
frame_1.pack(side=tkinter.LEFT)  # label
frame_2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)  # enter

send_list = [ent_name, lbl_name, ent_surname, lbl_surname,
             ent_address1, lbl_address1, ent_city, lbl_city,
             ent_reg, lbl_reg, ent_index, lbl_index,
             ent_country, lbl_country]


def send_command():
    a_true = True
    for i in send_list:
        if (send_list.index(i)+1) % 2 != 0:
            if i.get() == "":
                send_list[(send_list.index(i)+1)]["fg"] = "red"
                window.title(string="Не все поля заполнены!")
                a_true = False
            else:
                send_list[(send_list.index(i) + 1)]["fg"] = "black"
    if a_true:
        info = open("info.json", "w")
        info_list = [" Name:", ent_name.get(),
                     " Surname: ", ent_surname.get(),
                     " Address1: ", ent_address1.get(),
                     " Address2:", ent_address2.get(),
                     " City:", ent_city.get(),
                     " Region:", ent_reg.get(),
                     " Index:", ent_index.get(),
                     " Country:", ent_country.get()]
        for b in info_list:
            info.write(str(b))
        window.title(string=ent_name.get() + ", Ваши данные успешно отправлены")


button_send = tkinter.Button(master=frame_3, text="Отправить", command=send_command)
button_clear = tkinter.Button(master=frame_3, text="Очистить")
button_clear.pack(side=tkinter.LEFT)
button_send.pack(side=tkinter.RIGHT)

window.mainloop()
