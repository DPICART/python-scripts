#
# ALGORITHME DE TRI - Comment trier une liste de différentes manières
#
import random

#Création d'une liste de 100 entiers aléatoires non classés. (Sauf si vous avez extrêmement de chance)
tailleListe = 100
listeEntiersAleatoire = random.sample( range(1, tailleListe+1), tailleListe);

print("Voici la liste à trier: \n", listeEntiersAleatoire);

# Démonstration du tri par insertion
tableau = listeEntiersAleatoire
for i in range(1, len(tableau)):
    element = tableau[i]
    j = i
    while j > 0 and tableau[j-1]>element:
        tableau[j]=tableau[j-1]
        j-=1
    tableau[j]=element
print( "Résultat Tri par insertion: \n", tableau )

# Démonstration du tri à bulles
tableau = listeEntiersAleatoire
doitPermuter = True
passage = 0
while doitPermuter == True:
    doitPermuter = False
    passage = passage + 1
    for index in range(0, len(tableau) - passage):
        if tableau[index] > tableau[index + 1]:
            doitPermuter = True
            tableau[index], tableau[index + 1] = tableau[index + 1], tableau[index]
print( "Résultat du Tri à bulles: \n", tableau )
        
# Démonstration du tri Boustrophédon (ou tri à bulle bidirectionnel)
tableau = listeEntiersAleatoire
permutation= True
versDroite = True
index = 0
debut=0
fin=len(tableau)-2
while permutation == True:
    permutation = False
    while (index<fin and versDroite==True) or (index>debut and versDroite==False) :
        if tableau[index] > tableau[index + 1]:
            permutation = True
            tableau[index], tableau[index + 1] = tableau[index + 1],tableau[index]
            if versDroite == True:
                valeur = 1
            else:
                valeur = -1
            index = index + valeur
        if versDroite:
            fin = fin - 1
        else:
            debut = debut + 1
        versDroite = not versDroite
print( "Résultat du tri Boustrophédon: \n", tableau)