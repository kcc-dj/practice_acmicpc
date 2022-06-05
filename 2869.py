import math

aa=input("insert A, B, V \n")
aa=aa.split()
A=int(aa[0])
B=int(aa[1])
V=int(aa[2])


X=(V-B)/(A-B)
print(math.ceil(X))
