aa=int(input("insert number \n"))
k=0
n=1

while True:
    n+=6*k
    s=n+6*(k+1)
    if aa>n and aa<=s:
        break
    else:
        k+=1


print(k+2)

