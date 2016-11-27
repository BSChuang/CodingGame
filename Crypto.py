import string 
chars = list(string.ascii_uppercase)
#1 - Rectangle
#2 - Pentagon
#3 - 
#4 - prism
#5 - parallel
word = 'VDKBNLD SN SGD RBGNNK BNCD BGZKKDMFD DMSDQ SGD VNQC QDBSZMFKD ZR XNTQ EHQRS OZRRVNQC'
shiftInt = 1
decrypted = ''
for i in range (len(word)):
    if word[i] == ' ':
        decrypted += ' '
        continue
    shifted = chars.index(word[i]) + shiftInt
    decrypted += chars[shifted % 26]
    print(decrypted)
print(decrypted)

'regul'