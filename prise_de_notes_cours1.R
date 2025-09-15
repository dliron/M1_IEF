
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
