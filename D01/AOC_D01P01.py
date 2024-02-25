import re

def getCalibrationValue(inp):

    numsFromSTR = re.findall(
        '\d+',
        inp
    )
    print(inp," >> " + numsFromSTR[0] + "|" + numsFromSTR[-1])
    return int(numsFromSTR[0] +""+ numsFromSTR[-1])


# Read from input file
file = open("AOC_D01_input_file_test.txt", "r")
content = file.read()
input_txt = content.split("\n")
file.close()

# iterate each line
sum = 0
for input_str in input_txt:
    sum += getCalibrationValue(input_str)




print(sum)
