# On utilise la librairie de M. Kuranowski appelée pyroutelib3
# https://github.com/MKuranowski/pyroutelib3
# Cette librairie se base sur les données d'OpenStreetMap
from pyroutelib3 import Router
import sys

# Ici, à l'aide du constructeur (Router), on initialise un objet de type router
# Lors de l'instantiation, on lui spécifie via le paramètre "car" que l'on souhaite se déplacer en voiture.
# Mode de transport disponibles: car, cycle, foot, horse, tram, train
router = Router("car")

# On utilise la méthode findNode de l'objet router afin de récupérer le node le plus proche du couple latitude longitude spécifié
# https://www.openstreetmap.fr/ pour comprendre et https://www.openstreetmap.org pour trouver lat et lon
debutTrajet = router.findNode(50.198153,3.220213)
finTrajet = router.findNode(50.17601,3.22928)
# debutTrajet et finTrajet sont deux "Nodes" (=noeuds de navigation)

#Nous allonrs maintenant demander à l'objet router de trouver un ensemble de nodes à partir afin d'arriver du node de début au node de fin.
status, listeNodes = router.doRoute(debutTrajet, finTrajet)


print("Statut du calcul de l'itinéraire: ", status)

if status != 'success':
    print(" Fin du programme. Revoyez vos coordonnées GPS")
    Sys.exit(1);

print()
print()
print("Voici les nodes à suivre: ")
print( listeNodes )
# Pourquoi je vois des nombres ? Réponse ici: https://wiki.openstreetmap.org/wiki/Node
# Pour openstreetmap un node est un point dans l'espace et possède un id unique permettant de le reconnaitre.
# Dans le répertoires d'exécution du programme on remarque l'apparition d'un dossier tilescache. Que contient t'il ? Pourquoi en a t'on besoin ?
print()
print()
print( "Conversion de la liste de nodes en liste de couples (Latitude,Longitude)")
listeLatLon = []
for node in listeNodes:
    listeLatLon.append( router.nodeLatLon(node) )
print(listeLatLon)
print()
print()

# Nous avons maintenant une liste de couple latitude longitude mais pour un humain ce n'est pas très parlant.
# On peut utiliser un service de géocodage inverse ( lat long -> adresse ) afin de connaître l'adresse de nos points.
# Un service mis à dispo par l'état: https://adresse.data.gouv.fr/api -> /reverse/
# Exemple pour le point de départ: https://api-adresse.data.gouv.fr/reverse/?lat=50.198153&lon=3.220213




