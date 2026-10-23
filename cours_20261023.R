library(dplyr)

a = 1
a <- 1
class("test")
class(1)
class(TRUE)
class(T)
class(NULL)

myvec = c("a","b",3)
print("Hello")

print( paste("Hello", a) )
print( paste("Hello", a, sep="") )
print( paste0("Hello", a) )

b = 3
sprintf("Ceci est la valeur de a : %s et la valeur de b est : %s", a, b)
paste("Ceci est la valeur de a" , a , " et la valeur de b est :" , b)


for( i in 1:10 ) {
  print(i)
}


a = 1
while( a < 10) {
  print(a)
  a = a + 1
}

a = 3
if( a > 10 ){
  print("a > 10")
} else if( a < 5){
  print("a < 5")
} else {
  print(" a n'est pas > 10 ni < 5")
}


vec = c(0, 1)
vec = c(vec, 2)


######## Exercices
################################

# 1 - Vérifier si un nombre est premier ou pas. Pour savoir si un nombre est divisible par un autre, utilisez le modulo (% en Python)

a = 10
isPrime = TRUE
for( i in 2:(a-1)){
  if( a %% i == 0){
    print(sprintf("%s n'est pas premier, il est divisible par %s",a,i))
    isPrime = FALSE
    break
  }
}

if (isPrime) {
  print( sprintf("%s est premier !", a) )
} else {
  print( sprintf("%s n'est pas premier", a) )
}

# 2 - Les deux premiers termes de la suite de Fibonacci sont tous deux un. Les termes suivants de la séquence sont trouvés en additionnant les deux termes immédiatement précédents. Écrivez un code qui écrit les n termes de la séquence de Fibonacci pour tout n≥3. Initialisez une liste [1,1] et incrementez cette liste 

n = 45
listFibo = c(1, 1)
for(i in 1:n) {
  newVal = listFibo[length(listFibo)] + listFibo[length(listFibo)-1]
  listFibo = c(listFibo, newVal)
}
print(listFibo)
for (i in listFibo){
  print(i)
}

# 3 - Écrivez un code qui simule le lancer d'une pièce avec une probabilité p associée aux piles,  jusqu’à obtenir fâce, et renvoie le nombre de piles obtenues. Ensuite, reproduisez l’exécution de ce code 100 fois et afficher le nombre maximum de piles obtenus lors d’une même séquence. 

p = 0.5
maxNbPiles = 0
for (i in 1:100) {
  nbPiles = 0
  while (runif(1) <= p){
    nbPiles = nbPiles + 1
  }
  if (nbPiles > maxNbPiles){
    maxNbPiles = nbPiles
  }
}
sprintf("Le maximum de pile obtenu sur 100 lancers est : %s",maxNbPiles)



fonction_test <- function(a, b=10) {
  print(a)
  print(b)
  res <- a + b
  return(res)
}

test = fonction_test(a=10, b = 19)



