import re

print("Day4 challenge 2/2: start")


matrix = []

# Open and read the file
with open("input2.txt", "r") as file:
    for line in file:
        # Split the line into values based on a delimiter (e.g., space or comma)
        row = list(line.replace("\n", ""))  # create list of chars
        # Append the row to the matrix
        matrix.append(row)

target = "MAS"
targetReverse = "SAM"
total = 0


def recursive_skat(previousvalue, y, y_dir, x, x_dir):
    global total
    if x < 0 or y < 0:
        return False
    if y >= len(matrix) or x >= len(matrix[0]):
        return False

    newvalue = previousvalue + matrix[y][x]

    # check if value is XMAS
    if newvalue == target or newvalue == targetReverse:
        return True
    elif target.startswith(newvalue) or targetReverse.startswith(newvalue):
        return recursive_skat(newvalue, y + y_dir, y_dir, x + x_dir, x_dir)
    else:
        return False


def checkA(y, x):
    global total
    v = matrix[y][x]
    if v == "A" and recursive_skat("", y - 1, 1, x + 1, -1) and recursive_skat("", y - 1, 1, x - 1, 1) and recursive_skat("", y + 1, -1, x - 1, 1) and recursive_skat("", y + 1, -1, x + 1, -1):
        total += 1


for row_index, row in enumerate(matrix):
    # Iterate through each element in the row
    for col_index, element in enumerate(row):
        checkA(row_index, col_index)

print(total)
