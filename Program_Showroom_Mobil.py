from ctypes import resize
from tkinter import *
from tkinter.messagebox import *
from tkinter.messagebox import showerror
from abc import ABC

class Showroom:
    model = None
    year = None
    color = None

class Lowprice(Showroom):

    def __init__(self,model):
        self.model = model

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

class Highprice(Showroom):

    def __init__(self,model):
        self.model = model

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

def on_click():
    number = entry.get()
    try:
       number = int(number)
    except ValueError:
        showerror('Error', 'Input Number')
    else:
        if number <= 80000000:
            showerror('Error', 'Set A Higher Price')
        elif 80000000 < number <= 300000000:
            hasil = Label(window, text= ((xenia.getModel())))
            hasil.place(x=145,y=180)
            hasil = Label(window, text= ((avanza.getModel())))
            hasil.place(x=145,y=250)
        elif 300000000 < number <= 500000000:
            hasil = Label(window, text= ((innova.getModel())))
            hasil.place(x=145,y=180)
            hasil = Label(window, text= ((crv.getModel())))
            hasil.place(x=145,y=250)
        elif 500000000 < number <= 800000000:
            hasil = Label(window, text= ((fortuner.getModel())))
            hasil.place(x=145,y=180)
            hasil = Label(window, text= ((pajero.getModel())))
            hasil.place(x=145,y=250)
        elif 800000000 < number <= 2000000000:
            hasil = Label(window, text= ((alphard.getModel())))
            hasil.place(x=145,y=180)
            hasil = Label(window, text= ((mercedescla.getModel())))
            hasil.place(x=145,y=250)
        else:
            showerror('Error', 'No Car Available')

xenia = Lowprice("Daihatsu Xenia                   ")
innova = Lowprice ("Toyota Innova                  ")
fortuner = Lowprice ("Toyota Fortuner              ") 
alphard = Lowprice ("Toyota Alphard                ")
 
avanza = Highprice("Toyota Avanza                  ") 
crv = Highprice("Honda CR-V                        ")
pajero = Highprice ("Mitsubishi Pajero             ") 
mercedescla = Highprice("Mercedes-Benz CLA         ") 

window = Tk()

logo = PhotoImage(file="car.png")
window.iconphoto(True,logo)

window.geometry("370x320")
window.title("Showroom GET-CAR")
window.resizable(width = 0, height = 0)

menu = Menu(window)
itemmenu = Menu(menu, tearoff=0)
itemoption = Menu(menu, tearoff=0)
itemhelp = Menu(menu, tearoff=0)
itemmenu.add_command(label = 'More Info')
itemmenu.add_command(label = 'Database')
itemoption.add_command(label = 'Setting')
itemhelp.add_command(label = 'Contact : getyourcar@gmail.com')
menu.add_cascade(label='Menu', menu=itemmenu)
menu.add_cascade(label='Option', menu=itemoption)
menu.add_cascade(label='Help', menu=itemhelp)
window.config(menu=menu)


labeljudul = Label(window, 
                    text = "Showroom GET-CAR",
                    font = ("times new roman", 12))
labeljudul.pack(pady=20)   

labelText1 = Label(window, 
                    text = "  Price\t:",
                    font = ("times new roman", 12))
labelText1.place(x=60,y=65)   

labelText2 = Label(window, 
                    text = "Car 1  :",
                    font = ("times new roman", 12))
labelText2.place(x=160,y=150)   

labelText3 = Label(window, 
                    text = "Car 2 :",
                    font = ("times new roman", 12))
labelText3.place(x=160,y=220)   

entry = Entry(window)
entry.pack(pady=5)
btn = Button(window, text = "Search", command = on_click)
btn.place(x=260,y=65)


window.mainloop()

#modul 1 : variabel dan tipe data
#modul 2 : pengkondisian (if,elif,else)
#modul 4 : function (def)
#modul 5 : OOP (class & inheritance)
#modul 6 : setter and getter
#modul 8 : GUI