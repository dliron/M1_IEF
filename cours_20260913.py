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