from typing import List


range(1, 10, 2)

vocabulary=["ameliorate", "castigate", "defenestrate"]
numbers=[17,123]
empty=[]
print(vocabulary, numbers, empty)

numbers[1]=5
print (numbers[1])

numbers[3-2]
numbers[1.0]

numbers[-1]

numbers[-2]

horsemen = ["war", "famine", "pestilence", "death"]

i = 0
while i < 4:
  print (horsemen [i])
  i = i+1 


i = -1
while 4 > i:
  print (horsemen [i])
  i = i-1 


i = 0
while i < len(horsemen):
  print (horsemen [i])
  i = i+1 

horsemen = ['war','famine','pestilence','death']
"pestilence" in horsemen
'debauchery' in horsemen

'debauchery' not in horsemen

for  horsemen in horsemen:
  print (horsemen)

for number in range(20):
  if number % 2 ==0:
    print(number)

for fruit in ["banana","apple", "quince"]:
  print ("I like to eat " + fruit + "s!") 

a=[1,2,3]
b=[4,5,6]
c= a+b
print(c)

[0]*4

[1,2,3]*5

list = ['a','b','c','d','e','f']
list[1:3]
list[:4]
list[3:]
list[:]

fruit = ['banana','apple','quince']

fruit[0]='pear'
fruit[-1]='orange'
print(fruit)

list = ['a','b','c','d','e','f']
list[1:3]=['x','y']
print (list)

list = ['a','b','c','d','e','f']
list[1:3] = []
print(list)

list = ['a','d','f']
list[1:1] = ['b','c']
print(list)

list[4:4] = ['e']
print(list)

a= ['one', 'two', 'three']
del a[1]
print(a)

list=['a','b','c','d','e','f']
del list[1:5]
print (list)