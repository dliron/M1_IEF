###### Importation des librairies utiles pour le projet
import pandas as pd
import numpy as np

###### Premiere partie : les variables
# 1 - les types de variables
a = "test"
type(a)

type(1)
type(1.0)
type(True)
type(False)

type(None)

type( [] )
type( list() )

malist = [1, 2, 3, 4, "test", True, False, None]


a = 5
print(f'la variable a vaut : {a} et son type est : {type(a)}')

pd.read_csv("input/base.csv", sep = ";")

###### Premiere partie : les structures de controle
# 1 - les listes
list()
[]
maList = [1, 2, 3, 4, "test", True, False, None]
maList[4]

# 2 - les dictionnaires
dict()
{}

monDict = { "prenom" : "Didier", "nom" : "Liron" }

monDict.keys()
monDict.values()

monDict["prenom"]

# 3 - les tuples
tuple()
()

# 4 - les sets
{1, 2, 2 ,3}
set()


###### Deuxieme partie : les boucles et les conditions
a = 4
if a > 4:
    print("a est superieur à 4")
elif a == 4:
    print("a vaut pile 4 !")
else:
    print("a est inferieur à 4...")

a != 4
a > 4
a >= 4
a < 4
a <= 4
a == 4

True and True
True & False
False & False
False & True

True | True
True | False
False | False
False | True

for i in range(0,10):
    print("Bonjour")
    print(i)
    if i > 5:
        break


a = 10
while a > 3:
    print(f"a est superieur à 3, il vaut {a}")
    a = a - 1


[1, 1, 2, 3, 5, 8]

maList = [1, 1] + [2]
len(maList)
maList[len(maList)-2]
maList[-2]


######## Exercices
################################

# 1 - Vérifier si un nombre est premier ou pas. Pour savoir si un nombre est divisible par un autre, utilisez le modulo (% en Python)

a = 7
isPrime = True
for i in range(2, a):
    if a % i == 0:
        print(f"{a} n'est pas premier, il est divisible par {i}")
        isPrime = False
        break
    
if isPrime:
    print(f"{a} est premier !")
else :
    print(f"{a} n'est pas premier")


# 2 - Les deux premiers termes de la suite de Fibonacci sont tous deux un. Les termes suivants de la séquence sont trouvés en additionnant les deux termes immédiatement précédents. Écrivez un code qui écrit les n termes de la séquence de Fibonacci pour tout n≥3. Initialisez une liste [1,1] et incrementez cette liste 

n = 6
listFibo = [1, 1]
for i in range(0, 6):
    newVal = listFibo[-1] + listFibo[-2]
    # listFibo = listFibo + [newVal]
    listFibo.append(newVal)
print(listFibo)
for i in listFibo:
    print(i)

# 3 - Écrivez un code qui simule le lancer d'une pièce avec une probabilité p associée aux piles,  jusqu’à obtenir fâce, et renvoie le nombre de piles obtenues. Ensuite, reproduisez l’exécution de ce code 100 fois et afficher le nombre maximum de piles obtenus lors d’une même séquence. 

import random as rd

p = 0.5
maxNbPiles = 0
for i in range(0, 100):
    nbPiles = 0
    while rd.random() <= p:
        nbPiles = nbPiles + 1

    if nbPiles > maxNbPiles:
        maxNbPiles = nbPiles
print(f"Le maximum de pile obtenu sur 100 lancers est : {maxNbPiles}")


