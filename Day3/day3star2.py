from functools import reduce
import operator




with open("input", "r", encoding="utf-8") as file:
    state = 0
    five = [] 
    seven = []
    enable = True


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
                if enable:
                    sum += int(res1) * int(res2)
                five = []
                seven = []
            elif (char == "d"):
                state = 10
            elif (char == "o" and state == 10):
                state = 11
            elif (state == 11 and char == "("):
                state = 12
            elif (state == 12 and char == ")"):
                enable = True
                state = 0
            elif (state == 11 and char == "n"):
                state = 13
            elif (state == 13 and char == "'"):
                state = 14
            elif (state == 14 and char == "t"):
                state = 15
            elif (state == 15 and char == "("):
                state = 16
            elif (state == 16 and char == ")"):
                enable = False
                state = 0
            else:
                five = []
                seven = []
                state = 0

print(sum)


                
            