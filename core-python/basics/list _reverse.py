l=['4','5','3','2','4','5','6','2']

for i in range(0,len(l)):
    for j in range(i+1, len(l)):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)

n ='kjhg'
nn=n[::-1]
print(nn)

