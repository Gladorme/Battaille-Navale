from tkinter import *
fen = Tk()
fen.geometry("1400x800")
fen.title("Solo")

#Réglages:
d=50
colonne=10

#Partie 1:
can1 = Canvas(fen, width= colonne*d, height= colonne*d)
can1.place(x=100,y=150)
tuile1 = []
val1 = []
for n in range(100):
    x = (n%10)*d
    y = (n//10)*d
    tuile1 = tuile1 + [can1.create_rectangle(x,y,x+d,y+d)]
    can1.itemconfig(tuile1[n], fill="orange")
    val1 = val1 + [can1.create_text(x+d//2, y+d//2)]
    can1.itemconfig(val1[n], text = n)
##Indication et palacement des indications
label1x = Label(text="  A     B     C     D     E     F    G     H     I      J", font=("Helvetica", 18))
label1x.place(x=100,y=110)
label1y1 = Label(text="1",font=("Helvetica", 18))
label1y2 = Label(text="2",font=("Helvetica", 18))
label1y3 = Label(text="3",font=("Helvetica", 18))
label1y4 = Label(text="4",font=("Helvetica", 18))
label1y5 = Label(text="5",font=("Helvetica", 18))
label1y6 = Label(text="6",font=("Helvetica", 18))
label1y7 = Label(text="7",font=("Helvetica", 18))
label1y8 = Label(text="8",font=("Helvetica", 18))
label1y9 = Label(text="9",font=("Helvetica", 18))
label1y10 = Label(text="10",font=("Helvetica", 18))
label1y1.place(x=70,y=160)
label1y2.place(x=70,y=210)
label1y3.place(x=70,y=260)
label1y4.place(x=70,y=310)
label1y5.place(x=70,y=360)
label1y6.place(x=70,y=410)
label1y7.place(x=70,y=460)
label1y8.place(x=70,y=510)
label1y9.place(x=70,y=560)
label1y10.place(x=60,y=610)


#Partie 2:
can2 = Canvas(fen, width= colonne*d, height= colonne*d)
can2.place(x=700,y=150)
tuile2 = []
val2 = []
for n in range(100):
    x = (n%10)*d
    y = (n//10)*d
    tuile2 = tuile2 + [can2.create_rectangle(x,y,x+d,y+d)]
    can2.itemconfig(tuile2[n], fill="brown")
    val2 = val2 + [can2.create_text(x+d//2, y+d//2)]
    can2.itemconfig(val2[n], text = n)

##Indication et palacement des indications
label2x = Label(text="  A     B     C     D     E     F    G     H     I      J", font=("Helvetica", 18))
label2x.place(x=700,y=110) 
label2y1 = Label(text="1",font=("Helvetica", 18))
label2y2 = Label(text="2",font=("Helvetica", 18))
label2y3 = Label(text="3",font=("Helvetica", 18))
label2y4 = Label(text="4",font=("Helvetica", 18))
label2y5 = Label(text="5",font=("Helvetica", 18))
label2y6 = Label(text="6",font=("Helvetica", 18))
label2y7 = Label(text="7",font=("Helvetica", 18))
label2y8 = Label(text="8",font=("Helvetica", 18))
label2y9 = Label(text="9",font=("Helvetica", 18))
label2y10 = Label(text="10",font=("Helvetica", 18))
label2y1.place(x=670,y=160)
label2y2.place(x=670,y=210)
label2y3.place(x=670,y=260)
label2y4.place(x=670,y=310)
label2y5.place(x=670,y=360)
label2y6.place(x=670,y=410)
label2y7.place(x=670,y=460)
label2y8.place(x=670,y=510)
label2y9.place(x=670,y=560)
label2y10.place(x=660,y=610)

    
fen.mainloop()