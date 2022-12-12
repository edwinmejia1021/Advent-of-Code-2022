with open("input.txt") as f:
    lines = f.read().splitlines()

# Turn the list of lines into just one string containing all of the trees
trees = ''.join(lines)

# Variables to keep track of the rows and columns.
row = 0
column = 0

# Keep track of the row length, number of rows, and total number of trees
len_row = len(lines[0]) - 1
total = len(trees)
num_rows = total//(len_row + 1)

# The number of trees that are visible.
visible = 0

for tree in trees:
    # If we are on the edges then we ignore that value because we already know it is visible
    if ((row == 0) or (column == 0) or (column == len_row) or (row == num_rows - 1)):
        visible += 1
        # If we are at the end of a row, we want to move to the next row and reset the column counter to 0. 
        if ((column % len_row) == 0) and column != 0:
            row += 1
            column = 0
        else:
            column += 1

        continue

    # Make a list for the surrounding trees depending on the trees' row and column.
    surr_rows = []
    surr_rows[:0] = trees[(row * (len_row + 1)): ((len_row + 1) * row) + (len_row + 1)]
    surr_cols = []
    surr_cols[:0] = trees[column: total - 1: len_row + 1]

    # Pop the element we are inspecting currently from the list
    surr_rows.pop(column)
    surr_cols.pop(row)

    # Make the left, right, top, and bottom of the current tree their own set
    surr_rows_left = set(int(x) for x in surr_rows[0: column])
    surr_rows_right = set(int(x) for x in surr_rows[column: ])
    surr_cols_left = set(int(x) for x in surr_cols[0: row])
    surr_cols_right = set(int(x) for x in surr_cols[row: ])

    # if the tree is not a number in the set to the left then it is either less than or greater than the set
    if int(tree) not in surr_rows_left:
        # Once added to the set, if the tree is the max, then we know it is the tallest on the left side, so we increase visible
        # And continue to the next tree
        surr_rows_left.add(int(tree))
        if (max(surr_rows_left) == int(tree)):
            visible += 1
            column += 1
            continue
    
    # if the tree is not a number in the set to the right then it is either less than or greater than the set
    if int(tree) not in surr_rows_right:
        # Once added to the set, if the tree is the max, then we know it is the tallest on the right side, so we increase visible
        # And continue to the next tree
        surr_rows_right.add(int(tree))
        if (max(surr_rows_right) == int(tree)):
            visible += 1
            column += 1
            continue

    # if the tree is not a number in the set to the top then it is either less than or greater than the set
    if int(tree) not in surr_cols_left:
        # Once added to the set, if the tree is the max, then we know it is the tallest on the top side, so we increase visible
        # And continue to the next tree
        surr_cols_left.add(int(tree))
        if (max(surr_cols_left) == int(tree)):
            visible += 1
            column += 1
            continue

    # if the tree is not a number in the set to the bottom then it is either less than or greater than the set
    if int(tree) not in surr_cols_right:
        # Once added to the set, if the tree is the max, then we know it is the tallest on the bottom side, so we increase visible
        # And continue to the next tree
        surr_cols_right.add(int(tree))
        if (max(surr_cols_right) == int(tree)):
            visible += 1
            column += 1
            continue

    # Increase the column number after each tree we see
    column += 1

print(visible)