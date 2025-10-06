print("Bonjour")


a = 1
b = 1.0

type(a)
type(b)

type(True)
None

type([1, 3, 10])

print(f"Hello world, la valeur de a est {a}")


import pandas as pd
import numpy as np

pd.read_csv("input/base.csv", sep=",")

maListe = ["didier","Liron"]
maListe[1]

[[1,2,3], [5,6,7]]

type([])
type({})

monDict = {"nom": "LIRON",
           "prenom": "Didier", 
           "enfants": ["toto","Bretrand"]
          }
monDict.keys()
monDict.values()
monDict["nom"]

[m for m in monDict.keys()]

for i in monDict.keys():
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

if i == 10:
    print("10")
elif i < 5:
    print("< 5")
else:
    print("else")



# Vérifier si un nombre est premier ou pas. 
# Pour savoir si un nombre est divisible par un autre,
#   utilisez le modulo (%% en R)
a = 7
estpremier = True
for i in range(2,a):
  if a % i == 0:
    print(f"{a} n'est pas un nombre premier car il est divisible pas {i}")
    estpremier = False
    break
  
if estpremier:
  print("Le nombre est premier")
else:
  print("Il est pas premier")



# Les deux premiers termes de la suite de Fibonacci sont tous deux un. 
# Les termes suivants de la séquence sont trouvés en additionnant les deux termes immédiatement précédents. 
# Écrivez un code qui écrit les n termes de la séquence de Fibonacci pour tout n≥3
nb_fibo = 10
fibo = [1, 1]
for i in range(0,nb_fibo):
    new_fibo = fibo[len(fibo)-1] + fibo[len(fibo)-2]
    fibo = fibo +  [new_fibo]
fibo


# Écrivez un code qui simule le lancer d'une pièce avec une 
# probabilité p associée aux piles,  jusqu’à obtenir fâce, 
# et renvoie le nombre de piles obtenues. Ensuite, reproduisez 
# l’exécution de ce code 100 fois et afficher le nombre maximum 
# de piles obtenus lors d’une même séquence. Pour générer une
# probabilité entre 0 et 1, utilisez runif(1).
import random
max_sur_100try = 0
for i in range(0,100):
  max_try = 1
  
  resultat = random.random()
  while resultat < 0.5:
    resultat = random.random()
    max_try = max_try + 1
  
  
  if max_try > max_sur_100try:
    max_sur_100try = max_try
  
print(max_sur_100try)



def maFonction(a:int, b:int, c:int=10) -> int:
   """ Additionne trois nombres entrés comme input
    Args:
        a: la valeur de a 
        b: la valeur de b
        c: la valeur de c (default 10)
   """
   res = a + b + c
   return res


def maFonction(a, b, c=10):
   res = a + b + c
   return res

maFonction(1, 3, 5)





# Vérifier si un nombre est premier ou pas. 
# Pour savoir si un nombre est divisible par un autre,
#   utilisez le modulo (%% en R)
def estPremier(nb: int) -> bool:
    """ Test si un bombre est premier
        Args:
            - nb: le nombre à verifier
    """
    estpremier = True
    for i in range(2,nb):
        if nb % i == 0:
            print(f"{nb} n'est pas un nombre premier car il est divisible pas {i}")
            estpremier = False
            break
    
    if estpremier:
        print("Le nombre est premier")
    else:
        print("Il est pas premier")

    return estpremier

estPremier(7)

# Les deux premiers termes de la suite de Fibonacci sont tous deux un. 
# Les termes suivants de la séquence sont trouvés en additionnant les deux termes immédiatement précédents. 
# Écrivez un code qui écrit les n termes de la séquence de Fibonacci pour tout n≥3
def fibo_function(nb_fibo:int) -> list:
    """ Retourn les nb_fibo prochains termes de la suite de Fibonacci
        Args:
            - bn_fibo: nombre de terme à ajouter
    """
    fibo = [1, 1]
    for i in range(0,nb_fibo):
        new_fibo = fibo[len(fibo)-1] + fibo[len(fibo)-2]
        fibo = fibo +  [new_fibo]
    fibo


# Écrivez un code qui simule le lancer d'une pièce avec une 
# probabilité p associée aux piles,  jusqu’à obtenir fâce, 
# et renvoie le nombre de piles obtenues. Ensuite, reproduisez 
# l’exécution de ce code 100 fois et afficher le nombre maximum 
# de piles obtenus lors d’une même séquence. Pour générer une
# probabilité entre 0 et 1, utilisez runif(1).
import random

def lancerDePiece(nb_lancer:int, proba_pile:float=0.5) -> int:
    """ Simule la chaine max de piles avant d'avoir un face pour une proba donnée
        Args:
            - nb_lancer: le nombre de lancers
            - proba_pile: probabilité associée aux piles (default 0.5)
    """
    max_sur_100try = 0
    for i in range(0,nb_lancer):
        max_try = 1
        
        resultat = random.random()
        while resultat < proba_pile:
            resultat = random.random()
            max_try = max_try + 1
        
        if max_try > max_sur_100try:
            max_sur_100try = max_try

    return max_sur_100try
  
lancerDePiece(nb_lancer=100, proba_pile=0.5)






import pandas as pd

pd.DataFrame()

data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "Ville": ["Paris", "Lyon", "Marseille"]
}

data = pd.DataFrame(data)
type(data)

data[["Nom","Age"]]
data[data.Age > 25]

data.loc[data.Age > 25, ["Nom","Age"]]
data.iloc[:,1:3]

data.columns
data.index
data.shape
data.shape[0] # les lignes
data.shape[1] # les colonnes
len(data)

data.replace({"Ville": {"Paris":"Nice"
                       ,"Lyon":"Rennes"}},
            inplace=True)

data.Nom.value_counts()
data.sort_values("Age", ascending=False)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
eia_data = pd.read_csv("input/eia_data.csv")

eia_data.tail(10)
eia_data.head(10)

eia_data.rename( columns={"EIA.COPC.REG_OPEC":"test"
                         ,"EIA.PATC.REG_OECD": "titi"}
                , inplace=True)


eia_data = pd.read_csv("input/eia_data.csv")
eia_data.date = pd.to_datetime(eia_data.date, format="%d/%m/%Y")
eia_data.set_index("date", inplace=True)
type(eia_data)

eia_data.resample("QS").mean()
eia_data.shift(1)


eia_data.apply(lambda x: x.mean(), axis=1)
eia_data["EIA.PATC.WLD"].rolling(10).std()
eia_data["EIA.PATC.WLD"].rolling(10).mean()


