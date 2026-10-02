###### Importation des librairies utiles pour le projet
import pandas as pd
import numpy as np
import random as rd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


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




#### Les fonctions

def maFonction(param1, param2="Valeur par defaut."):
    print(param1)
    print(param2)


maFonction(param1="Bonjour", param2="Hey !")
maFonction(param1="Bonjour")

a = 5

def maFonction2(a:int, b:int) -> int:
    """
    Additionne deux nombres entiers
    Args:
        a (int): premier nombre
        b (int): deuxieme nombre
    Returns:
        int: somme de a et b
    """
    a = a + 1
    valeur = a + b
    return(valeur)
    
toto = maFonction2(a = 1, b = 4)


# 1 - Vérifier si un nombre est premier ou pas. Pour savoir si un nombre est divisible par un autre, utilisez le modulo (% en Python)

def fonc_estpremier(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

fonc_estpremier(7)


# 2 - Les deux premiers termes de la suite de Fibonacci sont tous deux un. Les termes suivants de la séquence sont trouvés en additionnant les deux termes immédiatement précédents. Écrivez un code qui écrit les n termes de la séquence de Fibonacci pour tout n≥3. Initialisez une liste [1,1] et incrementez cette liste 

def fonc_fibo(n:int) -> list:
    """
    Calcule les n premiers termes de la suite de Fibonacci
    Args:
        n (int): nombre de termes à calculer
    Returns:
        list: les n premiers termes de la suite de Fibonacci
    """
    listFibo = [1, 1]
    for i in range(0, n):
        newVal = listFibo[-1] + listFibo[-2]
        listFibo.append(newVal)
    return listFibo

fonc_fibo(6)

# 3 - Écrivez un code qui simule le lancer d'une pièce avec une probabilité p associée aux piles,  jusqu’à obtenir fâce, et renvoie le nombre de piles obtenues. Ensuite, reproduisez l’exécution de ce code 100 fois et afficher le nombre maximum de piles obtenus lors d’une même séquence. 


def func_nbpiles(n=100, p=0.5):
    maxNbPiles = 0
    for i in range(0, n):
        nbPiles = 0
        while rd.random() <= p:
            nbPiles = nbPiles + 1

        if nbPiles > maxNbPiles:
            maxNbPiles = nbPiles
    return maxNbPiles

func_nbpiles()
func_nbpiles(n = 10000)
func_nbpiles(p = 0.99)



#########################################   PARTIE II   ###########################################
# Les DataFrame
#####################################################################################################
import pandas as pd

data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "Ville": ["Paris", "Lyon", "Marseille"]
}

data = pd.DataFrame(data)

data["Nom"]
data[["Nom","Age"]]
data.iloc[:,0]
data.iloc[0,:]
data.iloc[1:,:1]

data.loc[0:1, ["Nom","Age"]]


len(data) 
data.shape
data.describe().T
data.columns
data.index

data[data.Age >= 24]


brent = pd.read_csv("input/brent.csv", sep=",")
eia_data = pd.read_csv("input/eia_data.csv", sep=",")

brent.shape
eia_data.shape

base = pd.concat([brent, eia_data.iloc[:,1:]], axis = 1)
base.columns

base.rename( columns = {
        'DS.OILBREN.WLD.COLLAPSE.M' : "Prix_Brent",
        'EIA.COPC.REG_OPEC'         : "Consommation_OPEC",
        'EIA.COPS.REG_OPEC'         : "Offre_OPEC",
        'EIA.PAPR.REG_NONOPEC'      : "Production_non_OPEC",
        'EIA.PAPR.REG_OPEC'         : "Production_OPEC",
        'EIA.PAPR.RUS'              : "Production_Russie",
        'EIA.PAPR.USA'              : "Production_USA",
        'EIA.PASC.REG_OECD'         : "Consommation_OCDE",
        'EIA.PATC.CHN'              : "Consommation_Chine",
        'EIA.PATC.REG_NONOECD'      : "Consommation_non_OCDE",
        'EIA.PATC.REG_OECD'         : "Consommation_OCDE",
        'EIA.PATC.WLD'              : "Consommation_Mondiale"
       }, inplace = True )
base.head()


# 1 - Creez une sous base à partir de 'base' contenant les lignes de base avec la condition suivante : 
# Consommation mondiale > 100 et je ne veux que les colonnes date et Prix_Brent et consommation de la Chine
base2 = base.loc[base.Consommation_Mondiale>100,["date","Prix_Brent","Consommation_Chine"]]

# 2 - Reprenez cette sous base et n'affichez uniquement les lignes où la consommation de la Chine est < 15
base3 = base2[base2.Consommation_Chine < 15]

# 3 - Faites ceci en une seule ligne
base.loc[(base.Consommation_Mondiale>100) & (base.Consommation_Chine < 15),["date","Prix_Brent","Consommation_Chine"]]



######## Manipulation avancée des df
base.index
base.date = pd.to_datetime(base.date)
base.set_index("date", inplace = True)

base.Prix_Brent.head()
base.Prix_Brent.shift(1).head()

((base.Prix_Brent/base.Prix_Brent.shift(1)-1)*100).head()


base.Prix_Brent.rolling(window=5).mean().head()

base.apply(lambda x: x.mean(),axis=0)
base.apply(lambda x: x.mean(),axis=1)



## Exercice
# 1 - rechargez brent.csv et eia_data.csv
# 2 - Transformez les en serie temporelle
# 3 - Combinez les DataFrame dans une meme base avec pd.merge
# 4 - Ajoutez des colonnes à la base
     # - prix du brent lagé de 6 mois
     # - Ecart type mobile du prix du brent sur 12 mois
     # - Calculer le taux de croissance mensuel glissant moyen sur 6 mois
     # - Calculer l'ecart entre le prix du brent et sa moyenne mobile sur 12 mois


