import pandas as pd

mylist = [1,2,3]
mylist[0]


[1,2,"test",True]

print("toto")

prenom = "Didier"
f"Bonjour {prenom}, comment ca va ?"


data = pd.read_csv("input/brent.csv")


for i in ["Binjour","tout","le","monde"]:
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1


def myfunction(a, b=3):
    res = a + b
    return res

myfunction(a=1)




myDict = {"voiture": 4, "vélo": 2, "tricycle": 3}

[val for val in myDict.values()]

animaux = ["girafe", "tigre", "singe", "souris"]

animaux[0]

for key, value in myDict.items():
    print(f"l'élément de clé {key} vaut {value}")


[f"l'élément de clé {key} vaut {value}" for key,value in myDict.items()]

def myfonction(a, b):
    a += 1
    b +=1
    return a,b

val1, val2 = myfonction(3, 5)


myDict = {"key1":"val1", "key2":"val2", "key3":"val3"}
type(myDict)
myDict.keys()

myDict["key1"]

for key, value in myDict.items():
    print(f"l'élément de clé {key} vaut {value}")


[ f"la valeur de a est '{a}'" for a in myDict.keys()]




import pandas as pd

data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "Ville": ["Paris", "Lyon", "Marseille"]
}
df = pd.DataFrame(data)
type(df)

df.shape[0]
df.shape[1]

df.describe().T
df.columns
df.index

df[["Age","Ville"]]

df.Age
df['Age']

df[df.Age>=25]


pd.DataFrame([myDict])


pd.concat([df,df], axis=1)

df.tail(1)

df.rename(columns={"Nom":"name", "Ville":"city"}, inplace=True)
df.replace({"name":{"Alice":"toto","Bob":"titi"}}, inplace=True)



data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "Ville": ["Paris", "Lyon", "Marseille"]
}

df = pd.DataFrame(data)

df.Nom.value_counts()
df.sort_values(["Age","Ville"])




df[~df.index.isin([1, 2])]
df.loc[0, ["Nom", "Âge"]]
df.iloc[-1,]
df.iloc[:,1:3] 
df.iloc[:2, :2]
df.Nom
df.loc[df["Âge"] > 23, ["Nom", "Ville"]]

len(df)
df.shape
df.describe().T
df.columns
df.index


df.rename(columns={"Nom":"test"})
df.sort_values("Ville")

df.apply(lambda x: print(x),axis=1)
df["Âge"].rolling(2,min_periods=2).mean()

df.pivot()


df = pd.read_csv("input/eia_data.csv")
from statistics import mean
df.iloc[:,1:].apply(lambda x: mean(x))

df.iloc[:,1:].rolling(10, min_periods=10).mean()

df_melt = df.melt(id_vars="date", var_name="symbol")
df_melt.pivot(index="date", columns="symbol",values="value").reset_index()


df.date = pd.to_datetime(df.date, format="%d/%m/%Y")
df.set_index("date", inplace=True)

df





import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

brent = pd.read_csv("input/brent.csv")
brent.drop(columns=["date"],inplace=True)

eiaData = pd.read_csv("input/eia_data.csv")

base = pd.concat([brent, eiaData], axis=1)

base.rename(columns={"DS.OILBREN.WLD.COLLAPSE.M":"brent"
                    ,"EIA.PATC.WLD":"patcwld"}
           ,inplace=True)


