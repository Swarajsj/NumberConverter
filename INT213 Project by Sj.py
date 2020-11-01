#%%
# Final project Sj

from tkinter import*

root = Tk()
root.geometry("600x450")
root.resizable(0, 0)
root.configure(bg='#B0C4DE')


root.wm_title("Convertion by AK")
Base_Number = ""


def evaluate(event):

    if Base_Number == "Binary":
        try:
            dec = int(Myentry.get(), 2)
            myhex = hex(dec)
            myoct = oct(dec)
            re1.configure(text="Decimal is: "+str(dec))
            re2.configure(text="Hexadecimal is: "+str(myhex)[2:])
            re3.configure(text="Octal is: "+str(myoct)[2:])

        except ValueError:
            re1.configure(text="Please enter valid binary")
            re2.configure(text="")
            re3.configure(text="")

    elif Base_Number == "Octal":
        try:
            dec = int(Myentry.get(), 8)
            mybin = bin(dec)
            myhex = hex(dec)
            re1.configure(text="Binary is: "+str(mybin)[2:])
            re2.configure(text="Decimal is: "+str(dec))
            re3.configure(text="Hexadecimal is: "+str(myhex)[2:])
        except ValueError:
            re1.configure(text="Please enter valid decimal")
            re2.configure(text="")
            re3.configure(text="")

    elif Base_Number == "Decimal":
        try:
            dec = int(Myentry.get())
            mybin = bin(dec)
            myoct = oct(dec)
            myhex = hex(dec)
            re1.configure(text="Binary is: "+str(mybin)[2:])
            re2.configure(text="Octal is: "+str(myoct)[2:])
            re3.configure(text="Hexadecimal is: "+str(myhex)[2:])
        except ValueError:
            re1.configure(text="Please enter valid decimal")
            re2.configure(text="")
            re3.configure(text="")

    elif Base_Number == "Hexadecimal":
        try:
            dec = int(Myentry.get(), 16)
            mybin = bin(dec)
            myoct = oct(dec)
            re1.configure(text="Decimal is: "+str(dec))
            re2.configure(text="Binary is: "+str(mybin)[2:])
            re3.configure(text="Octal is: "+str(myoct)[2:])
        except ValueError:
            re1.configure(text="Please enter valid hexadecimal")
            re2.configure(text="")
            re3.configure(text="")
    else:
        re1.configure(text="Please select a BASE!")


def calcStyle():
    global Base_Number
    Base_Number = base.get()
    print(base.get())


Myentry = Entry(root, font=("Arial"))
#Myentry.bind("<Return>", evaluate)
Myentry.grid(row=0, column=1)
Myentry.place(x=215, y=195)

result1 = Label(root, text="Choose a Base", bg='#B0C4DE',
                fg='black', font=("Georgia", 18, "bold", "underline"))
result1.place(x=220, y=10)


result2 = Label(root, text="Enter a Number", bg='#B0C4DE',
                fg='black', font=("Georgia", 18, "bold", "underline"))
result2.place(x=205, y=155)


re1 = Label(root, font=("Georgia", 18), bg='#B0C4DE')
re1.place(x=120, y=300)

re2 = Label(root, font=("Georgia", 18), bg='#B0C4DE')
re2.place(x=120, y=342)

re3 = Label(root, font=("Georgia", 18), bg='#B0C4DE')
re3.place(x=120, y=383)

base = StringVar()
Radiobutton(root, text="Binary", font=15, variable=base, value="Binary",
            fg='#800000', bg='#B0C4DE', command=calcStyle).place(x=245, y=40)
Radiobutton(root, text="Decimal", font=15, variable=base, value="Decimal",
            fg='#800000', bg='#B0C4DE', command=calcStyle).place(x=245, y=65)
Radiobutton(root, text="Hexadecimal", font=15, variable=base, value="Hexadecimal",
            fg='#800000', bg='#B0C4DE', command=calcStyle).place(x=245, y=90)
Radiobutton(root, text="Octal", font=15, variable=base, value="Octal",
            fg='#800000', bg='#B0C4DE', command=calcStyle).place(x=245, y=115)


def result():

    f1 = Frame(root, height=3, width=600, bg="black")
    f1.place(y=275)

    f2 = Frame(root, height=180, width=50, bg="#800000")
    f2.place(y=278)

    f3 = Frame(root, height=2, width=450, bg="black")
    f3.place(x=100, y=295)

    f4 = Frame(root, height=2, width=450, bg="black")
    f4.place(x=100, y=422)

    f5 = Frame(root, height=2, width=450, bg="black")
    f5.place(x=100, y=337)

    f6 = Frame(root, height=2, width=450, bg="black")
    f6.place(x=100, y=379)

    f7 = Frame(root, height=129, width=2, bg="black")
    f7.place(x=100, y=295)

    f8 = Frame(root, height=129, width=2, bg="black")
    f8.place(x=550, y=295)

    l1 = Label(root, text="R", font=("Georgia", 14), fg='white', bg="#800000")
    l1.place(x=13, y=280)

    l2 = Label(root, text="E", font=("Georgia", 14), fg='white', bg="#800000")
    l2.place(x=13, y=308)

    l3 = Label(root, text="S", font=("Georgia", 14), fg='white', bg="#800000")
    l3.place(x=13, y=333)

    l4 = Label(root, text="U", font=("Georgia", 14), fg='white', bg="#800000")
    l4.place(x=12, y=358)

    l5 = Label(root, text="L", font=("Georgia", 14), fg='white', bg="#800000")
    l5.place(x=13, y=383)

    l6 = Label(root, text="T", font=("Georgia", 14), fg='white', bg="#800000")
    l6.place(x=13, y=408)


b1 = Button(text="RESULT", command=result)
b1.bind("<Button-1>", evaluate)
b1.place(x=271, y=230, width=70, height=30)


root.mainloop()
