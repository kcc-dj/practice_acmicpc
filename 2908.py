aa = input("insert two numbers \n")

bb=aa.split()
cc=list()
for i in bb:
    cc.append(int(i[::-1]))
    
print(max(cc))
        

