# le 5 janvier 2021
# programme écrit par Hanna Albala
# lien gitHub    https://github.com/hanna384/TP3Python.git
# ToDo : 
# Lorsqu'un missile rencontre un ennemie, les deux doivents etre détruit
# gerer les vies restantes et le score
#ameliorer les fonctions d'affichage photo fond

from tkinter import Tk, Label, Button, PhotoImage, Canvas, Menu
#from tkinter import *
#from SpaceIvadersTools import *  #finalement j'ai mis mes fonctions et le programme principal dans un seul fichier
import random


# classe des objets ennemies
#contient une position horizontal X et vertical Y générés aléatoirement
#contient un sens de déplacement initié à droite ->1
#contient l'id du widget crée
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
        # print (monCanvas.find_all())
        # print (id_ennemi)
        #retourne l'id du widget (a l'interieur de monCanvas)
        return id_ennemi
    def deplacement(self):
        # recupère la coordonnées du point haut-gauche et bas-droite du rectangle imaginaire tracé autour de tous les aliens
        listeAliens=monCanvas.find_withtag('aliens')
        if listeAliens:
            xHG, yHG, xBD, yBD=monCanvas.bbox('aliens')
            dx=3
            dy=0
            #modifier le sens de déplacement si dépasse bords canvas
            if yBD>=415: #si atteint 415 c-a-d le haut du vaisseau : à améliorer, transmettre la coordonnée
                gameOver()
            else:
                if xBD >700 or xHG<0:
                    self.direction*=-1
                    dy=30
                monCanvas.move(self.id,dx*self.direction,dy)
                myWindow.after(40,self.deplacement)
        #if monCanvas.coords(balle)
        





# classe de l'objet vaisseau
#contient des coordonnées initiales   
#contient une méthode de création du widget vaisseau
#contient deux méthodes pour déplacer le vaisseau à droite et à gauche
class vaisseaux:
    
    def __init__(self):
        #coordonnées d'origine
        self.x0=325
        self.y0=415
        self.x1=375
        self.y1=415
        self.y1=415
        self.x2=390
        self.y2=445
        self.x3=310
        self.y3=445
        self.id=self.creationVaisseau()
    def creationVaisseau(self):
        #polygone de coordonnées x0,x1,y0,y1
        id_vaisseau=monCanvas.create_polygon(self.x0,self.y0,self.x1,self.y1,self.x2,self.y2,self.x3,self.y3, outline='blue', fill='blue',tag='monVaisseau')
        #retourne l'id du widget (a l'interieur de monCanvas)
        return id_vaisseau
    def mooveRight(self, event):
        # se deplacer de 5 pixels à droite
        dx=5
        dy=0
        # recupèrer la coordonnées du point en bas à droite du rectangle imaginaire tracé autour de ma forme
        listeVaisseau=monCanvas.find_withtag('monVaisseau')
        if listeVaisseau: #si mon vaisseau existe
            xHG, yHG, xBD, yBD=monCanvas.bbox('monVaisseau')
            if xBD<700 :
                monCanvas.move(self.id,dx,dy)
        
        #if monCanvas.coords(balle)
        #bbox pour les aliens utiliser un tag alien a declarer dans les options de create oval pour creer une boite autour de tous les aliens pour qu'ils reviennent
    
    def mooveLeft(self, event):
        # se deplacer de 5 pixels à gauche
        dx=-5
        dy=0
        listeVaisseau=monCanvas.find_withtag('monVaisseau')
        if listeVaisseau: #si mon vaisseau existe
            xHG, yHG, xBD, yBD=monCanvas.bbox('monVaisseau')
            #print(xHG, yHG, xBD, yBD)
            if xHG>0 :
                monCanvas.move(self.id,dx,dy)
    
    
#  classe des objets missiles
#contient des coordonnées initiales 
#contient l'id du missile 
#contient une methode de création du missile
#contient une methode de déplacement du missile   
class missiles : 
    def __init__(self):
        l=2 #demi largeur missile
        h=20#hauteur du missile
        listeVaisseau=monCanvas.find_withtag('monVaisseau')
        if listeVaisseau: #si mon vaisseau existe
            xHG, yHG, xBD, yBD=monCanvas.bbox('monVaisseau')
            #print(xHG, yHG, xBD, yBD)
            self.x0=xHG +(xBD-xHG)/2 -l
            self.x1=xHG +(xBD-xHG)/2 +l
            self.y0=yHG +h
            self.y1=yHG
            self.id=self.CreationMissile()
            #print(self.id)
            self.deplacementMissile()
    def CreationMissile(self):
        id_missile=monCanvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,outline='white', fill='white',tag='missile')
        return id_missile
    def deplacementMissile(self):
        # recupère la coordonnées y bas-droite du missile 
        xHG, yHG, xBD, yBD=monCanvas.bbox(self.id)
        if yBD <0:
            monCanvas.delete(self.id)
        else:
            dx=0
            dy=-20
            monCanvas.move(self.id,dx,dy)
            myWindow.after(40,self.deplacementMissile)  

def gameOver():
    monCanvas.delete('all') 
    creerImageGameOver()
         
        
def createMissile(event):
    missiles()

#fonction principal du jeu
def new_game():
    nombreEnnemis=10
    
    #supprime tout ce qui est contenu dans monCanvas(c-a-d les ennemis mais egalement l'image de fond)
    monCanvas.delete('all')
    creerImageFond() #on réafiche l'image de fond

    #instancier les ennemis
    for n in range(nombreEnnemis):
        ennemis()

    vaisseau1 = vaisseaux()
    #print(vaisseau1.id)

    monCanvas.focus_set()
    monCanvas.bind("<Right>",vaisseau1.mooveRight)
    monCanvas.bind("<Left>",vaisseau1.mooveLeft)
    monCanvas.bind("<space>",createMissile)

    


    
    

    
   




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
photo1 = PhotoImage(file = "game_over.gif")
photo2 = PhotoImage(file = "logo.gif")
largeur = 700 
hauteur = 445
monCanvas = Canvas(myWindow, width = largeur, height =hauteur)
# a ameliorer pour ne pas reperter la fonction 3 fois, mais si je met le photo = PhotoImage(file = ... dans la fonction ca ne marche pas
def creerImageFond():
    monCanvas.create_image(0,0 , anchor ='nw' , image = photo)
def creerImageGameOver():
    monCanvas.create_image(0,0 , anchor ='nw' , image = photo1)
def creerImageBienvenue():
    monCanvas.create_image(0,0 , anchor ='nw' , image = photo2)
creerImageBienvenue()
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