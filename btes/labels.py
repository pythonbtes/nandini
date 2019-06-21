'''
Created on 19-Jun-2019

@author: naina
'''
from tkinter import *
window=Tk()
for i in range(1,6):
    label="label"+str(i)
    label=Label(text="label"+str(i))
    label.grid(row=i,column=1) 
window.mainloop()