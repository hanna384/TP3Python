# le 5 janvier 2021
# programme écrit par Hanna Albala
# lien gitHub    https://github.com/hanna384/TP3Python.git
# ToDo : 

from tkinter import Tk, Label, Button, PhotoImage, Canvas
#from tkinter import *
from functionsSI import *

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
Largeur = photo.height() 
Hauteur = photo.width()
monCanvas = Canvas(myWindow, width = 700, height =445)
item = monCanvas.create_image(0,0 , anchor ='nw' , image = photo)
monCanvas.grid(row=1, column= 0)

buttonNewGame = Button (myWindow, text="New Game", command = myWindow.destroy)
buttonNewGame.grid(row=1, column=1)

buttonQuit = Button (myWindow, text="Quitter", command = myWindow.destroy)
buttonQuit.grid(row=2, column=1)


myWindow.mainloop()