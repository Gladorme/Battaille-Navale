from tkinter import *
from random import randint

def jouer():
    fen = Tk()
    fen.geometry("1400x800")
    fen.title("Solo")
    fen.title("Solo - Bataille Navale")
        
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
    
    #Permet le placement aléatoire du bloc de "base"
    cases_occupées=[]
    def random(k,position,impossible):
        global cases_occupées
        case = randint(0,100)
        if k == 0:
            used=[]
            used.extend(cases_occupées)
            used.extend(impossible)
            if position == 0:
                while (case or (case+1) or (case+2) or (case+3) or (case+4)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+1),(case+2),(case+3),(case+4)])
            else:
                while (case or (case+10) or (case+20) or (case+30) or (case+40)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+10),(case+20),(case+30),(case+40)])
        if k == 1:
            used=[]
            used.extend(cases_occupées)
            used.extend(impossible)
            if position == 0:
                while (case or (case+1) or (case+2) or (case+3)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+1),(case+2),(case+3)])
            else:
                while (case or (case+10) or (case+20) or (case+30)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+10),(case+20),(case+30)])
        if k == 2:
            used=[]
            used.extend(cases_occupées)
            used.extend(impossible)
            if position == 0:
                while (case or (case+1) or (case+2)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+1),(case+2)])
            else:
                while (case or (case+10) or (case+20)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+10),(case+20)])
        if k == 3:
            used=[]
            used.extend(cases_occupées)
            used.extend(impossible)
            if position == 0:
                while (case or (case+1) or (case+2)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+1),(case+2)])
            else:
                while (case or (case+10) or (case+20)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+10),(case+20)])
        if k == 4:
            used=[]
            used.extend(cases_occupées)
            used.extend(impossible)
            if position == 0:
                while (case or (case+10)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+1)])
            else:
                while (case or (case+10)) in used:
                    case = randint(0,100)
                cases_occupées.extend([case,(case+10)])
        return case
                
            
    ##Placement de l'AI
    #var position: si position=0 alors le navire sera horizontal sinon si position=1 alors le bateau sera vertical
    for k in range(0,5):
        if k == 0:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97,6,16,26,36,46,56,66,76,86,96]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89,70,71,72,73,74,75,76,77,78,79,60,61,62,63,64,65,66,67,68,69]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig((tuile2[case]), fill="red")
                can2.itemconfig((tuile2[case]+2), fill="red")
                can2.itemconfig((tuile2[case]+4), fill="red")
                can2.itemconfig((tuile2[case]+6), fill="red")
                can2.itemconfig((tuile2[case]+8), fill="red")
            else:
                can2.itemconfig((tuile2[case]), fill="red")
                can2.itemconfig((tuile2[case]+20), fill="red")
                can2.itemconfig((tuile2[case]+40), fill="red")
                can2.itemconfig((tuile2[case]+60), fill="red")
                can2.itemconfig((tuile2[case]+80), fill="red")
        if k == 1:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89,70,71,72,73,74,75,76,77,78,79]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case], fill="yellow")
                can2.itemconfig((tuile2[case]+2), fill="yellow")
                can2.itemconfig((tuile2[case]+4), fill="yellow")
                can2.itemconfig((tuile2[case]+6), fill="yellow")
            else:
                can2.itemconfig(tuile2[case], fill="yellow")
                can2.itemconfig((tuile2[case]+20), fill="yellow")
                can2.itemconfig((tuile2[case]+40), fill="yellow")
                can2.itemconfig((tuile2[case]+60), fill="yellow")
        if k == 2:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case], fill="blue")
                can2.itemconfig((tuile2[case]+2), fill="blue")
                can2.itemconfig((tuile2[case]+4), fill="blue")
            else:
                can2.itemconfig(tuile2[case], fill="blue")
                can2.itemconfig((tuile2[case]+20), fill="blue")
                can2.itemconfig((tuile2[case]+40), fill="blue")
        if k == 3:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99,80,81,82,83,84,85,86,87,88,89]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case], fill="pink")
                can2.itemconfig((tuile2[case]+2), fill="pink")
                can2.itemconfig((tuile2[case]+4), fill="pink")
            else:
                can2.itemconfig(tuile2[case], fill="pink")
                can2.itemconfig((tuile2[case]+20), fill="pink")
                can2.itemconfig((tuile2[case]+40), fill="pink")
        if k == 4:
            position=randint(0,1)
            if position == 0:
                impossible=[9,19,29,39,49,59,69,79,89,99]
            else:
                impossible=[90,91,92,93,94,95,95,96,97,98,99]
            case=random(k,position,impossible)
            if position == 0:
                can2.itemconfig(tuile2[case], fill="black")
                can2.itemconfig((tuile2[case]+2), fill="black")
            else:
                can2.itemconfig(tuile2[case], fill="black")
                can2.itemconfig((tuile2[case]+20), fill="black")
    
    
    
    fen.mainloop()