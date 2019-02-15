import turtle # https://docs.python.org/3.3/library/turtle.html

# Nous allons créer un logiciel permettant de dessiner un labyrinthe depuis une liste

# Observez le plateau ci-dessous
# On indique les "passages"
plateau = [
    [
        "HautDroite", "GaucheDroite", "GaucheBas"
    ],
    [
        "BasDroite", "GaucheDroite", "HautGauche"    
    ],
    [
        "HautDroite", "GaucheBas", "Fin"
    ],
    [
        "Rien", "HautBas", "BasHaut"    
    ],
    [
        "Rien", "HautDroite", "GaucheHaut"
    ]
]


# Fonction permettant de dessiner 1 case du plateau
def dessinerUneCase( typeCase, x, y, largeur, pensize):
    turtle.pensize( pensize)
    turtle.penup()
    turtle.setposition( x, y)
    turtle.setheading(0)
    if "Rien" in typeCase:
        return
    if "Fin" in typeCase:
        turtle.goto(x + largeurCase/2 ,y + largeurCase/2 )
        turtle.pendown()
        turtle.color('red', 'yellow')
        turtle.begin_fill()
        turtle.circle(largeurCase/4)
        turtle.end_fill()
        turtle.color('black', 'white')
        turtle.penup()
        return
    if not "Haut" in typeCase:
        turtle.pendown()
    turtle.forward(largeur)
    turtle.left(90)
    if "Droite" in typeCase:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(largeur)
    turtle.left(90)
    if "Bas" in typeCase:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(largeur)
    turtle.left(90)
    if "Gauche" in typeCase:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(largeur)
    turtle.left(90)
# ! Fin fonction dessinerUneCase


turtle.title("TP Tortue: Dessiner un labyrinthe depuis une liste")
turtle.delay(10)
largeurCase = 5

# X de gauche à droite et Y de haut vers le bas (Pour être dans le meme "sens" que la liste)
taille = 4 * largeurCase
turtle.setworldcoordinates(-1 * taille, 1 * taille , 1 * taille , -1 * taille)

pensize = 4
departX = -10
departY = -10

# On loope sur la liste et pour chaque case on demande le "dessin"
for indexHauteur in range(0, len(plateau) ):
    print( plateau[indexHauteur]) # Pour debug
    for indexLargeur in range( 0, len(plateau[indexHauteur])):
        typeCase = plateau[indexHauteur][indexLargeur]
        print( typeCase ) #Pour debug
        dessinerUneCase( typeCase,
                         departX + indexLargeur * largeurCase,
                         departY + indexHauteur * largeurCase,
                         largeurCase,
                         pensize)
    
    


     
