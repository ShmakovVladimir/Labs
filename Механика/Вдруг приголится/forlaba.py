data = open('labaData.txt')
import matplotlib.pyplot as plt
fourtySec = []
cells = []
cellsTicks = []
cY = []
i=0
while i<1000:
    cY.append(i/1000)
    i+=5
for row in data:
    i = 0
    while i<=8:
        fourtySec.append(int(row.split()[i])+int(row.split()[i+1]))

        i+=2
plt.style.use('fivethirtyeight')
proportion = []
for i in range(35,81):
    proportion.append(fourtySec.count(i)/len(fourtySec))
    print(str(i)+'  '+str(fourtySec.count(i)/len(fourtySec)))
    cells.append(i+0.5)
    cellsTicks.append(i)
#print(fourtySec)
#plt.hist(fourtySec,cells,histtype='step')
plt.xticks(cellsTicks)
plt.yticks(cY)
plt.xlabel("N")
plt.ylabel("W")
plt.step(cells,proportion)
plt.show()