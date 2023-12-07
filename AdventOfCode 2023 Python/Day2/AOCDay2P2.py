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
        power = 1;
        powerDictionary = {
            "r": 0,
            "b": 0,
            "g": 0
        }
        
        for partition in partitions:
            numberString = ""
            for num in partition:
                if num.isdigit():
                    numberString += num
            numberContained = int(numberString)
            
            if partition.startswith("Game"):
                id = numberContained
                print(id)
            elif "r" in partition and numberContained > powerDictionary["r"]:
                powerDictionary["r"] = numberContained
            elif "b" in partition and numberContained > powerDictionary["b"]:
                powerDictionary["b"] = numberContained
            elif "g" in partition and numberContained > powerDictionary["g"]:
                powerDictionary["g"] = numberContained
        print(powerDictionary)
        output += powerDictionary["r"] * powerDictionary["b"] * powerDictionary["g"]
        

    print(output)