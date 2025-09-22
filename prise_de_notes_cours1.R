
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





