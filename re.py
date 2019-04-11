def createHashTable(length):
    data = []
    for x in range(length):
        data.append(None)
    return data
def getIndex(key, length):
    total = 0
    for x in key:
        total += ord(x)
    return total % length
def addValue(table, value):
    table[getIndex(value, len(table))] = value
    return
data = createHashTable(10)
addValue(data, "Ree")
print(data[getIndex("Ree, len(data")])