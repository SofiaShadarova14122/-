#Отрывок пьесы "Горе от ума", Шадарова София 14122
inFile = open('пьеса.txt', 'r')
myDict ={}
i = 1
for line in inFile:
    x = line.split()
    myDict[x[0].strip('. ')] = myDict.get(x[0].strip('. '), '') + str(i) + ') ' + ' '.join(x[1:]) + '\n'
    i += 1
for key,value in myDict.items(): print(key, ':\n', value, sep='')
inFile.close()
