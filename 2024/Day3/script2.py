import re

print("Day3 challenge 2/2: start")

total = 0

#Read from file
with open("input.txt", "r") as file:
    content = file.read()

doDontPattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

matches = re.findall(doDontPattern, content)
print(matches)

numberpattern = r"(\d*,\d*)"
enabled = True
for value in matches:
    if value == 'do()':
        #enabled
        enabled = True
    elif value == 'don\'t()':
        enabled = False
    else:
        if enabled == True:
            print(value)
            #String looks like mul(x,y)
            splitnumbers = re.findall(numberpattern, value)[0].split(',')
            # print(splitnumbers)  #['x,y']
            total += int(splitnumbers[0]) * int(splitnumbers[1])


print(total)
