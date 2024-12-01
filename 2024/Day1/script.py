print("Day1 challenge 1/2: start")

leftlist = []
rightlist = []

with open("input.txt", "r") as file:
    for line in file:
        linesplit = line.split()
        leftlist.append(int(linesplit[0]))
        rightlist.append(int(linesplit[1]))

#Sort the lists in ascending order
leftlist.sort()
rightlist.sort()

totalSum = 0

for index, value in enumerate(leftlist):
    hej = abs(value - rightlist[index])
    print(str(value) + " " + str(rightlist[index]) + " " + str(hej))
    totalSum = totalSum + hej

print("Total distance is: " + str(totalSum))
