def newLine():
  print()

print("FirstLine") 
newLine()
print("SecondLine")
quotient = 7/3
print(quotient)
remainder = 7%3
print(remainder)
remainder = 9%3
print(remainder)
x=-1
if 0 < x:
  if x < 10:
    print ("x is a positive single digit")  
    
import math 
x=2
def printLogarithm(x):
    if x <= 0:
        print ("Positive number only,please")
        return 
result = math.log(x) 
print("The log of x is", result)           
def countdown(n):
    if n==0:
        print("Blastoff!")
    else:
        print (n) 
        countdown(n-1)
countdown(4)
newLine()   
def threeLines():   
     newLine()
     newLine()
     newLine()

threeLines()

def nLines(n):
    if n > 0:
        print()
        nLines(n-1) 

nLines(6)

def recurse():
    recurse()

recurse()
name = raw_input("What is your name?")
print (input)

import math 

def cube(num):
    print("code")
    return num**3
    
print(cube(3))
