fruit="bananaa"
letter=fruit[1]
print(letter)
letter=fruit[0]
print(letter)
phrase="completelyunderstanding"
letter=phrase[16]
print(letter)
len(phraseR)
length=len(phrase)
last=phrase[length]
print(last)
fruit="banana"
length=len(fruit)
last=fruit[-5]
print(last)               
index=0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index=index + 1


fruit="banana"
for char in fruit:
  print (char)

prefixes ="JKLMNOPQ"
suffix ="ack"
for letter in prefixes:
  print(letter+suffix)

word="phraser"
len(word)
length=len(word)
last=word[length-1]
print(last)


word="phraser"
index=0
while index < len(word):
  letter = word[index]
  print (letter)
  index = index + 1

s="Peter, paul, and Mary"
print(s[2:4])
print(s[:])

#exercise on for loop
prefixes ="JKLMNOPQ"
suffix ="ack"
suffixes ="uack"
for letter in prefixes:
  if letter=="O" or letter=="Q":
    print(letter+suffixes)
  else:
    print(letter+suffix)

#exercise on traversal
word ="phraser"
index=-1
while len(word) > index :
  letter = word[index]
  print (letter)
  index = index-1


word ="phraser"
for letter in word[::-1]:
    print(letter)

word="banana"
if word=="banana":
  print("Yes, we have no bananas!")

word="avery"
if word < "banana":
  print ("Your word," + word + ", comes before banana.")
elif word > "banana":
  print("Your word,"+ word +", comes after banana.")
else:
  print("Yes, we have no bananas!")

greeting="Hello World!"
newGreeting ='J' + greeting[1:]
print (newGreeting)

def find(str, ch, n ):
  index = 0
  while index < len(str):
    if str[index]== ch:
      return index
    index = index + 1
  return -1

find("completec", "c",2)

fruit ="banana"
count = 0
for char in fruit:
  if char =='a':
    count = count + 1
print (count)
 
# exercise on count
def countLetters(str,ch):
  count = 0
  for char in str:
    if char ==ch:
     count = count + 1
  print(count) 

countLetters("complete", "e")

fruit = "banana"
index=str.find(fruit,"na")
print(index)

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
 
def isLower(ch):
  return str.find(str.lower,ch) !=-1

isLower("O")

def isLower(ch):
  return ch in string.ascii_lowercase

isLower("e")

print(string.whitespace)

