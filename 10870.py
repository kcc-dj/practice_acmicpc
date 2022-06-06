aa=int(input("insert number \n"))

def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibo(num-2)+fibo(num-1)

print(fibo(aa))
