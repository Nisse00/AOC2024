sum = 0
list1 = []
list2 = []

with open("input", "r") as file:
    for line in file:
        temp = line.split(" ")
        list1.append(int(temp[0]))
        list2.append(int(temp[3].split("\n")[0]))

list1.sort()
list2.sort()
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])
print(sum)
