# Helper method that will determine the number of moves and the arrays that will change based on the moves
def make_moves(line):
        # Determine the starting array and convert to an int.
        start_arr = int(line[line.find('m ') + 2: line.find(' t')])

        # Determine the end array and convert to an int.
        end_arr = int(line[line.find('o ') + 2: len(line)])

        # Determine the number of moves needed.
        moves = int(line[line.find('e') + 2: line.find(' f')])

        # Based on the total number of moves start to change the arrays based on the move lists
        i = moves - 1  # This index will be used to determine the first crate taken out considering it's not the first one in the stack
        for x in range(moves):
            lists[end_arr - 1].insert(0, lists[start_arr - 1].pop(i))
            i -= 1

# Read the text file and put each line into an index of an array.
with open("input.txt") as f:
    lines = f.read().splitlines()

# Remove any empty string elements in the list of lines.
lines.remove('')

# Make a lists that will hold each stack with its crates
# Still trying to figure out how to not manually input how many stacks there are
lists = [[] for _ in range(9)]

for line in lines:
    # If the line has a 1 in the first index then we know to ignore this line because it just lists the array numbers.
    if (line[1] == '1'):
        continue
    # If the line has an m as the first element then we know the rules are starting, so we do those rules.
    elif (line[0] == 'm'):
        make_moves(line)
    # The last case is we are at the beginning of the text file and setting up the arrays.
    for i in range(1, len(line), 4):
        # If the line does not have an empty string and is an upper case letter then it represents a crate.
        if (line[i] != '' and line[i].isupper()):
            lists[i//4].append(line[i])

# Create a string with the first crate from each stack
answer = "".join([item[0] for item in lists])
print(answer)