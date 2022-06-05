aa=int(input("insert N\n"))

bb=list()
for i in range(aa//5 +1):
    for j in range(aa//3 +1):
        if 5*i+j*3==aa:
            bb.append(i+j)

if not len(bb):
    print(-1)
else:
    print(min(bb))

