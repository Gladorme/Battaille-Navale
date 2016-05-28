#-----------------------#
# Début: Dépendances    #
#-----------------------#
from tkinter import *
from random import randint
import sys
sys.setrecursionlimit(10000)
#-----------------------#
# Fin: Dépendances      #
#-----------------------#

#-----------------------#
# Début: Variables      #
#-----------------------#
#Une partie des variables, généralement celle qui sont globale nécessaire d'être crée avant leur utilisation dans les fonctions
fen = Tk() #Varible qui raccourcit "Tk()"
cases_occupées_bot=[] #Liste des cases où les navires du bots sont placés
cases_tirées_bot=[] #Liste des cases où les tirs du bot ont déjà étés effectués
cases_occupées_joueur=[] #Liste des cases où les navires du joueur sont placés
cases_tirées_joueur=[] #Liste des cases où les tirs du joueur ont déjà étés effectués
état = "initial" #état de base du jeu à son lancement
fen_map = Canvas(fen, bg="white", width=1300, height=800) #Canvas de l'interface du jeu
label_info = Label(fen_map, text="Informations:") #Label situé sous les plateforme, il donne des informations
label_info_desc = Label(fen_map, text="Placement du bot") #Label situé sous les plateforme, il donne des informations
bateaux_bot = [] #Liste calquée sur cases_occupées_bot, utilisé dans la fonction "check()" permettant de savoir quand le jeu est terminé, si la liste est vide, le joueur a gagné
bateaux_joueur = [] #Liste calquée sur cases_occupées_joueur, utilisé dans la fonction "check()" permettant de savoir quand le jeu est terminé, si la liste est vide, le bot a gagné
b=0  #Variable qui permet de savoir quel navire est en cours de placement, utilisé dans la fonction "placement()"
background_img = PhotoImage(file="background.gif") #Image
map_jeu=PhotoImage(file="Fondmap.gif") #Image
map_victoire=PhotoImage(file="Victoire.gif") #Image
map_défaite=PhotoImage(file="défaite.gif") #Image
#-----------------------#
# Fin: Variables        #
#-----------------------#

#-----------------------#
# Début: Fonctions      #
#-----------------------#
def getCase(x,y):
    """
    Permet d'obtenir la case où l'utilisateur clique sur les plateformes. Chaque case vaut d, c'est à dire 50 pixels
    """
    x=x//50
    y=y//50
    case = int(str(y)+str(x)) #Utilisation des str() pour éviter addition entre x et y, pour ensuite le transformer l'ensemble en int
    return case
    
def check():
    """
    Permet de vérifier après chaque tirs de chacun des joueurs si la partie est finie
    """
    global état,bateaux_bot,bateaux_joueur,map_victoire,map_défaite
    if bateaux_bot == []: #Si la liste est vide, le joueur gagne
        fen_map_victoire = Canvas(fen, bg="white", width=1300, height=800)
        fen_map_victoire.place(x=0,y=0)
        fen_map_victoire.create_image(750,400, image=map_victoire)
        label_victoire = Label(fen_map_victoire, text="Beau travail Amiral ! \n Si vous souhaitez conquérir d'autres mers, relancez le projet !", font=("Impact", 24))
        label_victoire.place(x=300,y=400)
    if bateaux_joueur == []: #Si la liste est vide, le bot gagne
        fen_map_défaite = Canvas(fen, bg="white", width=1300, height=800)
        fen_map_défaite.place(x=0,y=0)
        fen_map_défaite.create_image(750,400, image=map_défaite)
        label_défaite = Label(fen_map_défaite, text="Quelle humiliation ... \n Si vous souhaitez rejouer, relancez le projet !", font=("Impact", 24))
        label_défaite.place(x=300,y=400)
        
def tirer_bot(): 
    """ Fonction qui permet au bot de tirer """
    global état,can1,tuile1,cases_tirées_bot,cases_occupées_joueur,bateaux_joueur
    case=randint(0,99)
    if  état == "jouer_bot" and (case not in cases_tirées_bot): 
        if case in cases_occupées_joueur: #si la case appartient à cases_occupées_joueur qui est la liste des bateaux du joueur, alors la case du navire est considérée comme touchée
            can1.itemconfig((tuile1[case]), fill="red")
            cases_tirées_bot.extend([case]) #on rajoute la case dans la liste pour vérifier après que le bot ne retire pas sur la même case
            bateaux_joueur.remove(case) # lorsqu'elle se vide ( avec remove ) c'est là que la def Check prend tout son sens puisqu'il fixe la fin de la partie
            check()
            état = "jouer_joueur" #cet état est celui qui permet au joueur de tirer à son tour dans la fonction "tirer_joueur()"
        else:
            can1.itemconfig((tuile1[case]), fill="yellow") #la même choose que précédemment, cependant on considère que le tir est raté
            cases_tirées_bot.extend([case])
            état = "jouer_joueur"
    else:
        tirer_bot() #si la case est déjà occupée, alors on rexecute la fonction (récursivité)
        
def tirer_joueur(case):
    """ Fonction qui permet au joueur de tirer, l'argument 'case' est obtenu à partir de getCase() lorsque le joueur clique sur la plateforme. Suit le même fonctionnemnt que la fonction "tirer_bot """
    global état,can2,tuile2,cases_tirées_joueur,cases_occupées_bot,bateaux_bot
    if état == "jouer_joueur" and (case not in cases_tirées_joueur):
        if case in cases_occupées_bot:
            can2.itemconfig((tuile2[case]), fill="red")
            cases_tirées_joueur.extend([case])
            bateaux_bot.remove(case)
            check()
            état = "jouer_bot"
            tirer_bot()
        else:
            can2.itemconfig((tuile2[case]), fill="yellow")
            cases_tirées_joueur.extend([case])
            état = "jouer_bot"
            tirer_bot()
    elif case in cases_tirées_joueur:
        label_info_desc.config(text="Veuillez tirer sur une case libre")
        
def placement(case,impossible,position): #Problème de superposition des navires
    """ Fonction qui permet au joueur de placer ses navires, l'argument 'case' est obtenu à partir de getCase() lorsque le joueur clique sur la plateforme, l'arg impossible sont les cases où le joueur ne peut pas cliquer, l'arg position peut être soit égal à 0 (horizontal) ou 1 (vertical) """
    global cases_occupées_joueur,can1,tuile1,b,état,bateaux_joueur
    if b == 0: #porte-avion (5 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1),(case+2),(case+3),(case+4))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+1),(case+2),(case+3),(case+4)])
            can1.itemconfig((tuile1[case]), fill="purple")
            can1.itemconfig((tuile1[case]+2), fill="purple")
            can1.itemconfig((tuile1[case]+4), fill="purple")
            can1.itemconfig((tuile1[case]+6), fill="purple")
            can1.itemconfig((tuile1[case]+8), fill="purple")
            b=1 #pour passer au bateau suivant
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10),(case+20),(case+30),(case+40))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+10),(case+20),(case+30),(case+40)])
            can1.itemconfig((tuile1[case]), fill="purple")
            can1.itemconfig((tuile1[case]+20), fill="purple")
            can1.itemconfig((tuile1[case]+40), fill="purple")
            can1.itemconfig((tuile1[case]+60), fill="purple")
            can1.itemconfig((tuile1[case]+80), fill="purple")
            b=1 #pour passer au bateau suivant
    if b == 1: #croiseur (4 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1),(case+2),(case+3))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+1),(case+2),(case+3)])
            can1.itemconfig((tuile1[case]), fill="green")
            can1.itemconfig((tuile1[case]+2), fill="green")
            can1.itemconfig((tuile1[case]+4), fill="green")
            can1.itemconfig((tuile1[case]+6), fill="green")
            b=2
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10),(case+20),(case+30))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+10),(case+20),(case+30)])
            can1.itemconfig((tuile1[case]), fill="green")
            can1.itemconfig((tuile1[case]+20), fill="green")
            can1.itemconfig((tuile1[case]+40), fill="green")
            can1.itemconfig((tuile1[case]+60), fill="green")
            b=2
    if b == 2 or b == 3: #contre-torpilleur et sous-marin (3 cases chacun)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1),(case+2))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+1),(case+2)])
            can1.itemconfig((tuile1[case]), fill="blue")
            can1.itemconfig((tuile1[case]+2), fill="blue")
            can1.itemconfig((tuile1[case]+4), fill="blue")
            b=b+1
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10),(case+20))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+10),(case+20)])
            can1.itemconfig((tuile1[case]), fill="blue")
            can1.itemconfig((tuile1[case]+20), fill="blue")
            can1.itemconfig((tuile1[case]+40), fill="blue")
            b=b+1
    if b == 4: #torpilleur(2 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+1)])
            can1.itemconfig((tuile1[case]), fill="black")
            can1.itemconfig((tuile1[case]+2), fill="black")
            bateaux_joueur = cases_occupées_joueur
            état = "jouer_joueur"
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10))).intersection(set(cases_occupées_joueur))) == 0:
            cases_occupées_joueur.extend([case,(case+10)])
            can1.itemconfig((tuile1[case]), fill="black")
            can1.itemconfig((tuile1[case]+20), fill="black")
            bateaux_joueur = cases_occupées_joueur
            état="jouer_joueur"
            label_info.config(text="Informations:")
            label_info_desc.config(text="A vous de tirer ...")

def gauche(event):
    """ Fonction qui est appellée lorsque le joueur clique sur une plateforme avec un clique gauche, l'argument event contient les donnée par rapport au clique comme les positions """
    global état,b
    if état == "jouer_joueur": #Cette condition est nécessaire en première position lors du placement pour éviter des conflits avec l'état "placement_joueur"
        label_info.config(text="Informations:")
        label_info_desc.config(text="A vous de tirer ...")
        tirer_joueur(getCase((event.x),(event.y))) #event.x et event.y permettent de connaitre les coordonnée du clique
    if état == "jouer_bot": #Cette état, évite le joueur de joueur plusieurs fois alors que le bot n'a pas encore joué
        label_info.config(text="Informations:")
        label_info_desc.config(text="Veuillez attendre que le bot joue")      
    if état == "placement_joueur":
        label_info_desc.config(text="Placement joueur")
        if b == 0:
            label_info_desc.config(text="Veuillez placer le porte-avion (5 cases)")
            impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97,6,16,26,36,46,56,66,76,86,96]
            placement((getCase((event.x),(event.y))),impossible,0)
        if b == 1:
            label_info_desc.config(text="Veuillez placer le croiseur (4 cases)")
            impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97]
            placement((getCase((event.x),(event.y))),impossible,0)
        if b == 2 or b == 3:
            label_info_desc.config(text="Veuillez placer le contre-torpilleur (3 cases)")
            impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98]
            placement((getCase((event.x),(event.y))),impossible,0)
        if b == 4:
            label_info_desc.config(text="Veuillez placer le torpilleur (2 cases)")
            impossible=[9,19,29,39,49,59,69,79,89,99]
            placement((getCase((event.x),(event.y))),impossible,0) 
    
        
def droit(event):
    """  Fonction qui est appellée lorsque le joueur clique sur une plateforme avec un clique gauche, l'argument event contient les donnée par rapport au clique comme les positions, même fonctionnement que le clique gauche """
    global état,b
    if état == "jouer_joueur":
        label_info.config(text="Informations:")
        label_info_desc.config(text="A vous de tirer ...")
        tirer_joueur(getCase((event.x),(event.y)))
    if état == "jouer_bot":
        label_info.config(text="Informations:")
        label_info_desc.config(text="Veuillez attendre que le bot joue")
    if état == "placement_joueur":
        label_info_desc.config(text="Placement joueur")
        if b == 0:
            label_info_desc.config(text="Veuillez placer le porte-avion (5 cases)")
            impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89,70,71,72,73,74,75,76,77,78,79,60,61,62,63,64,65,66,67,68,69]
            placement((getCase((event.x),(event.y))),impossible,1)             
        if b == 1:
            label_info_desc.config(text="Veuillez placer le croiseur (4 cases)")
            impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89,70,71,72,73,74,75,76,77,78,79]
            placement((getCase((event.x),(event.y))),impossible,1) 
        if b == 2 or b == 3:
            label_info_desc.config(text="Veuillez placer le contre-torpilleur (3 cases)")
            impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89]
            placement((getCase((event.x),(event.y))),impossible,1) 
        if b == 4:
            label_info_desc.config(text="Veuillez placer le torpilleur (2 cases)")
            impossible=[90,91,92,93,94,95,95,96,97,98,99]
            placement((getCase((event.x),(event.y))),impossible,1)

def random(k,position,impossible):
    """ Permet de générer des case où il n'y a pas encore de navires placé et qui soit possible (éviter que le bateau soit sur deux lignes), l'argument k correspond au navire en cours de placement """
    global cases_occupées_bot
    case = randint(0,99)
    if k == 0: #porte-avion (5 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1),(case+2),(case+3),(case+4))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+1),(case+2),(case+3),(case+4)])
            return case
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10),(case+20),(case+30),(case+40))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+10),(case+20),(case+30),(case+40)])
            return case
        else:
            return random(k,position,impossible)
    if k == 1: #croiseur (4 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1),(case+2),(case+3))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+1),(case+2),(case+3)])
            case=int(case)
            return case
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10),(case+20),(case+30))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+10),(case+20),(case+30)])
            return case
        else:
            return random(k,position,impossible)
    if k == 2 or k == 3: #sous-marin et contre-torpilleur (3 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1),(case+2))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+1),(case+2)])
            return case
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10),(case+20))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+10),(case+20)])
            return case
        else:
            return random(k,position,impossible)
    if k == 4: #torpilleur (2 cases)
        if position == 0 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+1))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+1)])
            return case
        elif position == 1 and len(set(((case),(case))).intersection(set(impossible))) == 0 and len(set(((case),(case+10))).intersection(set(cases_occupées_bot))) == 0:
            cases_occupées_bot.extend([case,(case+10)])
            return case
        else:
            return random(k,position,impossible)
            
#-----------------------#
# Fin:   Fonctions      #
#-----------------------#
#-----------------------#
# Début: Jeu            #
#-----------------------#
def jouer(): #def initiale permettant la créatoin de la fenêtre de jeu est l'insertion des premiers plateaux
    """ Fonction qui permet la génération de l'interface de jeu """
    global état,can1,can2,tuile1,tuile2,bateaux_bot,map_jeu
    #Suppression des éléments présent dans le menu d'accueil
    can_menu.config(width=0, heigh=0) #permet faire en sorte de supprimer le canvas
    jouer_button.destroy()
    info_label.destroy()
    
    #On crée une image de fond 
    fen.geometry("1300x800")
    fen_map.place(x=0,y=0)
    fen_map.create_image(750,400, image=map_jeu)
       
    #------------------------------#
    # Début: Génération du plateau #
    #------------------------------#
    #Réglages:
    d=50
    colonne=10
		
    #Partie 1:
    #génération du premier plateau -> joueur
    can1 = Canvas(fen, width= colonne*d, height= colonne*d)
    can1.bind("<Button-1>", gauche)  #permet d'attacher le event de def gauche au clic de la souris sur can1
    can1.bind("<Button-3>", droit)
    can1.place(x=100,y=150)
    tuile1 = []
    val1 = []
    for n in range(100): #car on prend un tableau de 100 cases, utilisation de l'aide fournit en classe
        
        x = (n%10)*d
        y = (n//10)*d
        tuile1 = tuile1 + [can1.create_rectangle(x,y,x+d,y+d)]
        can1.itemconfig(tuile1[n])
        val1 = val1 + [can1.create_text(x+d//2, y+d//2)]
	
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
    # idem que pour le plateau joueur
    
    can2 = Canvas(fen, width= colonne*d, height= colonne*d)
    can2.bind("<Button-1>", gauche)
    can2.place(x=700,y=150)
    tuile2 = []
    val2 = []
    for n in range(100):
        x = (n%10)*d
        y = (n//10)*d
        tuile2 = tuile2 + [can2.create_rectangle(x,y,x+d,y+d)]
        can2.itemconfig(tuile2[n])
        val2 = val2 + [can2.create_text(x+d//2, y+d//2)]

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
    
    label_info.place(x=600,y=675)
    label_info_desc.place(x=600,y=700)
    #------------------------------#
    # Fin: Génération du plateau   #
    #------------------------------#
    #------------------------------#
    # Début: Placement du bot      #
    #------------------------------#       
    ##Placement de l'AI
    état = "placement_bot"
    for k in range(0,5):
        if k == 0:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97,6,16,26,36,46,56,66,76,86,96]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89,70,71,72,73,74,75,76,77,78,79,60,61,62,63,64,65,66,67,68,69]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig((tuile2[case]))
                can2.itemconfig((tuile2[case]+2))
                can2.itemconfig((tuile2[case]+4))
                can2.itemconfig((tuile2[case]+6))
                can2.itemconfig((tuile2[case]+8))
            else:
                can2.itemconfig((tuile2[case]))
                can2.itemconfig((tuile2[case]+20))
                can2.itemconfig((tuile2[case]+40))
                can2.itemconfig((tuile2[case]+60))
                can2.itemconfig((tuile2[case]+80))
        if k == 1:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89,70,71,72,73,74,75,76,77,78,79]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case])
                can2.itemconfig((tuile2[case]+2))
                can2.itemconfig((tuile2[case]+4))
                can2.itemconfig((tuile2[case]+6))
            else:
                can2.itemconfig(tuile2[case])
                can2.itemconfig((tuile2[case]+20))
                can2.itemconfig((tuile2[case]+40))
                can2.itemconfig((tuile2[case]+60))
        if k == 2 or k == 3:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case])
                can2.itemconfig((tuile2[case]+2))
                can2.itemconfig((tuile2[case]+4))
            else:
                can2.itemconfig(tuile2[case])
                can2.itemconfig((tuile2[case]+20))
                can2.itemconfig((tuile2[case]+40))
        if k == 4:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case])
                can2.itemconfig((tuile2[case]+2))
            else:
                can2.itemconfig(tuile2[case])
                can2.itemconfig((tuile2[case]+20))
    bateaux_bot = cases_occupées_bot #On copie la liste qui sera nécessaire pour la fonction check()
    #------------------------------#
    # Fin: Placement du bot        #
    #------------------------------#
                
    #------------------------------#
    # Début: Placement joueur      #
    #------------------------------#
    #Initialisation
    état = "placement_joueur" #afin de prévenir que l'état d'initialisation est terminé (c'est à dire que l'interface est pleinement généré et que le bot est placé ses navires) et que l'état est à présent celui d'état joueur
    label_info_desc.config(text="Veuillez placer le porte-avion (5 cases)")
    label_info.config(text="Clique gauche pour que le bateau soit horizontal et clique droit pour qu'il soit vertical")
    #------------------------------#
    # Fin: Placement joueur        #
    #------------------------------#
#-----------------------#
# Fin: Jeu              #
#-----------------------#

#-----------------------#
# Début: MENU D'ACCUEIL #
#-----------------------#
fen.title("Bataille Navale")
fen.geometry("950x535")
#Créations d'un canvas afin de placer une image de fond
can_menu = Canvas(fen, bg="white", width=950, height=535)
can_menu.place(x=0,y=0)
can_menu.create_image(473,267, image=background_img)

jouer_button = Button(fen, text="Jouer !", command=jouer, cursor="pirate", font=("Helvetica",25))
info_label = Label(fen, text="Informations: \nIl y a deux plateformes, la première (celle de gauche) \n vous permettera de placer vos navires et voir où l'adversaire a tiré,\n Le second tableau vous permet tirer sur les navires ennemis,\n si le navire est touché, la case sera rouge,\n si le tir manque sa cible, la case sera jaune.\n Pour placer vos navires, utilisez le clique droit pour qu'ils soient verticals\n et le clique gauche pour qu'ils soient horizontals.", font=("Helvetica",10))

jouer_button.place(x=120,y=100)
info_label.place(x=400,y=75)
#-----------------------#
# Fin: MENU D'ACCUEIL   #
#-----------------------#
fen.mainloop() #Lancement de la fenêtre