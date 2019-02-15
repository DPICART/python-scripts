from tkinter import *
from tkinter import messagebox
import os # OS = Operating System = Système d'exploitation = Librairie permettant d'intéragir avec l'OS
import requests
import pygame # Permet de créer des jeux basiques. Ici on va sen servir pour jouer des sons
# Le but de ce script est de récupérer une ressource web en connaissant uniquement son url

# Exemple d'url pointant vers une ressource:
# http://www.beyermusic.net/IU/David%20Bowie/Heroes.mp3
print()
print("Début du script")
print()

def jouerSon( nomDuMp3 ):
    pygame.init()    # initialisation pygame
    pygame.mixer.music.load("./media/audio/"+nomDuMp3)  #outil pygame.mixer.music avec
    pygame.mixer.music.play()
    
jouerSon("metroid_door.mp3")

couleur_bg = "black"
couleur_fg = "limegreen"

gui = Tk() # GUI = Graphical User Interface = Interface Graphique Utilisateur = IHM = Interface Homme Machine
#  Une deuxième instance de Tk....gui2 = Tk() 
gui.configure(background='red') 
gui['background']='black'
# les deux lignes précédentes modifient loption background de gui. Les 2 écritures sont possibles
titre = Label(gui,
              text="H4CK - URL DOWNLOADER",
              bg=couleur_bg,
              fg=couleur_fg)# fg pour foreground et bg pour background
# Ce Widget de type Label, est affecté à la fenetre  gui. On vient modifier certaines propriétés du widget.
# Ici text est une propriété du widget que l'on vient< modifier avec du text :< ici H4...
titre.pack(padx=5,            
           pady=5)  # Au moment ou on instancie ('est le pack qui instancie) le label dans la fenetrenon lui dit d'appliquer un padding en x et y

frame1 = Frame(gui,
              bg="yellow") # On utilise un frame afin de "cloisonner" un groupe de widgets entre eux
#frame = cadre
frame1.pack()

Label(frame1,
      text="URL: ",
      bg=couleur_bg,
      fg=couleur_fg).pack(padx=5,
                         pady=5,
                         side=LEFT)

valeurDeLInput = StringVar()

inputDeTexte = Entry(frame1,
                     width=60,
                     textvariable=valeurDeLInput,
                     bg=couleur_fg,
                     fg=couleur_bg) #inversion couleur juste pour style

inputDeTexte.pack(padx=5,
                  pady=5,
                  side=LEFT)

frame2 = Frame(gui,
              bg=couleur_bg)
frame2.pack()

Label(frame2,
      text="Nouveau nom du fichier:",
      bg=couleur_bg,
      fg=couleur_fg).pack(padx=5,
                          pady=5,
                          side=LEFT)
# ici on a utilisé le constructeur du widget Label ( Label(..) )
# A partir du moment ou un constructeur est apppelé, une instance est créée
# Une instance est une sorte de "clone" d'un objet
#toto1 = Label()
#toto2 = Label()

# .pack() est une méthode du widget Label
valeurDuNouveauNom = StringVar()

# Dans inputDeTexte2 on stocke une instance du widget de type Entry. Linstance a été créé en appelant le constructeur du widget ( Entry(...) )
inputDeTexte2 = Entry( frame2,
                       textvariable=valeurDuNouveauNom,
                       bg=couleur_fg,
                       fg=couleur_bg) # pas de .pack a la suite si on stocke l'instance dans une variable

inputDeTexte2.pack(padx=5,
                   pady=5,
                   side=LEFT)


bouton = Button(gui,
                text="Lancer le téléchargement",
                bg=couleur_bg,
                fg=couleur_fg,
                activebackground="red",
                activeforeground="yellow")

bouton.pack(padx=5,
            pady=5)

def callbackBouton(event): # le nom "event" na aucune importance, il est généré (voir ci dessous)
    print("Clic sur le bouton, on démarre le processus")
    print("URL renseignée: ",valeurDeLInput.get())
    print("Vérification de l'URL en cours")
    # La fonction renvoie **True ou False permettant ainsi au If de savoir s'il continue ou non
    if chaineRessembleUrl( valeurDeLInput.get() ):
        print("URL commence bien par http ou https")
        print("Vérification du nom")
        if len(valeurDuNouveauNom.get())>3:
            print("Lancement du téléchargement")
            jouerSon("fizzle.mp3")
            telechargerLeLien( valeurDeLInput.get(), valeurDuNouveauNom.get() )
        else:
            print("Le nom semble incorrect")
            jouerSon('no.mp3')
            messagebox.showinfo("Erreur", "Le nom semble incorrect")
    else:
        print("L'URL ne semble pas correcte")
        jouerSon('no.mp3')
        messagebox.showinfo("Erreur", "L'URL ne semble pas correcte")

# Pour l'instance du widget de type bouton
# je lui demande d'écouter ( bind = lier) certains type d'événements ( = event)
# ici l'event écouté (ou surveillé) est un clic sur le bouton 1 de la souris
# si l'événement (ou event) est détecté/capturé/reçu on appelle la fonction de callback ( call = appel / back = retour)
# Attention, ici on ne met pas de parentheses mais lorsque la fonction sera appelée un parametre lui sera automatiquement associé
bouton.bind("<Button-1>", callbackBouton)
   
# **
def chaineRessembleUrl( chaine ):
    if chaine.startswith("http://") or chaine.startswith("https://"):
        return True
    return False

def telechargerLeLien( lien, nouveauNom ):
    try:
        dossier = "Téléchargements"
        creerDossierTelechargement( dossier ) # On créé un dossier dans lequel on ira mettre notre téléchargement
        r = requests.get(lien, allow_redirects=True) # Création d'une requête vers la ressource ciblée
        print("Requête de téléchargement terminée")
        print("Enregistrement sur le disque en cours")
        open("./"+dossier+"/"+nouveauNom, 'wb').write(r.content)
        print("Terminé")
        jouerSon("goat.mp3")
        messagebox.showinfo("Bèèèèèéééé", "Téléchargement terminé")
    except:
        jouerSon("no.mp3")
        messagebox.showerror("Erreur", "Erreur lors du téléchargement\nLe lien spécifié est-il correct ?")
    
def creerDossierTelechargement( nomDuDossier):
    dossier = os.path.dirname("./"+nomDuDossier+"/")
    try:
        os.stat(dossier) # On essaye de récupérer les "stats" du dossier afin de voir s'il existe
    except: # s'il n'existe pas, on recoit une exception
        os.mkdir(dossier)  # On créé alors le dossier

# Remarque: Lors du téléchargement d'un gros fichier, le programme semble figé (il freeze). Pourquoi ? Car ici on travaille de manière synchrone (=tout à la suite)
# pour éviter ce freeze, il aurait fallu travailler de manière asynchrone (=en parallèle)

gui.mainloop()

