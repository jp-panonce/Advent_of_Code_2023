import re

def isItPossible(inp_str):

    bag_contents = {
        "red":12,
        "green":13,
        "blue":14
    }

    bag_values = {
        "red": [],
        "green": [],
        "blue":[]
    }

    gameNum = int(re.search('Game (.*):',inp_str).group(1))
    gameS = (inp_str.split(":")[1]).split(";")
    
    possible = True
    for st in gameS:
        print(">>",st)
        # print("== ",re.search(r'\d+(?=\sred)',st).group():)

        
        for clr in ["red","green","blue"]:
            if re.search('\\d+(?=\\s' + clr + ')',st):

                val = int(re.search('\d+(?=\s' + clr + ')',st).group())

                print("    = ", clr, " - ",val)
                bag_values[clr].append(val)
    
    powerToReturn = max(bag_values["red"]) * max(bag_values["green"]) * max(bag_values["blue"])

    
    print("TO RETURN:",powerToReturn)
    return powerToReturn
    
    # for clr in ["red","green","blue"]:

    #     bag_minmax[whereGetPower][clr]

    
    


# Read from input file
file = open("D02\AOC_D02_input_file.txt", "r")
content = file.read()
input_txt = content.split("\n")
file.close()

# iterate each line
sum = 0
for game_str in input_txt:
    sum += isItPossible(game_str)




print(sum)
