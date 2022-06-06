while True:
    aa=int(input("choose 1 to 8 \n"))
    if aa > 8 or aa < 0:
        print("plz choose 1 to 8")
    else:
        break





def star_shape(num):
    ss=[]
 
    if num==1:
        return ['*']

    stars = star_shape(num//3)
    for i in stars:
        ss.append(i*3)
    for i in stars:
        ss.append(i+(' '*(num//3))+i)
    for i in stars:
        ss.append(i*3)

    return ss

print('\n'.join(star_shape(3**aa)))


