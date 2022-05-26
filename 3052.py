aa=list()
for i in range(10):
    bb=int(input("insert integers \n"))
    aa.append(bb%42)
dd=list()
for i in aa:
    if not i in dd:
        dd.append(i)

print(len(dd))



cc=set(aa)
print(len(cc))

