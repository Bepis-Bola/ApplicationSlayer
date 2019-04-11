def binarySearch(data, value):
    low = 0
    high = len(data) - 1
    mid = -1
    index = -1
    while index == -1 and not mid == high:
        mid = (low + high)//2
        if data[mid] < value:
            low = mid + 1
        elif data[mid] > value:
            high = mid - 1
        else:
            index = mid
    return index

import random
data = []
for x in range(100):
    data.append(random.randint(0,100))
data = sorted(data)
binarySearch(data, 5)