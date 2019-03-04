# Donner la valeur de retour de cette fonction
def fonctionA():
    return 1

#print("fonctionA():",fonctionA())

# Donner la valeur de retour de cette fonction
def fonctionB():
    return 2

#print("fonctionB():",fonctionB())

# Donner la valeur de retour de cette fonction
def fonctionC():
    return 3

#print("fonctionC():",fonctionC())

# Donner la valeur de retour de cette fonction
def fonctionD():
    return fonctionA()+fonctionB()-fonctionC()

#print("fonctionD():",fonctionD())

# Donner la valeur de retour de cette fonction
def fonctionE():
    return fonctionB()+fonctionD()

#print("fonctionE():",fonctionE())

# Donner la valeur de retour de cette fonction en passant 5 en paramètre
def fonctionF( command ):
    return command * fonctionA()

#print("fonctionF():",fonctionF(5))

# Donner la valeur de retour de cette fonction en passant 2 en paramètre
def fonctionG( et ):
    return et**2

#print("fonctionG():",fonctionG(2))

# Donner la valeur de retour de cette fonction en passant 3 en paramètre
def fonctionH( conquer ):
    return conquer + fonctionG(conquer) + fonctionF( conquer )

#print("fonctionH():",fonctionH(3))

# Donner la valeur de retour de cette fonction en passant 10 en paramètre
def fonctionI( aleatoire ):
    return aleatoire + fonctionH( aleatoire ) + fonctionF( fonctionG( aleatoire) )

#print("fonctionI():",fonctionI(10))

# Donner la valeur de retour de cette fonction en passant 64 et 19 en paramètre
def fonctionJ( b , a):
    return [ a , b ]

#print("fonctionJ():",fonctionJ(64, 19))
    
# Donner la valeur de retour de cette fonction en passant 9.5 et 30.5 en paramètre
def fonctionK( b , a):
    return fonctionJ( 2*a, 2*b)

#print("fonctionK():",fonctionK(9.5, 30.5))

# Donner la valeur de retour de cette fonction en passant 5 en parametre
def fonctionL( a ):
    if a == 0:
        return 0
    return a + fonctionL(a - 1)

print("fonctionL():",fonctionL(5))