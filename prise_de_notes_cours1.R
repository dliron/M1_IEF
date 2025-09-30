
b = "Bonjour"
"5"
5

class("5")
class(5.0)

c(1, a, 3)


b = 5
b = b + 2

a = "5"
as.numeric(a) + 2


a
print(a)

print( paste0("La valeur de a est : ", a, " et voila") )
cat("La valeur de a est : ", a, " et voila")
sprintf("La valeur de a est %s et la valeur de b est %s", a, b)

read.csv("input/eia_data.csv", sep = ",")
read.csv("./input/eia_data.csv", sep = ",")


read.csv("../20150218224500.translation.export.CSV", sep = "\t")


TRUE
FALSE
T
class(F)


TRUE & TRUE
TRUE & FALSE
TRUE | FALSE

a = 11
if( a > 10  | a > 20) {
  print("BOnjour")
} else if ( a < 5) {
  print("Enfin")
} else {
  print("Au revoir")
}


for( i in 1:5){
  print("Bonjour")
  print(i)
}

a = 0
while( a < 10){
  print("Bonjour")
  a = a + 1
}



c(1, 1, 2, 3, 5, 8)


runif(1)



# Vérifier si un nombre est premier ou pas. 
# Pour savoir si un nombre est divisible par un autre,
#   utilisez le modulo (%% en R)
a = 100
estpremier = TRUE
for( i in 2:(a-1)) {
  if( a %% i == 0){
    print(sprintf("%s n'est pas un nombre premier car il est divisible pas %s", a, i))
    estpremier = FALSE
    break
  }
}

if( estpremier ){
  print("Le nombre est premier")
} else {
  print("Il est pas premier")
}


monvec = c(1, 1)
monvec = c(monvec, 2)


monvec[3] + monvec[2]
length(monvec)
monvec[length(monvec)]


# Les deux premiers termes de la suite de Fibonacci sont tous deux un. 
# Les termes suivants de la séquence sont trouvés en additionnant les deux termes immédiatement précédents. 
# Écrivez un code qui écrit les n termes de la séquence de Fibonacci pour tout n≥3
nb_fibo = 100
fibo = c(1, 1)
for( i in 1:nb_fibo){
  new_fibo = fibo[length(fibo)] + fibo[length(fibo)-1]
  fibo = c(fibo, new_fibo)
  # fibo[length(fibo)+1] = new_fibo
}
fibo

# Écrivez un code qui simule le lancer d'une pièce avec une 
# probabilité p associée aux piles,  jusqu’à obtenir fâce, 
# et renvoie le nombre de piles obtenues. Ensuite, reproduisez 
# l’exécution de ce code 100 fois et afficher le nombre maximum 
# de piles obtenus lors d’une même séquence. Pour générer une
# probabilité entre 0 et 1, utilisez runif(1).
max_sur_100try = 0
for( i in 1:100){
  max_try = 1
  
  resultat = runif(1)
  while(resultat < 0.5){
    resultat = runif(1)
    max_try = max_try + 1
  }
  
  if(max_try > max_sur_100try){
    max_sur_100try = max_try
  }
  
}
print(max_sur_100try)


myfunction <- function(a, b="valeur de v", c = "valeur de c") {
  print(a)
  print(b)
  print(c)
}


somme2val <- function(a, b) {
  res = a + b
  return(res)
}




func_estpremier <- function(myval) {
  estpremier = TRUE
  for( i in 2:(myval-1)) {
    if( a %% i == 0){
      print(sprintf("%s n'est pas un nombre premier car il est divisible pas %s", a, i))
      estpremier = FALSE
      break
    }
  }
  
  if( estpremier ){
    print("Le nombre est premier")
  } else {
    print("Il est pas premier")
  }
  
  return(estpremier)
}

res_estpremier = func_estpremier(7)




func_fibo <- function(nb_items) {
  fibo = c(1, 1)
  for( i in 1:nb_items){
    new_fibo = fibo[length(fibo)] + fibo[length(fibo)-1]
    fibo = c(fibo, new_fibo)
  }
  return(fibo)
}
res_fibo = func_fibo(nb_items=10)


func_pileface <- function(probap = 0.5, nb_iter = 100) {
  max_sur_100try = 0
  for( i in 1:nb_iter){
    max_try = 1
    
    resultat = runif(1)
    while(resultat < probap){
      resultat = runif(1)
      max_try = max_try + 1
    }
    
    if(max_try > max_sur_100try){
      max_sur_100try = max_try
    }
    
  }
  return(max_sur_100try)
}

func_pileface()
func_pileface(probap = 0.04)
func_pileface(nb_iter=10)
func_pileface(probap = 0.99, nb_iter=1000)




taille  = c(121, 156, NA, 234)
poids    = c(67, 78, 235, 567)
sexe    = c("Homme","Femme","Homme", "homme")

mydata = data.frame(taille = taille, poids = poids, sexe = sexe)
class(mydata)

colnames(mydata)
rownames(mydata)
dim(mydata)
nrow(mydata)
ncol(mydata)
summary(mydata)


mydata[ , ]
mydata[ 2, ]
mydata[ , 3]
mydata[ 1, 3]
mydata[ c(1,4), ]

mydata[ , "poids"]
mydata[ , c("poids","taille")]
mydata["poids"]
mydata$poids

mydata[ mydata$poids >= 100, ]
mydata[ mydata$poids >= 100, "poids"]

data = read.csv("input/eia_data.csv")
brent = read.table('input/brent.csv',sep = ",", header = TRUE)

dim(brent)
dim(data)

res = cbind(data, brent)
res = res[,2:ncol(res)]

brent[,!colnames(brent) %in% c("date")]
colnames(res)


# Créer un DF et transformer une colonne en facteur 
taille   = c(121, 156, 194)
poids  = c(67, 78, 235)
sexe    = c("Homme","Femme","Homme")
mydata = data.frame(taille = taille, poids = poids, sexe = sexe)

mydata$sexe = as.factor(mydata$sexe)

rbind(mydata, c(150, 67, "Femmes"))



apply(data[,2:ncol(data)], 2, function(x) mean(x))
apply(data[,2:ncol(data)], 1, function(x) mean(x))

data["meanCols"] = apply(data[,2:ncol(data)], 1, function(x) mean(x))

library(zoo)
data_ma15 = rollapply(data[,2:ncol(data)], 15, function(x) mean(x))


my_ts = ts(1:100, start = c(1980, 2), frequency = 12)

library(xts)
dates = as.Date(c('2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'))
my_xts <- xts(1:5, order.by = dates)


class(my_ts)
class(my_xts)

window(my_ts, start=c(1984, 10), end=c(1987,4))
my_xts["2024-03-01/"]
head(my_xts)

lag(my_ts, 5)
lag(my_xts, -3)


# Importer les fichiers brent.csv et eia_data.csv depuis le repertoire input et renommer les colonnes
data = read.csv("input/eia_data.csv")
colnames(data) = c("date","cocpopec","copsopec","paprnonopec","papropec","paprrus","paprus","pascoecd","patcchn","patcnonoecd","patcoecd","patcwld")

brent = read.table('input/brent.csv',sep = ",", header = TRUE)
colnames(brent) = c("date","brent")

dateBrent = as.Date(brent$date, format = "%d/%m/%Y")
brent_xts = xts(brent[,-1], order.by = dateBrent)
colnames(brent_xts) = "brent"

dateData = as.Date(data$date, format = "%d/%m/%Y")
data_xts = xts(data[,-1], order.by = dateData)

base_xts = cbind(brent_xts, data_xts)

# Formater «base» en trimestrielle
base_xts_quarterly = apply.quarterly(base_xts, mean) 
dim(base_xts_quarterly)

library(lubridate)
index(base_xts_quarterly) = as.Date(format(index(base_xts_quarterly) - months(2), "%Y-%m-01"))


base_xts_quarterly = data.frame(date=index(base_xts_quarterly), base_xts_quarterly)
write.csv(base_xts_quarterly,"output/baseDL.csv", row.names = FALSE)


# library(magrittr)
# format(index(base_xts_quarterly) - months(2), "%Y-%m-01") %>% as.Date


headers = NULL
if (!is.null(taceconomics.apikey())) {
  headers <- c(headers, list("Authorization"=paste("Bearer", taceconomics.apikey())))
}

library(httr)
url = "https://api.taceconomics.com/data/DS/JPCPACR_R/WLD?api_key=sk_t8LMzhebMQNpwPpH0-s60NTuw4AHAnsfOa35z6zSUHM" 
req = httr::VERB("GET", url)
if( httr::status_code(req) == 200 ) {
  data = httr::content(req, "text", encoding="UTF-8")
  data = jsonlite::fromJSON(data)
  return(data)
}

data$data


