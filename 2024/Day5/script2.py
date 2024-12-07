import re

print("Day5 challenge 1/2: start")


update = []

# Open and read the file
with open("input.txt", "r") as file:
    for line in file:
        update.append(line.strip().split(','))

rules = {}
#Read rules
with open("inputrules.txt", "r") as file:
        for line in file:
            bonka = line.strip().split('|')
            if bonka[0] in rules:
                rules[bonka[0]].append(bonka[1])
            else:
                rules[bonka[0]] = [bonka[1]]

rules2 = {}
with open("inputrules.txt", "r") as file:
    for line in file:
        bonka = line.strip().split('|')
        if bonka[1] in rules2:
            rules2[bonka[1]].append(bonka[0])
        else:
            rules2[bonka[1]] = [bonka[0]]

print(rules2)

incorrectUpdates = []

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
    if stop:
        incorrectUpdates.append(updateRow)


fixedUpdates = []

#incorrect updates
#75,97,47,61,53
#61,13,29
#97,13,75,29,47

for row in incorrectUpdates:
    correctedRow = []
    index = 0  # Start index
    while index < len(row):
        updateRowNumber = row[index]
        print(row)

        if updateRowNumber in rules2:  # if key in map
            rulesForIndex = rules2[updateRowNumber]
            print("Curr row: " + updateRowNumber)
        # '53': ['47', '75', '61', '97'],
        # '13': ['97', '61', '29', '47', '75', '53'],
        # '61': ['97', '47', '75'],
        # '47': ['97', '75'],
        # '29': ['75', '97', '53', '61', '47'],
        # '75': ['97']
        # 75,97,47,61,53 - börja med 75 och kolla rules. Finns någon av de bakom i listan?
        # 97,47,61,53,75
        # 47,61,53,75
        # 61,53,75,47
        # 53,75,47,61
        # 75,47,61,53
        # 47,61,53
        # 61,53
        # 97, 75, 47,61,53 end result

            sublist = row[index + 1:]
            print("sublist " + str(sublist))
            # for num in row[1:]:
            common_exists = any(item in rulesForIndex for item in sublist)
            # check if the numbers after in the row is ok
            if common_exists:  # ex 97 finns i lista før 75
                print("common exists for " + str(rulesForIndex) + " " + str(sublist))
                row.remove(updateRowNumber)
                row.append(updateRowNumber)  # put 75 in the back

            else:  # talet e på ret plads
                print("else: " + str(updateRowNumber))
                row.remove(updateRowNumber)
                correctedRow.append(updateRowNumber)
                print("row corrected: " + str(correctedRow))

            print("row now: " + str(row))
        else:
            row.remove(updateRowNumber)
            correctedRow.append(updateRowNumber)

    print("row corrected: " + str(correctedRow))
    fixedUpdates.append(correctedRow)

total = 0
print(fixedUpdates)
for list in fixedUpdates:
    middle_index = len(list) // 2
    middle_value = list[middle_index]
    total += int(middle_value)

print(total)