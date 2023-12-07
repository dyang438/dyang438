with open("/Users/davidyang438/VSCode Python/Day1P1input.txt", "r") as readfile:
    sum = 0;
    a = readfile.readlines()
    numArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    count = 0
    for input in a:
        if count > 1: print("input ------- " + input)
        k = 0
        front = True
        returnNum = ""
        tempBack = ""
        count += 1
        print(len(input))
        while k < len(input):
            print("digit: " + input[k])
            
            if (input[k] in numArr) and front:
                returnNum = input[k]
                tempBack = input[k]
                front = False
                if count == len(a): print("returnNum ------- " + returnNum)
            elif (input[k] in numArr) and (not front):
                tempBack = input[k]
                if count == len(a): print("tempBack ------- " + tempBack)
            if k == len(input)-1:
                if count == len(a): print("returnNum ------- " + returnNum)
                if input[k] in numArr:
                    tempBack = input[k]
                returnNum += tempBack
                sum += int(returnNum)
            k += 1

    print("final sum is: " + str(sum))
