# le 5 janvier 2021
# programme écrit par Hanna Albala
# lien gitHub    https://github.com/hanna384/TP3Python.git
# ToDo : 
# mettre repo en public
# 
#puis créer un tableau d'ennemies j'imagine
# 

#from tkinter import Tk, Label, Button, PhotoImage, Canvas, Menu
from tkinter import *
from SpaceIvadersTools import *
import random


# classe des objets ennemies
#contient une position horizontal X et vertical Y générés aléatoirement
#contient un sens de déplacement initié à droite ->1
#contient une méthode de création du widget ennemi
#contient une méthode pour déplacer les ennemis
class ennemis:
    
    def __init__(self):
        self.posX=random.randint(0,350)
        self.posY=random.randint(0,200)
        self.direction=1
        self.id=self.creationEnnemi()
        self.deplacement()
    def creationEnnemi(self):
        #r rayon du cercle ennemi
        r=45
        #cercle de centre (posX,posY) et de rayon r
        id_ennemi=monCanvas.create_oval(self.posX, self.posY, self.posX+r, self.posY+r, outline='red', fill='red', tag='aliens')
        print (monCanvas.find_all())
        print (id_ennemi)
        #retourne l'id du widget (a l'interieur de monCanvas)
        return id_ennemi
    def deplacement(self):
        # recupère la coordonnées du point haut-gauche et bas-droite du rectangle imaginaire tracé autour de tous les aliens
        xHG, yHG, xBD, yBD=monCanvas.bbox('aliens')
        #modifier le sens de déplacement si besoin
        if xBD >700 or xHG<0:
            self.direction*=-1
        dx=1
        dy=0
        monCanvas.move(self.id,dx*self.direction,dy)
        myWindow.after(40,self.deplacement)
        #if monCanvas.coords(balle)
        





# classe de l'objet vaisseau
#contient une méthode de création du widget vaisseau
#contient deux méthodes pour déplacer le vaisseau à droite et à gauche
class vaisseaux:
    
    def __init__(self):
        self.id=self.creationVaisseau()
    def creationVaisseau(self):
        #coordonnées d'origine
        x0=325
        y0=415
        x1=375
        y1=415
        x2=390
        y2=445
        x3=310
        y3=445
        #polygone de coordonnées x0,x1,y0,y1
        id_vaisseau=monCanvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3, outline='blue', fill='blue',tag='monVaisseau')
        #retourne l'id du widget (a l'interieur de monCanvas)
        return id_vaisseau
    def mooveRight(self, event):
        # se deplacer de 5 pixels à droite
        dx=5
        dy=0
        # recupèrer la coordonnées du point en bas à droite du rectangle imaginaire tracé autour de ma forme
        xHG, yHG, xBD, yBD=monCanvas.bbox('monVaisseau')
        if xBD<700 :
            monCanvas.move(self.id,dx,dy)
        
        #if monCanvas.coords(balle)
        #bbox pour les aliens utiliser un tag alien a declarer dans les options de create oval pour creer une boite autour de tous les aliens pour qu'ils reviennent
    
    def mooveLeft(self, event):
        # se deplacer de 5 pixels à gauche
        dx=-5
        dy=0
        xHG, yHG, xBD, yBD=monCanvas.bbox('monVaisseau')
        if xHG>0 :
            monCanvas.move(self.id,dx,dy)


#fonction principal du jeu
def new_game():
    nombreEnnemis=12
    
    #supprime tout ce qui est contenu dans monCanvas(c-a-d les ennemis mais egalement l'image de fond)
    monCanvas.delete('all')
    creerImageFond() #on réafiche l'image de fond

    #instancier les ennemis
    for n in range(nombreEnnemis):
        ennemis()

    vaisseau1 = vaisseaux()
    print(vaisseau1.id)

    #vaisseau1.bind("<KeyPress-Left>", lambda e: gfg.left(e)) 
    #monCanvas.bind("<Right>",mooveRight)
    # vaisseau1.bind("<Left>",mooveLeft)
    # vaisseau1.bind("<space>",tirer)
    # vaisseau1.bind("<KeyPress-Right>", mooveRight)
    monCanvas.focus_set()
    monCanvas.bind("<Right>",vaisseau1.mooveRight)
    monCanvas.bind("<Left>",vaisseau1.mooveLeft)
    

    
   




myWindow = Tk()
myWindow.title('Space Invaders')
myWindow.geometry('800x500')


labelScore = Label(myWindow, text = "Score : ")
labelScore.grid(row=0, column=0)
#labelScore.pack(side= 'top')

labelLives = Label(myWindow, text = "Lives : ")
labelLives.grid(row=0, column=1)
#labelLives.pack(side= 'top')

photo = PhotoImage(file = "terre.gif")
largeur = 700 
hauteur = 445
monCanvas = Canvas(myWindow, width = largeur, height =hauteur)
def creerImageFond():
    item = monCanvas.create_image(0,0 , anchor ='nw' , image = photo)
creerImageFond()
monCanvas.grid(row=1, column= 0)


buttonNewGame = Button (myWindow, text="New Game", command = new_game)
buttonNewGame.grid(row=1, column=1)

buttonQuit = Button (myWindow, text="Quitter", command = myWindow.destroy)
buttonQuit.grid(row=2, column=1)

#création du menu
# menu = Menu(myWindow) 
# monMenu = Menu(menu, tearoff = 0)   
# monMenu.add_command(label="Quit", command = myWindow.destroy) 
# monMenu.add_command(label="TEST", command = myWindow.destroy)  
  
# myWindow.config(menu = menu) 








myWindow.mainloop()