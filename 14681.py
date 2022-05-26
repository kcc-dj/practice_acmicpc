def quadrant_n(x,y):
    if x>0:
        if y>0:
            print("quadrant 1")
        else:
            print("quadrant 4")
    else:
        if y>0:
            print("quadrant 2")
        else:
            print("quadrant 3")

aa=int(input("insert x"))
bb=int(input("insert y"))
quadrant_n(aa,bb)
