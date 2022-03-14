a,b,c = 0.105,0.105,0.145
s = 331
freq = []
def cn(num,length):
    return (num/length)**2
for m in range(4):
    for n in range(4):
        for p in range(4):
            fr = ((cn(m,a)+cn(n,b)+cn(p,c))**.5)*(s/2)
            freq.append([fr,m,n,p])
freq.sort()
for i in freq:
    print(str(i[0])+" +/- "+str(i[0]/100)+'m:'+str(i[1])+'n:'+str(i[2])+'p:'+str(i[3]))