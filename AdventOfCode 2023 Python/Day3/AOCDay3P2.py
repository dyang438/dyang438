import time
start = time.time()
import re
class AOCDay3P1:

    def __init__(self, file):
        self.INPUT = file

    def openData(self, file):
        with open(file) as readfile:
            return readfile.readlines()
            
    #def findAllInts(self, lineString):
    #    print(list(map(int, re.findall('\d+', lineString))))

    def surroundInts(self, lineString, charNumber):
        left = charNumber
        right = charNumber
        while lineString[charNumber-1].isdigit():
            left -= 1
            charNumber -= 1
        charNumber = right
        while lineString[charNumber+1].isdigit():
            right += 1
            charNumber += 1
        print(left, right)
        return left, right

    def solveAroundOneStar(self, a, starNumber, lineNumber):
        print("New Star: ")
        count = 0
        storedLeft = []
        storedRight = []
        storedRows = []
        product = 1
        left = starNumber-1
        right = starNumber+1
        up = lineNumber-1
        down = lineNumber+1
        
        if left >= 0 and a[lineNumber][left].isdigit() :
            print("left")
            tempLeft, tempRight = self.surroundInts(a[lineNumber], left)
            storedLeft.append(tempLeft)
            storedRight.append(tempRight)
            storedRows.append(lineNumber)
            count += 1
        if right < len(a[lineNumber]) and a[lineNumber][right].isdigit():
            tempLeft, tempRight = self.surroundInts(a[lineNumber], right)
            if count == 0 or (tempLeft not in storedLeft or tempRight not in storedRight or lineNumber not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber)
                count += 1
        if up >= 0 and a[up][starNumber].isdigit():
            tempLeft, tempRight = self.surroundInts(a[up], starNumber)
            if count == 0 or (tempLeft not in storedLeft or tempRight not in storedRight or (lineNumber-1) not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber-1)
                count += 1
        if down < len(a) and a[down][starNumber].isdigit():
            print("down")
            tempLeft, tempRight = self.surroundInts(a[down], starNumber)
            if count == 0 or (tempLeft not in storedLeft or tempRight not in storedRight or (lineNumber+1) not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber+1)
                count += 1
        if up >= 0 and left >= 0 and a[up][left].isdigit():
            print("upleft")
            tempLeft, tempRight = self.surroundInts(a[up], left)
            if count == 0 or (tempLeft not in storedLeft or tempRight not in storedRight or (lineNumber-1) not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber-1)
                count += 1
        if right < len(a[lineNumber]) and up >= 0 and a[up][right].isdigit(): 
            print("upright")
            tempLeft, tempRight = self.surroundInts(a[up], right)
            if count == 0 or (tempLeft not in storedLeft or tempRight not in storedRight or (lineNumber-1) not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber-1)
                count += 1
        if down < len(a) and left >= 0 and a[down][left].isdigit():
            print("downleft")
            tempLeft, tempRight = self.surroundInts(a[down], left)
            if count == 0 or (tempLeft not in storedLeft or tempRight not in storedRight or (lineNumber+1) not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber+1)
                count += 1
        if down < len(a) and right < len(a[lineNumber]) and a[down][right].isdigit():
            print("downright")
            tempLeft, tempRight = self.surroundInts(a[down], right)
            if count == 0 or ((tempLeft not in storedLeft or tempRight not in storedRight) or (lineNumber+1) not in storedRows):
                storedLeft.append(tempLeft)
                storedRight.append(tempRight)
                storedRows.append(lineNumber+1)
                count += 1
        print(storedLeft, storedRight, storedRows)
        if count == 2:
            for i in range(0, len(storedLeft)):
                product *= self.combineDigit(storedLeft[i], storedRight[i], a[storedRows[i]])
            return product
        return 0
    

    def combineDigit(self, left, right, lineString):
    
        print("CombineDigit: " + lineString[left:right+1])
        return int(lineString[left:right+1])
        

    def solveQuestion(self):
        a = self.openData(self.INPUT)
        sum = 0
        temp = 0
        counter = 0
        storedLeft = 0
        storedRight = 0
        for lineNumber, lineString in enumerate(a):
            #iterate through each string finding digits
            for starNumber, star in enumerate(lineString):
                if a[lineNumber][starNumber] == "*":
                    #check if the surrounding digits are surrounded by special characters
                    sum += self.solveAroundOneStar(a, starNumber, lineNumber)
            
        return sum
                        
                        
                    
                    

if __name__ == '__main__':
    output = AOCDay3P1(file = "/Users/davidyang438/AdventOfCode 2023 Python/Day3/Day3input.txt")
    print(output.solveQuestion())
    print(time.time()-start)