num = int(input("number of results"))


for i in range(num):
    res=input("%d st result?" % (i+1))
    score=list()
    sco=0
    total=0
    res=res+"X"
    for j in range(len(res)):
        if res[j]=="O":
            sco+=1
            score.append(sco)
        else:
            total+=sum(score)
            score=list()
            sco=0
    print(total)


