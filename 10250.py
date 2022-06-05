aa=input("insert H, W, N \n")

aa=aa.split()
H=int(aa[0])
W=int(aa[1])
N=int(aa[2])

if not N//H:
    if H<10:
        print("%d01"% (N%H))
    else:
        print("%d1" % (N%H))
else:
    if N//H<10:
        print("%d0%d" % (N%H,N//H +1))
    else:
        print("%d%d" % (N%H,N//H +1))
