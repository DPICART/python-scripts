# Ajd nous allons travailler avec le format JSON
# Le JSON permet à des machines de communiquer entres elles via une structure de donnée
# Le JSON est une manière textuelle de représenter de l'information ( comme le XML )

## Selon WIKIPEDIA:
#Un document JSON a pour fonction de représenter de l'information accompagnée d'étiquettes permettant d'en interpréter les divers éléments,
#sans aucune restriction sur le nombre de celles-ci.

#Un document JSON ne comprend que deux types d'éléments structurels :
#des ensembles de paires « nom » (alias « clé ») / « valeur » ;
#des listes ordonnées de valeurs.

#Ces mêmes éléments représentent trois types de données :
#des objets ;
#des tableaux ;
#des valeurs génériques de type tableau, objet, booléen, nombre, chaîne ou null.

# Afin de pouvoir travailler, un fichier contenant des données sous format JSON a été sauvegardé dans la cible ci dessous:
chemin = './media/data/utilisateurs.json'

# Rq: Nous allons récupérer un json via lecture d'un fichier mais nous aurions pu le récupérer via une requête HTTP.

# Prendre le temps de regarder la structure du fichier json (il contient les informations concernant trois utilisateurs différents)

# Commencons
import json
# On ouvre le fichier contenant les données Json
with open(chemin) as fichier:
    # On charge ce fichier json en tant que tableau dans python
    data = json.load(fichier)
    
# On peut alors utiliser les données chargées
print(data)

print()

print( "Nombre de users:", len(data)) 

print()

# je désire afficher le login des utilisateurs
print("Affichage des logins: ")
for index in range(0, len(data) ):
    print(data[index]["login"]["username"])

print()

#Rq: on peut érire le for différemment
print("Affichage des logins (V2): ")
for user in data:
    print(user["login"]["username"])
print()

# Programme permettant de chercher un utilisateur afin d'afficher certaines infos le concernant.
print( "Chercher utilisateur V1")
pseudo = input("Entrez le nom d'utilisateur:\n")
print("Voici les infos dont nous disposons concernant l'utilisateur suivant: ", pseudo)
trouve = False
for user in data:
    if user["login"]["username"] == pseudo:
        print("Gender: ", user["gender"])
        print("Name: ", user["name"]["title"], user["name"]["first"],user["name"]["last"] )
        print("Email: ", user["email"])
        print("Location: ", user["location"]["street"], user["location"]["city"], user["location"]["state"], user["location"]["postcode"])
        trouve = True
        break
if not trouve:
    print( "Nous n'avons malheureusement aucune info sur cet utilisateur")
print()

# Nous allons réécrire le programme ci-dessus en le découpant en plusieurs fonctions
## fonction permettant de trouver un utilisateur dans une liste en fnction de son username
print( "Chercher utilisateur V2")
def trouverUtilisateur(username, listeUser):
    for user in listeUser:
        if user["login"]["username"] == username:
            return user
    return False

## Fonction qui pour un utilisateur donné, affiche certaines infos
def afficherInfosUtilisateur( utilisateur):
    print("Gender: ", utilisateur["gender"])
    print("Name: ", utilisateur["name"]["title"], utilisateur["name"]["first"], utilisateur["name"]["last"] )
    print("Email: ", utilisateur["email"])
    print("Location: ", utilisateur["location"]["street"], utilisateur["location"]["city"], utilisateur["location"]["state"], utilisateur["location"]["postcode"])
  
## Fonction principale regroupant les 2 précédentes.
def chercherUtilisateur():
    pseudo = input("Entrez le nom d'utilisateur:\n")
    print("Voici les infos dont nous disposons concernant l'utilisateur suivant: ", pseudo)
    utilisateur = trouverUtilisateur( pseudo, data)
    if not utilisateur:
        print("Nous n'avons malheureusement aucune info sur cet utilisateur")
    else:
        afficherInfosUtilisateur( utilisateur)

## Appel de la fonction principale
chercherUtilisateur()
print()

# A toi !
## Créer une fonction demandant à l'utilisateur un pseudo puis un mot de passe signature: demanderIdentifiants() Cette fonction doit renvoyer un tuple de string
###def demanderIdentifiants():


## Créer une fonction permettant de trouver un utilisateur dans une liste d'utilisateurs (cette fonction devra rechercher par username et également vérifier le mot de passe)
### def chercherEtVerifierUtilisateur( listeUser, username, motDePasse):
    

## Créer une fonction "seConnecter" qui fera appelle aux 2 fonctions précédentes:
### Remarque: Un message différent doit apparaitre selon que l'utilisateur soit correctement identifié ou non
### def seConnecter():
    



## BONUS: lire un json depuis internet (nécessite un accès internet)
# Lisez la page https://requests-fr.readthedocs.io/en/latest/
# Installez la librairie "requests" avant de l'importer
import requests

# En utilisant requests, effectuer un appel vers https://randomuser.me/api
print("Requete en cours vers randomuser.me")
r = requests.get('https://randomuser.me/api')

# Afficher le status code de la requete (le status code fait parti de la réponse de la requête) (200 = ok, 404 = non trouvé, 500 = erreur serveur etc)
# https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP
print( "Status code: ", r.status_code )
print()

# Stocker le résultat dans monJsonVenuDuWeb sous format texte
monJsonVenuDuWeb = r.text

# charger monJsonVenuDuWeb dans un tableau en utilisant json.loads
data2 = json.loads(monJsonVenuDuWeb)
print("Affichage JSON complet")

print("DATA RECUE: ", data2)
print()
# Observer la réponse précédente et Afficher l'email de l'utilisateur
print( "email: ", data2["results"][0]["email"])

print( "Fin programme")


