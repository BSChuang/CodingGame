string = 'Hello how are you?'

for i in range(len(string)):
    print (string[0:i])

for i in range(len(string)):
    print (string[0:len(string) - i])

print (' ')

for i in range(len(string)):
    print (string[0:i] + ' ' + string[i:len(string)])

for i in range(len(string)):
    print (string[0:len(string) - i] + ' ' + string[len(string) - i:len(string)])

for i in range(len(string)):
    print (string[0:i] + ' ' + string[len(string) - i:len(string)])

for i in range(len(string)):
    print (string[0:len(string) - i] + ' ' + string[i:len(string)])

