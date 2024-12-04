import re

print("Day3 challenge 1/2: start")

total = 0

#Read from file
with open("input.txt", "r") as file:
    content = file.read()

#Look for mul(x,y) in string
pattern = r"(mul\(\d*,\d*\))"  # Define the substrings or patterns to find
matches = re.findall(pattern, content)

numberpattern = r"(\d*,\d*)"

for value in matches:
    #String looks like mul(x,y)
    splitnumbers = re.findall(numberpattern, value)[0].split(',')
    print(splitnumbers)  #['x,y']
    total += int(splitnumbers[0]) * int(splitnumbers[1])

print(total)
