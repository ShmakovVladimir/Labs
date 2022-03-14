data = open('labaData.txt')
f = open('table.txt','w')
counter = 1
for row in data:
    i = 0
    while i<=8:
        f.write(str(int(row.split()[i])+int(row.split()[i+1]))+'   ')
        i+=2
    if counter%2 == 0:
        f.write('\n')
        f.write('\n')
    counter+=1

        