import re

print("Day4 challenge 1/2: start")


matrix = []

# Open and read the file
with open("input.txt", "r") as file:
    for line in file:
        # Split the line into values based on a delimiter (e.g., space or comma)
        row = list(line.replace("\n", ""))  # create list of chars
        # Append the row to the matrix
        matrix.append(row)

target = "XMAS"

total = 0


def recursive_skat(previousvalue, old_y, y_dir, old_x, x_dir):
    y = old_y + y_dir
    x = old_x + x_dir

    global total
    if x < 0 or y < 0:
        return
    if y >= len(matrix) or x >= len(matrix[0]):
        return

    newvalue = previousvalue + matrix[y][x]
    # check if value is XMAS
    if newvalue == target:
        total += 1
    elif target.startswith(newvalue):
        recursive_skat(newvalue, y, y_dir, x, x_dir)


print(matrix[0][5])

for row_index, row in enumerate(matrix):
    # Iterate through each element in the row
    for col_index, element in enumerate(row):
        if matrix[row_index][col_index] == 'X':
            recursive_skat("X", row_index, 0, col_index, 1)
            recursive_skat("X", row_index, 0, col_index, -1)
            recursive_skat("X", row_index, 1, col_index, 0)
            recursive_skat("X", row_index, 1, col_index, 1)
            recursive_skat("X", row_index, 1, col_index, -1)
            recursive_skat("X", row_index, -1, col_index, 0)
            recursive_skat("X", row_index, -1, col_index, 1)
            recursive_skat("X", row_index, -1, col_index, -1)

print(total)
