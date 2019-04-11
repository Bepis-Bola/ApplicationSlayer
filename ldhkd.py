yeet = [4,5,6,7,0,1,2]
target = 3
ree = False
for i in range(len(yeet)):
    if yeet[i] == target:
        print (i)
        ree = True
    if i == len(yeet)-1:
        if ree == False:
            print(-1)