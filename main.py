# le 5 janvier 2021
# programme écrit par Hanna Albala
# lien gitHub    https://github.com/hanna384/TP3Python.git
# ToDo : 
# faire en sorte que l'ennemi bouge tout seul
#puis ajouter plusieurs ennemis
#mais surtout il faut d'abord que l'affichage de l'ennemi se fasse dans une methode de la classe et pas dans le programme principal car sinon ça va être trop dur a gerer

#from tkinter import Tk, Label, Button, PhotoImage, Canvas, Menu
from tkinter import *
from SpaceIvadersTools import *






def mooveHorizontal(ennemi):
    #incremente coordonnées de la balle
    ennemi.posX += 20

    #rappel de mooveHorizontal toutes les 50ms
    ennemi.after(50, ennemi.mooveHorizontal)

#fonction principal du jeu
def new_game():
    nombreEnnemis=6

    ennemi_1= ennemis()
    
    #r rayon du cercle ennemi
    r=45
    #cercle de centre (posX,posY) et de rayon r
    monCanvas.create_oval(ennemi_1.posX, ennemi_1.posY, ennemi_1.posX+r, ennemi_1.posY+r, outline='red', fill='red')
    print (monCanvas.find_all())

    mooveHorizontal(ennemi_1)



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
item = monCanvas.create_image(0,0 , anchor ='nw' , image = photo)
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