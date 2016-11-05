import random
import string

found = False
test = ''
possString = string.digits
#possString += string.digits
poss = []
password = ''
for i in range(len(possString)): #Turn possible into list
    poss += possString[i] 

for i in range(random.randint(5, 7)): #Length of password
    password += random.choice(poss) #Choose characters of password

iterations = 10000000
while i < iterations:
    i += 1
    test = ''
    for j in range(random.randint(5, 7)):
        test += random.choice(poss)
    test = str(test)
    
    if test == password:
        print ("Found!")
        break
else:
    print ("Not found!")

print (password)
print (test)