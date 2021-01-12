# le 5 janvier 2021
# programme écrit par Hanna Albala
#classes, méthodes et fonctions


from tkinter import *
import random


# classe des objets ennemies
#avec une position horizontal X et vertical Y
#avec une méthode de déplacement
class ennemis:

    def __init__(self):
        self.posX=random.randint(0,655)
        self.posY=random.randint(0,200)
    def creationEnnemi(self):
        #r rayon du cercle ennemi
        r=45
        #cercle de centre (posX,posY) et de rayon r
        monCanvas.create_oval(ennemi_1.posX, ennemi_1.posY, ennemi_1.posX+r, ennemi_1.posY+r, outline='red', fill='red')
        print (monCanvas.find_all())

        




