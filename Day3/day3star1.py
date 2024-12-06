from functools import reduce
import operator




with open("input", "r", encoding="utf-8") as file:
    state = 0
    five = [] 
    seven = []


    sum = 0
    for line in file:
        for char in line:
            if state == 0 and char == "m":
                state = 1
            elif (state == 1 and char == "u"):
                state = 2
            elif (state == 2 and char == "l"):
                state = 3
            elif (state == 3 and char == "("):
                state = 4
            elif (state == 4 and char.isdigit() and len(five) < 3):
                five.append(char)
            elif (state == 4 and char == ","):
                state = 5
            elif (state == 5 and char.isdigit() and len(seven) < 3):
                seven.append(char)
            elif (state == 5 and char == ")"):
                state = 0
                res1 = "".join(five)
                res2 = "".join(seven)
                sum += int(res1) * int(res2)
                five = []
                seven = []
            else:
                five = []
                seven = []
                state = 0

print(sum)


                
            