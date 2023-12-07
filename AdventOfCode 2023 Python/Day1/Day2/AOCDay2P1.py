import re
with open ("/Users/davidyang438/AdventOfCode 2023 Python/Day2/Day2input.txt") as readfile:
    
    a = readfile.readlines()
    output = 0

    for i, line in enumerate(a):
        id = 0
        
        line = (
            line.replace(";", "|")
            .replace(" red", "r")
            .replace(" blue", "b")
            .replace(" green", "g")
            .replace(", ", "|")
            .replace(": ", "|")
        )
        partitions = line.split("|")
       
        add = True

        for partition in partitions:
            
            numberString = ""
            for num in partition:
                if num.isdigit():
                    numberString += num
            numberContained = int(numberString)
            
            if partition.startswith("Game"):
                id = numberContained
                print(id)
            elif "r" in partition and numberContained > 12:
                add = False
            elif "b" in partition and numberContained > 14:
                add = False
            elif "g" in partition and numberContained > 13:
                add = False
        print(add)
        if add == True:
            output += (id)
        print("output" + str(output))
    
    print(output)