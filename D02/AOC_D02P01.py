import re

def isItPossible(inp_str):

    bag_contents = {
        "red":12,
        "green":13,
        "blue":14
    }



    gameNum = int(re.search('Game (.*):',inp_str).group(1))
    gameS = (inp_str.split(":")[1]).split(";")
    
    for st in gameS:
        print(">>",st)
        # print("== ",re.search(r'\d+(?=\sred)',st).group():)

        
        for clr in ["red","green","blue"]:
            if re.search('\d+(?=\s' + st + ')',st):
                if re.search('\d+(?=\s' + st + ')',st).group() > bag_contents[clr]:
                    return 0

    return gameNum


# Read from input file
file = open("D02\AOC_D02_input_file_test.txt", "r")
content = file.read()
input_txt = content.split("\n")
file.close()

# iterate each line
sum = 0
for game_str in input_txt:
    sum += isItPossible(game_str)




print(sum)
