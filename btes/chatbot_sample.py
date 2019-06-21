from tkinter import *
from PIL import Image
from PIL import ImageTk

def onclick1():
    name=textentry.get()
    Label(window,text="hello"+name).grid(row=4,column=80)
window=Tk()
window.title("this is my first chatbot")

imag=Image.open("robot.png")
imag=imag.resize((150,150),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(imag)


Label(window,image=photo1).grid(row=0,column=10)

Label(window,text="enter name",bg="black",fg="white").grid(row=1,column=0
                                                           )
textentry=Entry(window,width=30)
textentry.grid(row=1,column=10)

Label(window,text="enter password",bg="black",fg="white").grid(row=2,column=0)

textentry2=Entry(window,width=30)
textentry2.grid(row=2,column=10)

Button(window,text="click me",command=onclick1).grid(row=3,column=15)

window.mainloop()