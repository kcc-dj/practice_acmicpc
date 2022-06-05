aa=int(input("insert number \n"))

i=1
while True:
    aa-=i
    if aa<0:
        aa+=i
        if aa==1:
            if i%2:
                print('%d/1' % i)
            else:
                print('1/%d' % i)
        else:
            if i%2:
                print('%d/%d' % (i-aa+1,aa))
            else:
                print('%d/%d' % (i+aa-1,i+1-aa))

        break

    elif aa==0:
        if i%2:
            print('1/%d' % i)
        else:
            print('%d/1' % i)
        break

    else: i+=1





