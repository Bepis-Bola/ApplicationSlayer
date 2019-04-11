s = [1,4,2,3,5,4,5,6,7,8,1,3,4,5,9,10,11,42]
range = 0
maxrun = -1
rl = {}
for x in s:
    run = rl[x] = rl.get(x-1, 0) + 1
    # print (x-run+1, 'to', x)
    if x - x-run+1 > range:
        range = x - x-run+1
print (range)