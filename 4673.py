cc=list(range(1,10001))

for i in range(1,10001):
    dn=i
    while True:
        aa=len(str(i))
        dn+=i//(10**(aa-1))
        i=i%(10**(aa-1))
        aa-=1
        if aa==0:
            break
    if dn in cc:
        cc.remove(dn)

print(cc)


