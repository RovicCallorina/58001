from tkinter import *

class myName:
    def __init__(self, name):
        self.lbl5 = Label(name, text="My Full Name")
        self.lbl5.place(x=200, y=15)

        self.lbl1 = Label(name, text="Enter Given Name:")
        self.lbl1.place(x=100, y=60)
        self.lbl2 = Label(name, text="Enter Middle Name:")
        self.lbl2.place(x=100, y=90)
        self.lbl3 = Label(name, text="Enter Last Name:")
        self.lbl3.place(x=100, y=120)
        self.lbl4 = Label(name, text="My Full Name is:")
        self.lbl4.place(x=100, y=170)

        self.txt1 = Entry(name, bd=1)
        self.txt1.place(x=250, y=60)
        self.txt2 = Entry(name, bd=1)
        self.txt2.place(x=250, y=90)
        self.txt3 = Entry(name, bd=1)
        self.txt3.place(x=250, y=120)
        self.txt4 = Entry(name, bd=1)
        self.txt4.place(x=250, y=170, width= 200)

        self.btnGivenName = Button(name, text="Show Full Name")
        self.btnGivenName.place(x=190, y=200)
        self.btnGivenName.bind('<Button-1>', self.fullname)

    def fullname(self, name):
        GivenName = self.txt1.get()
        MiddleName = self.txt2.get()
        LastName = self.txt3.get()
        result = GivenName +" " + MiddleName + " " + LastName
        self.txt4.insert(END, result)


window = Tk()
mywin = myName(window) # changed to myName
window.geometry("600x400")
window.title("Midterm Exam Problem 2")
window.mainloop()