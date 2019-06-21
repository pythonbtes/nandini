'''
Created on 21-Jun-2019

@author: naina

from tkinter import *
root=Tk()
def click():
    Label(root,text=but1.cget('text')).pack()
i=0
while i<10:
    but1=Button(root,text=i,command=click)
    but1.pack()
    i=i+1'''
import random,re
'''print(random.randint(0,5))
print(random.random()*1)

print(random.choice(range(2,24)))'''
try:
    r=re.search('ab', 'seshab')
except:
    print("string not found")
print(r.group())