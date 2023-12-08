import time
start = time.time()
import re
class AOCDay3P1:

    def __init__(self, file):
        self.INPUT = file

    def openData(self, file):
        with open(file) as readfile:
            return readfile.readlines()
            
    def findAllInts(self, lineString):
        print(list(map(int, re.findall('\d+', lineString))))

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
        return left, right

    def searchAroundOneChar(self, a, charNumber, lineNumber):
        speChars = "!@#$%^&*()-+?_=,<>/"
        left = charNumber-1
        right = charNumber+1
        up = lineNumber-1
        down = lineNumber+1
        
        if left >= 0 and a[lineNumber][left] in speChars :
            return True
        if right < len(a[lineNumber]) and a[lineNumber][right] in speChars:
            return True
        if up >= 0 and a[up][charNumber] in speChars:
            return True
        if down < len(a) and a[down][charNumber] in speChars:
            return True
        if up >= 0 and left >= 0 and a[up][left] in speChars:
            return True
        if right < len(a[lineNumber]) and up >= 0 and a[up][right] in speChars: 
            return True
        if down < len(a) and left >= 0 and a[down][left] in speChars:
            return True
        if down < len(a) and right < len(a[lineNumber]) and a[down][right] in speChars:
            return True
        return False

    def combineDigit(self, left, right, lineString):
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
            for charNumber, char in enumerate(lineString):
                if a[lineNumber][charNumber].isdigit():
                    #check if the surrounding digits are surrounded by special characters
                    if self.searchAroundOneChar(a, charNumber, lineNumber):
                        #find the surrounding digits
                        left, right = self.surroundInts(lineString, charNumber)
                        #if they are, return the sum of the surrounding digits
                        if (left != storedLeft or right != storedRight):
                            storedLeft = left
                            storedRight = right
                            temp = self.combineDigit(left, right, lineString)
                            sum += temp
            
        return sum
                        
                        
                    
                    

if __name__ == '__main__':
    output = AOCDay3P1(file = "/Users/davidyang438/AdventOfCode 2023 Python/Day3/Day3input.txt")
    print(output.solveQuestion())
    print(time.time()-start)