aa="abcdefghijklmnopqrstuvwxyz"

bb=input("insert word \n")

for i in aa:
    if not i in bb:
        print(-1)
    else:
        print(bb.index(i))

