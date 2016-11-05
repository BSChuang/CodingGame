import string

allChar = []
encrpyted = ''
unencrypted = ''
for i in range (len(string.printable)): #Turn possible into list
    allChar += string.printable[i]

string = 'Yeah I wonder what this means'
for i in range (len(string)):
    switched = allChar[len(allChar) - allChar.index(string[i])]
    encrpyted += switched
print (encrpyted)



for i in range (len(encrpyted)):
    switched = allChar[len(allChar) - allChar.index(encrpyted[i])]
    unencrypted += switched
print (unencrypted)