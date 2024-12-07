import re

print("Day5 challenge 1/2: start")


update = []

# Open and read the file
with open("input.txt", "r") as file:
    for line in file:
        update.append(line.strip().split(','))

        #update = file.readlines()
#update = [line.strip() for line in update]

rules = {}
#Read rules
with open("inputrules.txt", "r") as file:
        for line in file:
            bonka = line.strip().split('|')
            if bonka[0] in rules:
                rules[bonka[0]].append(bonka[1])
            else:
                rules[bonka[0]] = [bonka[1]]


correctUpdates = []

for updateRow in update:
    talSomVarit = []
    stop = False
    for updateRowIndex in updateRow:
        if stop:
            break
        if updateRowIndex in rules:
            rulesForIndex = rules[updateRowIndex]
            #Check if previous numbers is in the ruleset
            for num in rulesForIndex:
                if num in talSomVarit:
                    stop = True
                    break
        talSomVarit.append(updateRowIndex)
    if not stop:
        correctUpdates.append(updateRow)

print(correctUpdates)

total = 0

for list in correctUpdates:
    middle_index = len(list) // 2
    middle_value = list[middle_index]
    total += int(middle_value)

print(total)