import random 

def award(a,b,c):
    if a!=b and a !=c:
        print(max(a,b,c)*100,"won")
    elif a==b and a==c:
        print(a*1000+10000,"won")
    else:
        if a==b or a==c:
            print(a*100 + 1000,"won")
        else: 
            print(b*100 + 1000,"won")

a1,b1,c1=input("insert result of three dice").split()

a1=int(a1)
b1=int(b1)
c1=int(c1)
award(a1,b1,c1)
        
