num=int(input("insert number of subjects"))
aa=list()
for i in range(num):
    a1=int(input("insert %d st score\n" % (i+1)))
    aa.append(a1)

bb=max(aa)
for i in range(len(aa)):
    aa[i]=aa[i]/bb*100

print(sum(aa)/len(aa))
