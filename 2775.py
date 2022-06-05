def k_n_num(k,n):
    apt=list(range(1,n+1))
    for i in range(1,k+1):
        apt2=list(apt)
        for j in range(n):
            apt[j]=sum(apt2[:j+1])
    print(apt[n-1])


aa=input("insert k,n \n")
aa=aa.split()
k1=int(aa[0])
n1=int(aa[1])

k_n_num(k1,n1)



