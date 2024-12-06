sum = 0
list1 = []
mp = {}

with open("input", "r") as file:
    for line in file:
        temp = line.split(" ")
        list1.append(int(temp[0]))
        tempVal = int(temp[3].split("\n")[0])
        if tempVal in mp:
            mp[tempVal] += 1
        else:
            mp[tempVal] = 1

list1.sort()
for i in range(len(list1)):
    val = list1[i]
    if val in mp:
        sum += val * mp[val]
print(sum)
