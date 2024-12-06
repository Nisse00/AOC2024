



safe = 0

with open("input", "r") as file:
    for line in file:
        flag = False
        temp = line.split(" ")
        last = temp[0]
        if int(temp[0]) > int(temp[1]):
            decreasing = True
        else:
            decreasing = False
        for i, nbr in enumerate(temp):
            nbr = int(nbr)
            last = int(last)
            if i != 0:
                if decreasing:
                    if nbr > last or last - nbr > 3 or last - nbr == 0:
                        flag = True
                        break
                    else:
                        last = nbr
                else:
                    if nbr < last or nbr - last > 3 or nbr - last == 0:
                        flag = True
                        break
                    else:
                        last = nbr
        print(temp, flag)
        if not flag:
            safe += 1
print(safe)