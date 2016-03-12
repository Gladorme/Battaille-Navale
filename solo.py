# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:32:59 2016

@author: ladorme
"""

from tkinter import *
fen = Tk()
fen.geometry("800x800")
fen.title("Solo")

#Réglages:
d=35
colonne=10

#Partie 1:
can1 = Canvas(fen, width= colonne*d, height= colonne*d)
can1.pack()
tuile = []
val = []
for n in range(100):
    x = (n%10)*d
    y = (n//10)*d
    tuile = tuile + [can1.create_rectangle(x,y,x+d,y+d)]
    can1.itemconfig(tuile[n], fill="orange")
    val = val + [can1.create_text(x+d//2, y+d//2)]
    can1.itemconfig(val[n], text = n)

#Partie 2:
can2 = Canvas(fen, width= colonne*d, height= colonne*d)
can2.pack()
tuile = []
val = []
for n in range(100):
    x = (n%10)*d
    y = (n//10)*d
    tuile = tuile + [can2.create_rectangle(x,y,x+d,y+d)]
    can2.itemconfig(tuile[n], fill="brown")
    val = val + [can2.create_text(x+d//2, y+d//2)]
    can2.itemconfig(val[n], text = n)
    
fen.mainloop()
