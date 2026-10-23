
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

