aa=input("insert word \n")

aa=aa.upper()
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bb=list()
for i in alpha:
    bb.append(i)

cc=[3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10]

dd=dict(zip(bb,cc))

time_sum=0
for i in aa:
    time_sum+=dd[i]

print(time_sum)

