print("Day1 challenge 2/2: start")

leftlist = []
rightlist = []

with open("input.txt", "r") as file:
    for line in file:
        linesplit = line.split()
        leftlist.append(int(linesplit[0]))
        rightlist.append(int(linesplit[1]))

totalSum = 0

rightMap = {}
#Check how many times a number is represented in right list
for key in rightlist:
    if key in rightMap:
        rightMap[key] += 1
    else:
        rightMap[key] = 1

#Check how many times a left entry appears in right list
for leftEntry in leftlist:
    if leftEntry in rightMap:
        antalIRight = rightMap[leftEntry]
        totalSum += leftEntry * antalIRight

print("Total distance is: " + str(totalSum))
