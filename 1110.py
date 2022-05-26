num=int(input("insert one integer which 0 to 99"))
aa=num
cy=0
while True:
    if num<10:
        num = num*11
    else:
        num=(num%10)*10 + (num//10 + num%10)%10

    cy+=1
    if num==aa:
        print(cy,"cycle")
        break

