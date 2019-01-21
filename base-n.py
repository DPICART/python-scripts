# BASE N
import math

# http://villemin.gerard.free.fr/Wwwgvmm/Numerati/ConBin.htm
# Il existe 10 sortes de personnes
# ceux qui connaissent le binaire et ceux qui ne le connaissent pas.

nombre = 13
print("Nombre ", nombre)

base = 2
print("Base ", base)

poidMax = int(nombre/base)
print("PoidMax ", poidMax)

def toBase2(nombre):
    reste = nombre
    newNombre = ""
    for poid in reversed( range(poidMax+1) ):
        if (reste - math.pow(base, poid))>=0 :
            reste -= math.pow(base, poid)
            newNombre += str(1)
        else:
            newNombre += str(0)
    return newNombre
    
print("Nombre en base ", base, ": ", toBase2(nombre) )

### EN COURS / PAS TERMINE

