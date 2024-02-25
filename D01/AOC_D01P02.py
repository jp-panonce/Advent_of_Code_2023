import re

def getCalibrationValue(inp):

    digits_list = ["one","two","three","four","five","six","seven","eight","nine"]

    numsFromSTR = re.findall(
        '(?=(\d|' + "|".join(digits_list) + "))",
        inp,
        re.IGNORECASE
    )

    print(numsFromSTR)

    for n,x in enumerate(numsFromSTR):
        if(x.lower() in digits_list):
            numsFromSTR[n] = str(digits_list.index(x.lower()) + 1)
    
    print(inp," >> " + numsFromSTR[0] + "|" + numsFromSTR[-1])
    return int(numsFromSTR[0] +""+ numsFromSTR[-1])


# Read from input file
file = open("AOC_D01_input_file.txt", "r")
content = file.read()
input_txt = content.split("\n")
file.close()

# iterate each line
sum = 0
for input_str in input_txt:
    sum += getCalibrationValue(input_str)




print(sum)
