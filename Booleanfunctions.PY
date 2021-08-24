def isDivisible(x,y):
    if x%y == 0:
        return True
    else:
        return False
        
def factorial(n):
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result = n * recurse
        return result

factorial(3)
 
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(0)
def countdown(n):
  while n>0:
    print (n)
    n=n-1
  print ("Blastoff")

countdown(1000)

def sequence(n):
  while n!=1:
    print (n),
    if n%2 ==0:
        n=n/2
    else:
        n=n*3+1

sequence(2)    

x= 1.0
while x < 100.0:
  print(x,'\t', math.log(x)/math.log(2.0))
  x = x*2.0
print('\t'"produces"'\n''\t'" "'\t'"this"'\n''\t'" ""\t""\t""output")

i = 1
while i <= 6:
  print (2*i,end='   ')
  i = i+1
  

def printMultiples(n,high):
  i=1
  while i <=high:
    print (n*i,end="   ",)
    i=i+1
  print()

       

def printMultTable(high):
  i = 1
  while i <= high:
    printMultiples(i,i)
    i=i+1

printMultTable(10)





