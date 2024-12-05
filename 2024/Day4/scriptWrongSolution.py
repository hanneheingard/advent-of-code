import re

print("Day4 challenge 1/2: start")


matrix = []

# Open and read the file
with open("inputexample.txt", "r") as file:
    for line in file:
        # Split the line into values based on a delimiter (e.g., space or comma)
        row = list(line.replace("\n", ""))  # create list of chars
        # Append the row to the matrix
        matrix.append(row)

target = "XMAS"

total = 0

def recursive_skat(previousvalue, y, x):
    global total
    if x < 0 or y < 0:
        return
    if y >= len(matrix) or x >= len(matrix[0]):
        return

    value = matrix[y][x]
    newvalue = previousvalue + value
    # check if value is XMAS
    if newvalue == target:
        total += 1
    elif target.startswith(newvalue):
        recursive_skat(newvalue, y, x+1)
        recursive_skat(newvalue, y, x-1)
        recursive_skat(newvalue, y+1, x+1)
        recursive_skat(newvalue, y-1, x+1)
        recursive_skat(newvalue, y-1, x-1)
        recursive_skat(newvalue, y+1, x)
        recursive_skat(newvalue, y-1, x)
        recursive_skat(newvalue, y+1, x-1)


recursive_skat("", 3, 9)

# Iterate through the rows
for row_index, row in enumerate(matrix):
    # Iterate through each element in the row
    for col_index, element in enumerate(row):
        recursive_skat("", row_index, col_index)

print(total)
