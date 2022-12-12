# Helper function that will find the scenic score for one side of the tree.
def find_scenic(list1, tree, reverse = True):
    # The scenic score for a tree 
    scenic_score = 0

    # Loop through one of the trees' side to find it scenic score.
    # Reverse is true when we are looking at the left and top side.
    if reverse:
        for x in range(len(list1) - 1, -1, -1):
            # If the tree is taller then add one more to the scenic score.
            if int(tree) > list1[x]:
                scenic_score += 1
            # Else we stop at the taller tree, add one more to the scenic score and break out the loop.
            elif int(tree) <= list1[x]:
                scenic_score += 1
                break
    # Reverse is false when looking at the right and bottom side.
    else:
        for x in range(0, len(list1)):
            # If the tree is taller then add one more to the scenic score.
            if int(tree) > list1[x]:
                scenic_score += 1
            # Else we stop at the taller tree, add one more to the scenic score and break out the loop.
            elif int(tree) <= list1[x]:
                scenic_score += 1
                break
    return scenic_score

# Read the input text file.
with open("input.txt") as f:
    lines = f.read().splitlines()

# Turn the list of lines into just one string containing all of the trees.
trees = ''.join(lines)

# Variables to keep track of the rows and columns.
row = 0
column = 0

# Keep track of the row length, number of rows, and total number of trees.
len_row = len(lines[0]) - 1
total = len(trees)
num_rows = total//(len_row + 1)

# List to keep the scenic score for left, right, top, and bottom side of a tree.
scenic_list = []

for tree in trees:
    # If we are on the edges then we ignore cause scenic score will be 0
    if ((row == 0) or (column == 0) or (column == len_row) or (row == num_rows - 1)):
        # If we are at the end of a row, we want to move to the next row and reset the column counter to 0. 
        if ((column % len_row) == 0) and column != 0:
            row += 1
            column = 0
            continue
        else:
            column += 1
            continue

    # Make a list for the surrounding trees depending on the trees' row and column.
    surr_rows = []
    surr_rows[:0] = trees[(row * (len_row + 1)): ((len_row + 1) * row) + (len_row + 1)]
    surr_cols = []
    surr_cols[:0] = trees[column: total - 1: len_row + 1]

    # Pop the element we are inspecting currently from the list.
    surr_rows.pop(column)
    surr_cols.pop(row)

    # Make the left, right, top, and bottom of the current tree their own set.
    surr_rows_left = [int(x) for x in surr_rows[0: column]]
    surr_rows_right = [int(x) for x in surr_rows[column: ]]
    surr_cols_left = [int(x) for x in surr_cols[0: row]]
    surr_cols_right = [int(x) for x in surr_cols[row: ]]

    # Use of the helper function to find the scenic score for each side of the tree.
    left = find_scenic(surr_rows_left, tree)
    right = find_scenic(surr_rows_right, tree, reverse = False)
    top = find_scenic(surr_cols_left, tree)
    bottom = find_scenic(surr_cols_right, tree, reverse = False)

    # Append the product of all 4 sides into the list.
    scenic_list.append(left * right * top * bottom)

    # Increase the column number after each tree we see.
    column += 1

# The best scenic score is the max number in the list.
best_score = max(scenic_list)

print(f"The best scenic score is {best_score}")