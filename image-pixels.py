#IMPORTS
# Vous devez installer Pillow (v5.4.0 utilisée ici)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#### Début du CODE

chemin = "./media/image/oslo.png"

print("Ouverture du fichier ", chemin)
imageOslo = Image.open(chemin)

print("Transformation de l'image en tableau de Pixel") # Quelle est la représentation du pixel ?
image = np.asarray(imageOslo)

# Affichage Lignes, Colonnes et nombre de plans
infosImage = image.shape
print("Width - Height - nombre de plans") # Qu'est-ce qu'un plan ?
print(infosImage) 

#FILTRE ROUGE
def filtreRouge(imageSource):
    im = np.copy(imageSource) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            im[i, j] = (r, 0, 0)
    return im
print("Application filtre rouge")
imageRouge = filtreRouge(image)
plt.imshow(imageRouge)
plt.show()

#FILTRE VERT
def filtreVert(imageSource):
    im = np.copy(imageSource) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            im[i, j] = (0, v, 0)
    return im
print("Application filtre vert")
imageVerte = filtreVert(image)
plt.imshow(imageVerte)
plt.show()

#FILTRE BLEU
def filtreBleu(imageSource):
    im = np.copy(imageSource) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            im[i, j] = (0, 0, b)
    return im
print("Application filtre bleu")
imageBleue = filtreBleu(image)
plt.imshow(imageBleue)
plt.show()

#FILTRE GRIS
def filtreGris(imageSource):
    im = np.copy(imageSource) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            moyenne = (int(r)+int(v)+int(b))/3
            im[i, j] = (moyenne, moyenne, moyenne)
    return im
print("Application filtre gris")
imageGrisee = filtreGris(image)
plt.imshow(imageGrisee)
plt.show()

#Affichage des couleurs de chaque pixels
def affichage_couleur_pixels(imageSource):
    for x in range(infosImage[0]):
        ligne = ""
        for y in range(infosImage[1]):
            ligne = ligne + str(image[x][y])
        print(ligne)
        print("\n")

#affichage_couleur_pixels(image)    
        
# Cette fonction permet de modifier les canaux de couleur selon une liste prédéfinie
# Rq: https://mortada.net/can-integer-operations-overflow-in-python.html
def ajoutBruit(imageSource, listeBruit):
    im = np.copy(imageSource) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            nouveauRouge = r + listeBruit[(i+j)%(len(listeBruit))]    
            nouveauVert = v - listeBruit[(j)%(len(listeBruit))]
            nouveauBleu = b - listeBruit[(i)%(len(listeBruit))]
            im[i, j] = ( nouveauRouge, nouveauVert, nouveauBleu)
    return im

listeBruit = [10, -100, -20, 200, 254, 300, 855, 654, 235, -89, 69, 13, 11, 15, 2018, 1993, 1964, 1961, 1998, 1993, -12, 23 ]

print("Application d'un bruit selon la liste suivante: ", listeBruit)
imageParasite = ajoutBruit(image, listeBruit)
plt.imshow(imageParasite)
plt.show()

def retraitBruit(imageSource, listeBruit):
    im = np.copy(imageSource) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            nouveauRouge = r - listeBruit[(i+j)%(len(listeBruit))]    
            nouveauVert = v + listeBruit[(j)%(len(listeBruit))]
            nouveauBleu = b + listeBruit[(i)%(len(listeBruit))]
            im[i, j] = ( nouveauRouge, nouveauVert, nouveauBleu)
    return im
    
# Rq: ajoutBruit puis retraitBruit == imageSource -> https://fr.wikipedia.org/wiki/Isomorphisme 
print("Retrait du bruit selon la liste suivante: ", listeBruit)
imageSansParasite = retraitBruit( imageParasite, listeBruit )
plt.imshow(imageSansParasite)
plt.show()

print("Fin du programme")