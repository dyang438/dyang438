"""import re

with open("/Users/davidyang438/VSCode Python/AdventOfCodeDay1P1.py") as readfile:
    a = readfile.read().strip()
    print(a)

def calibration(a):
    ls = a.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)

# Part 2
a = (
    a.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)
print(calibration(a))"""

with open("/Users/davidyang438/VSCode Python/Day1P1input.txt", "r") as readfile:
    sum = 0;
    a = readfile.readlines()
    numArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    count = 0
    for input in a:
        input = (
            input.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
        )
        k = 0
        front = True
        returnNum = ""
        tempBack = ""
        count += 1
        print(len(input))
        while k < len(input):            
            if (input[k] in numArr) and front:
                returnNum = input[k]
                tempBack = input[k]
                front = False
            elif (input[k] in numArr) and (not front):
                tempBack = input[k]
            if k == len(input)-1:
                if input[k] in numArr:
                    tempBack = input[k]
                returnNum += tempBack
                sum += int(returnNum)
            k += 1

    print("final sum is: " + str(sum))