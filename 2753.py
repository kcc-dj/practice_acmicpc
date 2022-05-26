def yoon_nyeon(aa):
    if not aa % 400:
        print(1)
    elif not aa%4 and aa%100:
        print(1)
    else:
        print(0)


bb=int(input("insert years"))
yoon_nyeon(bb)

