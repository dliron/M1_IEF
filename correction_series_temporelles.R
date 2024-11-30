# Importer les fichiers brent.csv et eia_data.csv depuis le repertoire input et renommer les colonnes (cf. slide 13)
brent = read.csv("input/brent.csv")
colnames(brent) = "brent"

eiaData = read.csv("input/eia_data.csv")
colnames(eiaData) = c("date","cocpopec","copsopec","paprnonopec","papropec","paprrus","paprus","pascoecd","patcchn","patcnonoecd","patcoecd","patcwld")

# Transformer ces deux structures en série temporelle avec un format xts
library(xts)

brent = xts(brent[,-1], order.by = as.Date(brent[,1], format = "%d/%m/%Y"))
colnames(brent) = "brent"

eiaData = xts(eiaData[,-1], order.by = as.Date(eiaData[,1], format = "%d/%m/%Y"))

# Fusionner les données dans une variable «base»
base = cbind(brent, eiaData)

# Formater «base» en trimestrielle
base = apply.quarterly(base, mean)
index(base) = as.Date(format(index(brent), "%Y-%m-01"))

library(lubridate)
index(base) = index(base) - months(2)

# Créer une variable «base_ts» qui est la même que «base» mais au format ts
base_ts = ts(base, start = 2003, frequency = 4)

# Effectuer un lag de 5 trimestres sur la colonne «brent» de «base» et l’ajouter dans la base
brentL5 = lag(base$brent, 5)
colnames(brentL5) = "brentL5"
base = cbind(base, brentL5)

# Calculer une moyenne mobile 6 trimestres sur cette même colonne et l’ajouter dans la base
brentL5MA6 = rollapply(base$brentL5, 6, mean)
colnames(brentL5MA6) = "brentL5MA6"
base = cbind(base, brentL5MA6)

# Calculer la croissance annuelle du brent et l’ajouter dans la base
tbrent = (base$brent/lag(base$brent, 4) - 1) * 100
colnames(tbrent) = "tbrent"
base = cbind(base, tbrent)

# Créer un indicateur qui vaut 1 si la croissance du brent est positive ou nulle, 0 sinon, et l’ajouter dans la base
istbrentpos = (base$tbrent >= 0) * 1
colnames(istbrentpos) = "istbrentpos"
base = cbind(base, istbrentpos)

# Sauvegarder la base dans un fichier «basefinale.csv» situé dans un repertoir «output»
baseFinale = data.frame(date=index(base), base)
write.table(baseFinale, "output/baseFinale.csv", row.names = F, sep=",")




