import tkinter as tk
window=tk.Tk()
window.geometry("400x250")
window.resizable(0,0)
window.configure(background="blue")

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
def red():
    if var1.get()==1:
        window.configure(background="red")
    elif var2.get()==1:
        window.configure(background="green")
    elif var3.get()==1:
        window.configure(background="pink")
    else:
        window.configure(background="blue")
check1=tk.Checkbutton(window,text="red",width=10,command=red,variable=var1)
check1.grid(row=1,column=1)

check2=tk.Checkbutton(window,text="green",width=10,command=red,variable=var2)
check2.grid(row=2,column=1)

check3=tk.Checkbutton(window,text="pink",width=10,command=red,variable=var3)
check3.grid(row=3,column=1)
window.mainloop()