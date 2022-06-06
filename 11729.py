aa=int(input("insert number"))


def hanoi(n,st,en):

    if n==1:
        print(st,en)
        return
    
    hanoi(n-1,st,6-st-en)
    print(st,en)
    hanoi(n-1,6-st-en,en)

print(2**aa -1)
hanoi(aa,1,3)



