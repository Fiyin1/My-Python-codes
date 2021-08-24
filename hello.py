from newline import nLines


msg="Hello world"
print(msg)
x=int(input("type in a number:"))
y=int(input("type in another number:"))
print(x+y)
def area(radius):
    return math.pi * radius**2
 

area(2)
def absoluteValue(x):
    if x<0:
        return -x
    elif x>0:
        return x
        print("ABSOLUTE Value")
print(absoluteValue(2))
def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    elif x<y:
        return -1

compare(4,3) 
import math
def distance(x1,y1,x2,y2):
  dx = x2 - x1
  dy = y2 - y1
  dsquared = dx**2 + dy**2
  result=math.sqrt(dsquared)
  return result

radius=distance(1,2,4,6)
print(radius)