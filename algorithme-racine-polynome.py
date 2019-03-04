from math import *
import sys

def racine(tab):
    a, b, c = tab
    D=b**2-4*a*c
    print( "Discriminant: ",D)
    if D<0:
        return ["inconnue"]
    x1=round((-b-sqrt(D))/(2*a),2)
    x2=round((-b+sqrt(D))/(2*a),2)
    return [x1, x2]

def demanderVariables():
    try:
        a=float(input("A ?\n"))
        b=float(input("B ?\n"))
        c=float(input("C ?\n"))
    except:
        print("Erreur lors de l'input")
        print("Fin du programme")
        sys.exit()
        
    print( "Polynôme: ", a,"x² + ",b,"x +",c )
    return [a, b, c]

print( "Résolution de A*x² + B*x + C = 0" )
print( "Réponses: ", racine ( demanderVariables() ) )
    