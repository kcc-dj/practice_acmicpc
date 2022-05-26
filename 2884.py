def alarm(h,m):
    if m>=45:
        print(h,":",m-45)
    else:
        if not h:
            print(23,":",m+15)
        else:
            print(h-1,":",m+15)

aa=int(input("insert hour"))
bb=int(input("insert minute"))
alarm(aa,bb)

