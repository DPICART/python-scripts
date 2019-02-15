# Dans ce script nous allons utiliser Tkinter
# Tkinter est un module inclut de de base dans Python 3 permettant de créer des fenêtres sous différents OS

from tkinter import *

# Création d'une fenètre Tkinter
fenetre = Tk()

# ajout d'un label à la fenêtre (juste du tetxte cad etiquette)
label = Label(fenetre,
              text="Mon premier Label")
label.pack() # La méthode pack permet de spécifier que l'on veut instancier le label dans la fenêtre (= on le cré)

# Ajout d'un label de couleur à la fenêtre
label2 = Label(fenetre,
              text="Mon deuxième Label (coloré)",
              bg="limegreen")
label2.pack()

# Ajout d'un input à la fenetre(pas demande de texte cad input)
valeurInput = StringVar()
                         # creation widget type Entry (=entrée) truc blanc... qui s adapte fenetre 
input1 = Entry(fenetre,    
               width=30,
               textvariable=valeurInput) # zone de data(zone blanche)
input1.pack()

def fonctionDeCallback(event):
    print(event)
    truc.insert(END, event)

recuptext = StringVar()
truc = Text(fenetre,height=2,width=55)
truc.pack()
truc.bind("<Button-1>", fonctionDeCallback) # bind (=assigner) permet d'assigner un event listener à un élément
# je vais attendre le clic sur bouton souris (un événement) sur mon widget (l'élément) 
# Ajout d'un checkbox à la fenêtre
checkbox = Checkbutton(fenetre, text="Mon checkbox")
checkbox.pack()

# Création et ajout d'une listbox
listbox = Listbox(fenetre)
listbox.insert( 1, "Python")
listbox.insert( 2, "HTML")
listbox.insert( 3, "CSS")
listbox.insert( 4, "Javascript")
listbox.pack()

# Création d'un bouton
bouton1 = Button(fenetre,
                 text="Bouton 1")
bouton1.pack()

# Création d'un message d'alerte
from tkinter.messagebox import *

def fonctionDeCallback():
    showwarning('Titre warning',
                'Je suis un warning déclenché par un bouton')

bouton2 = Button(fenetre,
                 text="Bouton alerte",
                 command=fonctionDeCallback)
bouton2.pack()

fenetre.mainloop()


# Les éléments que nous avons utilisé sont des widgets
# Pour afficher les méthodes / options d'un widget on effectue la commande ci dessous
# print( dir( NomDuWidget() ) )
print( dir( Entry() ) ) # Ex: pour un bouton



