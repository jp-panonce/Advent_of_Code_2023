import re

#TRIED ANSWERS THAT ARE WRONG:
#  11789 - too low <--- fix: on line 36 below, removed the int(n) and changed to just n. not sure why
#   539713 - CORRECT!!



def getAllPartNums(inp):

    allNums = []
    allSyms = []

    inp_height = len(inp)
    inp_width = len(inp[0])

    # iterate per line
    print("Finding all numbers...")
    for idx, line in enumerate(inp):

        # get all numbers via regex
        allNum = re.findall('\d+',line)
        print(" - on Line ",(idx+1),":",allNum)

        # get all positions of numbers
        st_soFar = 0
        print("   -",allNum)
        for n in allNum:

            # get start & end position of each number
            st = line.find(n,st_soFar)
            nd = st + len(n)
            st_soFar = nd

            #add it to list
            allNums.append([n,idx,st,nd])
            print("    = ",[int(n),idx,st,nd])
        
        # CREATE the symbol_mask which changes all non-symbols and period to '0'
        # replace dots and numerics with zero
        symbol_mask = re.sub(r'\d','.',line)
        symbol_mask = symbol_mask.replace('.','0')
        allSyms.append(symbol_mask)

    #iterate each num
    sm = 0
    for n in allNums:
        print("n | ",n)

        # check if there is a non-zero surrounding said number 
        #based on position
        prev_line_num = None if (n[1] == 0) else (n[1]-1)
        next_line_num = None if (n[1] == inp_height-1) else (n[1] + 1)
        l_limit = n[2] if (n[2] == 0) else (n[2]-1)
        r_limit = n[3] if (n[3] == inp_width-1) else (n[3]+1)

        searchArea_str = ''.join([
            '' if (prev_line_num is None) else allSyms[prev_line_num][l_limit:r_limit], #first line
            allSyms[n[1]][l_limit:r_limit], #2nd line
            '' if (next_line_num is None) else allSyms[next_line_num][l_limit:r_limit], #3rd line
        ])

        
        if len(searchArea_str.replace('0','')) > 0:
            # print("    > Found some")
            sm += int(n[0])
        else:
            print("Finding in >>> ",searchArea_str)
            print("    > Found NONE")

    print("SUM IS ", sm)
    pass

# Read from input file
file = open("D03\AOC_D03_input_file.txt", "r")
content = file.read()
input_txt = content.split("\n")
file.close()

# iterate each line
sum = 0
part_nums = getAllPartNums(input_txt)




print(sum)
