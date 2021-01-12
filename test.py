from tkinter import *
 
def deplacement():
    global dx, dy
    #On deplace la balle :
    canvas.move(balle1,dx,dy)
    #On repete cette fonction
    tk.after(20,deplacement)
 
#Deplacement de la balle au départ:
dx=0
dy=5


 
#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 
#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()
 
#On cree une balle:
balle1 = canvas.create_oval(10,10,30,30,fill='red')


 
deplacement()
 
#On lance la boucle principale:
tk.mainloop()