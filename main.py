# le 5 janvier 2021
# programme écrit par Hanna Albala
# lien gitHub    https://github.com/hanna384/TP3Python.git
# ToDo : 
# gerer affichage des points gagnés
# créer missiles contre le vaisseau pour perdre des vies
#ameliorer les fonctions d'affichage photo fond

from tkinter import Tk, Label, Button, PhotoImage, Canvas, Menu
#from tkinter import *
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
        #r rayon du cercle ennemi
        self.r=45
        self.id=self.creationEnnemi()
        self.deplacement()
    def creationEnnemi(self):
        #cercle de centre (posX,posY) et de rayon r
        id_ennemi=monCanvas.create_oval(self.posX, self.posY, self.posX+self.r, self.posY+self.r, outline='red', fill='red', tag='aliens')
        # print (monCanvas.find_all())
        #retourne l'id du widget (de monCanvas)
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
#contient l'objet joueur
#contient une methode de création du missile
#contient une methode de déplacement du missile   
class missiles : 
    def __init__(self, joueur1):
        self.l=2 #demi largeur missile
        self.h=20#hauteur du missile
        self.joueur= joueur1 #recupère l'objet joueur
        listeVaisseau=monCanvas.find_withtag('monVaisseau')
        if listeVaisseau: #si mon vaisseau existe
            xHG, yHG, xBD, yBD=monCanvas.bbox('monVaisseau')
            #print(xHG, yHG, xBD, yBD)
            self.x0=xHG +(xBD-xHG)/2 -self.l
            self.x1=xHG +(xBD-xHG)/2 +self.l
            self.y0=yHG +self.h
            self.y1=yHG
            self.id=self.CreationMissile()
            #print(self.id)
            self.deplacementMissile()
    def CreationMissile(self):
        id_missile=monCanvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,outline='white', fill='white',tag='missile')
        return id_missile
    def deplacementMissile(self):
        listeMissiles=monCanvas.find_withtag(self.id)
        if listeMissiles: #si il y a des missiles existants
            # recupère la coordonnées y bas-droite du missile 
            xHG, yHG, xBD, yBD=monCanvas.bbox(self.id)
            if yBD <0:
                monCanvas.delete(self.id)
            else:
                dx=0
                dy=-20
                monCanvas.move(self.id,dx,dy)
                self.checkIfMeetAlien(xHG, yHG, xBD, yBD)#verifie si le missile rencontre un alien, si oui, détruit le missile et l'alien
                myWindow.after(40,self.deplacementMissile) 
    def checkIfMeetAlien(self,xHG_Mi, yHG_Mi, xBD_Mi, yBD_Mi):
        listeAliens=monCanvas.find_withtag('aliens')
        for i in listeAliens:
            xHG, yHG, xBD, yBD=monCanvas.bbox(i)
            if ((yHG_Mi>=(yBD-40))and(yHG_Mi<=yBD)) and ((xHG_Mi>=xHG)and(xHG_Mi<=(xBD-2*self.l))):
                monCanvas.delete(i,self.id)
                self.joueur.gagnerPoints()

class joueurs :
    def __init__(self):
        self.lives=3
        self.pointsWon=0
    def perdreUneVie(self):
        self.lives-=1
        #changer l'affichage du nb de vies
        labelLives.config(text='Lives' + str(self.lives))  
    def gagnerPoints(self):
        self.pointsWon+=2 
        #changer l'affichage du nb de points
        labelScore.config(text='Score : ' + str(self.pointsWon))         

def gameOver():
    monCanvas.delete('all') 
    creerImageGameOver()
         
        
def createMissile(event, joueur):
    missiles(joueur)
   

#fonction principal du jeu
def new_game():
    nombreEnnemis=10
    
    #supprime tout ce qui est contenu dans monCanvas(c-a-d les ennemis mais egalement l'image de fond)
    monCanvas.delete('all')
    creerImageFond() #on réafiche l'image de fond

    #instancier le joueur
    joueur1= joueurs()

    #instancier les ennemis
    for n in range(nombreEnnemis):
        ennemis()

    vaisseau1 = vaisseaux()

    monCanvas.focus_set()
    monCanvas.bind("<Right>",vaisseau1.mooveRight)
    monCanvas.bind("<Left>",vaisseau1.mooveLeft)
    monCanvas.bind("<space>",lambda event: createMissile(event, joueur1)) #syntaxe différente car on transmet un parametre joueur1

    

  
    

    
   




myWindow = Tk()
myWindow.title('Space Invaders')
myWindow.geometry('800x500')


labelScore = Label(myWindow, text = "Score : ")
labelScore.config(text='Score : ' + '0')
labelScore.grid(row=0, column=0)
#labelScore.pack(side= 'top')

labelLives = Label(myWindow)
labelLives.config(text='Lives : ' + '3')
labelLives.grid(row=0, column=1)
#labelLives.pack(side= 'top')

photo = PhotoImage(file = "terre.gif")
photo1 = PhotoImage(file = "game_over.gif")
photo2 = PhotoImage(file = "logo.gif")
largeur = 700 
hauteur = 445
monCanvas = Canvas(myWindow, width = largeur, height =hauteur)
# a ameliorer pour ne pas repeter la fonction 3 fois, mais si je met le photo = PhotoImage(file = ... dans la fonction ca ne marche pas
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








myWindow.mainloop()