# le 5 janvier 2021
# programme écrit par Hanna Albala
# lien gitHub    https://github.com/hanna384/TP3Python.git
# ToDo : 
# faire en sorte que l'ennemi cogne les rebords et revient
#puis créer un tableau d'ennemies j'imagine
# Creer le vaisseau spatial

#from tkinter import Tk, Label, Button, PhotoImage, Canvas, Menu
from tkinter import *
from SpaceIvadersTools import *
import random


# classe des objets ennemies
#avec une position horizontal X et vertical Y
#avec une méthode de déplacement
class ennemis:
    
    def __init__(self):
        self.posX=random.randint(0,655)
        self.posY=random.randint(0,200)
        self.id=self.creationEnnemi()
        self.deplacement()
    def creationEnnemi(self):
        #r rayon du cercle ennemi
        r=45
        #cercle de centre (posX,posY) et de rayon r
        id_ennemi=monCanvas.create_oval(self.posX, self.posY, self.posX+r, self.posY+r, outline='red', fill='red')
        print (monCanvas.find_all())
        print (id_ennemi)
        #retourne l'id du widget (a l'interieur de monCanvas)
        return id_ennemi
    def deplacement(self):
        dx=1
        dy=0
        monCanvas.move(self.id,dx,dy)
        myWindow.after(40,self.deplacement)
        #if monCanvas.coords(balle)




class vaisseaux:
    
    def __init__(self):
        # self.x0=325, self.y0=415, self.x1=375, self.y1=415
        # self.x2=390, self.y2=445, self.x3=310, self.y3=445
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
        id_vaisseau=monCanvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3, outline='blue', fill='blue')
        print (monCanvas.find_all())
        print (id_ennemi)
        #retourne l'id du widget (a l'interieur de monCanvas)
        return id_vaisseau
    def deplacement(self):
        dx=1
        dy=0
        monCanvas.move(self.id,dx,dy)
        #if monCanvas.coords(balle)



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