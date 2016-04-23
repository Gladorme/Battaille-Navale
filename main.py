from tkinter import *

fen = Tk()
fen.title("Bataille Navale")


#-----------------------#
# Début: MENU D'ACCUEIL #
#-----------------------#
fen.geometry("950x535")
background_img = PhotoImage(file="background.gif")
can_menu = Canvas(fen, bg="white", width=950, heigh=535)
can_menu.place(x=0,y=0)
can_menu.create_image(473,267, image=background_img)

jouer_button = Button(fen, text="Jouer !", command=jouer, cursor="pirate", width=10)
scores_button = Button(fen, text="Scores", cursor="pirate", width=10)
info_label = Label(fen, text="Informations: \nIl y aura deux tableaux, le premier (celui de gauche)\n vous permettera de placer vos navires et voir où l'adversaire a tiré,\n vos navires ont la couleur blanche et les tirs violets.\n Le second tableau vous permet de voir vos tirs sur l'adversaire,\n si le tirs a touché un vaisseau ennemi la case sera rouge sinon elle sera jaune")

jouer_button.place(x=70,y=120)
scores_button.place(x=70,y=320)
info_label.place(x=500,y=100)
#-----------------------#
# Fin: MENU D'ACCUEIL   #
#-----------------------#
#-----------------------#
# Début: Fonctions      #
#-----------------------#
def jouer():
    can_menu.config(width=0, heigh=0)
    jouer_button.destroy()
    scores_button.destroy()
    info_label.destroy()
    fen.geometry("1300x800")
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
	
	##Indication et placement des indications
    label1x = Label(fen,text="  A     B     C     D     E     F    G     H     I      J", font=("Helvetica", 18))
    label1x.place(x=100,y=110)
    label1y1 = Label(fen,text="1",font=("Helvetica", 18))
    label1y2 = Label(fen,text="2",font=("Helvetica", 18))
    label1y3 = Label(fen,text="3",font=("Helvetica", 18))
    label1y4 = Label(fen,text="4",font=("Helvetica", 18))
    label1y5 = Label(fen,text="5",font=("Helvetica", 18))
    label1y6 = Label(fen,text="6",font=("Helvetica", 18))
    label1y7 = Label(fen,text="7",font=("Helvetica", 18))
    label1y8 = Label(fen,text="8",font=("Helvetica", 18))
    label1y9 = Label(fen,text="9",font=("Helvetica", 18))
    label1y10 = Label(fen,text="10",font=("Helvetica", 18))
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
	
	
	
	
	##Indication et placement des indications
    label2x = Label(fen,text="  A     B     C     D     E     F    G     H     I      J", font=("Helvetica", 18))
    label2x.place(x=700,y=110) 
    label2y1 = Label(fen,text="1",font=("Helvetica", 18))
    label2y2 = Label(fen,text="2",font=("Helvetica", 18))
    label2y3 = Label(fen,text="3",font=("Helvetica", 18))
    label2y4 = Label(fen,text="4",font=("Helvetica", 18))
    label2y5 = Label(fen,text="5",font=("Helvetica", 18))
    label2y6 = Label(fen,text="6",font=("Helvetica", 18))
    label2y7 = Label(fen,text="7",font=("Helvetica", 18))
    label2y8 = Label(fen,text="8",font=("Helvetica", 18))
    label2y9 = Label(fen,text="9",font=("Helvetica", 18))
    label2y10 = Label(fen,text="10",font=("Helvetica", 18))
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
#-----------------------#
# Fin: Fonctions        #
#-----------------------#
fen.mainloop()