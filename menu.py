from tkinter import *
fen = Tk()
fen.geometry("950x534")
fen.title("Menu - Bataille Navale")

#Definitions
def solo():
    info_label.config(text="Informations: \nIl y aura deux tableaux, le premier (celui de gauche)\n vous permettera de placer vos navires et voir où l'adversaire à tirer,\n vos navires ont la couleur blanche et les tirs violets.\n Le second tableau vous permet de voir vos tirs sur l'adversaire,\n si le tirs a touché un bâtiments ennemis la case sera rouge sinon elle sera jaune")
def multi():
    info_label.config(text="Multi")
def leader():
    info_label.config(text="Leaderboard")



#Fond du menu
background_img = PhotoImage(file="background.gif")
can = Canvas(fen, bg="white", width=950, heigh=534,)
can.place(x=0,y=0)
can.create_image(473,267, image=background_img)

#Elements présents dans le menu
solo_button = Button(fen, text="Solo", command=solo)
multi_button = Button(fen, text="Multi", command=multi)
leaderboard_button = Button(fen, text="Leaderboard", command=leader)
info_label = Label(fen, text="")

solo_button.place(x=150,y=100)
multi_button.place(x=150,y=200)
leaderboard_button.place(x=130,y=300)
info_label.place(x=500,y=100)






fen.mainloop()