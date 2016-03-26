from tkinter import *
import solo

fen = Tk()
fen.geometry("950x534")
fen.title("Menu - Bataille Navale")




#Definitions
def Solo():
    info_label.place(x=500,y=100)
    info_label.config(text="Informations: \nIl y aura deux tableaux, le premier (celui de gauche)\n vous permettera de placer vos navires et voir où l'adversaire a tiré,\n vos navires ont la couleur blanche et les tirs violets.\n Le second tableau vous permet de voir vos tirs sur l'adversaire,\n si le tirs a touché un vaisseau ennemi la case sera rouge sinon elle sera jaune")
    bouton_jouer = Button (fen, text="JOUER !", font=("Impact",50), command = solo.jouer(), bg = "#045FB4" )
    bouton_jouer.place(x=550, y=200)
	
def Multi():
    info_label.place(x=500,y=100)
    info_label.config(text="Multi")
	
def Leader():
    info_label.place(x=500,y=100)
    info_label.config(text="Leaderboard")

	
#Fond du menu
background_img = PhotoImage(file="background.gif")
can = Canvas(fen, bg="white", width=950, heigh=534,)
can.place(x=0,y=0)
can.create_image(473,267, image=background_img)


#Elements présents dans le menu
solo_button = Button(fen, text="Solo", command=Solo, cursor="pirate", width=10)
multi_button = Button(fen, text="Multijoueurs", command=Multi, cursor="pirate", width=10)
leaderboard_button = Button(fen, text="Leaderboard", command=Leader, cursor="pirate", width=10)
info_label = Label(fen, text="")

solo_button.place(x=70,y=120)
multi_button.place(x=70,y=220)
leaderboard_button.place(x=70,y=320)




#Lancement de la fenêtre
fen.mainloop()