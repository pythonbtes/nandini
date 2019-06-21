from tkinter import *



window=Tk()
window.title("simple calculator")
window.configure(background="#17A589")
window.geometry("370x150")
window.resizable(0,0)

expression=""

def display(num):
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method
    equation.set(expression) 

   
equation = StringVar() 

value = Entry(window,text=equation)
value.grid(columnspan=5,ipadx=120) 

button1=Button(window, text=' 1 ', height=1, width=10) 
button1.grid(row=2, column=0,command=display(1))
  
button2=Button(window, text=' 2 ', height=1, width=10) 
button2.grid(row=2, column=1,command=display(2)) 
  
button3 = Button(window, text=' 3 ', height=1, width=10) 
button3.grid(row=2, column=2) 

button4 = Button(window, text=' 4 ',height=1, width=10) 
button4.grid(row=3, column=0) 
  
button5 = Button(window, text=' 5 ', height=1, width=10) 
button5.grid(row=3, column=1) 

button6=Button(window, text= ' 6 ', height=1, width=10)
button6.grid(row=3,column=2)

button7=Button(window ,text= ' 7 ', height=1,width=10)
button7.grid(row=4,column=0)

button8=Button(window,text= ' 8 ',height=1,width=10)
button8.grid(row=4,column=1)

button9=Button(window ,text= ' 9 ', height=1,width=10)
button9.grid(row=4,column=2)

button0=Button(window,text= ' 0 ',height=1,width=10)
button0.grid(row=5,column=0)

button_clear=Button(window ,text= ' clear ', height=1,width=10)
button_clear.grid(row=5,column=1)

button_equal=Button(window,text= ' = ',height=1,width=10)
button_equal.grid(row=5,column=2)

button_plus=Button(window,text=" + ",height=1, width=10)
button_plus.grid(row=2,column=3)

button_minus=Button(window,text=" - ",height=1, width=10)
button_minus.grid(row=3,column=3)

button_divide=Button(window,text=" /",height=1, width=10)
button_divide.grid(row=4,column=3)

button_multiply=Button(window,text=" * ",height=1, width=10)
button_multiply.grid(row=5,column=3
                     )



window.mainloop()