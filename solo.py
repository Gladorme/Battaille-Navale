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
tuile1 = []
val1 = []
for n in range(100):
    x = (n%10)*d
    y = (n//10)*d
    tuile1 = tuile + [can1.create_rectangle(x,y,x+d,y+d)]
    can1.itemconfig(tuile1[n], fill="orange")
    val1 = val1 + [can1.create_text(x+d//2, y+d//2)]
    can1.itemconfig(val1[n], text = n)

#Partie 2:
can2 = Canvas(fen, width= colonne*d, height= colonne*d)
can2.pack()
tuile2 = []
val2 = []
for n in range(100):
    x = (n%10)*d
    y = (n//10)*d
    tuile2 = tuile2 + [can2.create_rectangle(x,y,x+d,y+d)]
    can2.itemconfig(tuile2[n], fill="brown")
    val2 = val2 + [can2.create_text(x+d//2, y+d//2)]
    can2.itemconfig(val2[n], text = n)
    
fen.mainloop()
