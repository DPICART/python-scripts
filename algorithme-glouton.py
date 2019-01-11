#
# ALGORITHME GLOUTON - Rendu de monnaie d'une machine à café
#

listePieces = [ ];
    
# [ Valeur Piece , Quantité dans machine ]
listePieces.append( [ 0.5, 6 ] );
listePieces.append( [ 0.05, 2 ] );
listePieces.append( [ 1.0, 1] );
listePieces.append( [ 0.01, 2 ] );
listePieces.append( [ 2.0, 3 ] );
listePieces.append( [ 0.1, 2 ] );
listePieces.append( [ 0.02, 0 ] );
listePieces.append( [ 0.2, 2 ] );

# Trie de la liste par valeur de piece croissante
listePieces.sort();

# Trie de la liste par valeur de piece décroissante (Pourquoi est-ce important de trier ?)
listePieces.reverse();
print( "Voici la liste des couples [Valeur - Quantité] de pièces", listePieces )

# Un client désire se payer un café.
# Un café coûte 0.27 €.
prix = 0.27;
print( "Le café coûte %s €" % prix);

# Le client paie en insérant une pièce de 2 € ( paiment = 2 ).
paiement = 2;
print( "Le client a payé %s €" % paiement);

# On détermine la somme à rembourser
aRendre = round((paiement - prix), 2);
print( "Nous devons donc rembourser %s €" % aRendre);

# On rembourse ensuite l'utilisateur avec les pièces dont on dispose.
# Rq: Si pas assez d'argent, on rembourse l'utilisateur autant qu'on le peut et on lui affiche un message d'excuse.

# On stockera la liste des pièces à rendre dans listePiecesARendre.
listePiecesARendre = [ ];

for (valeur, quantite) in listePieces :
    while True:
        if  valeur <= aRendre and round(quantite) > 0:
            # On rajoute la pièce courante aux pièces à rendre
            listePiecesARendre.append( valeur );
            # On cherche la position du couple [ valeur piece, quantite ]
            positionCouple = listePieces.index( ([valeur, quantite]));
            # et on modifie ce couple (on décrémente la quantité de la pièce courante de 1).
            quantite-=1;
            listePieces[ positionCouple ] = [ valeur, quantite];
            # On décrémente le montant à rendre au client
            # Rq: On arrondi afin d'éviter les soucis de précision ( Retirez le round vous verrez)
            aRendre = round(aRendre - valeur, 2) ;
        else:
            break;

print( "Voici les pièces rendues: ",listePiecesARendre );

# Si nous n'avons pas pu rembourser totalement
if aRendre != 0:
    print( "Nous sommes désolé, nous n'avons pas assez de pièces afin de vous rembourser totalement. (Manque ", aRendre, " €)");

print("Bonne dégustation !");

