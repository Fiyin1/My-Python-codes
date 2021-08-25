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

prefixes ="JKLMNOPQ"
suffix ="ack"
suffixes ="uack"
for letter in prefixes:
  if letter=="O" or letter=="Q":
    print(letter+suffixes)
  else:
    print(letter+suffix)


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