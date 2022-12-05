# Read the text file and put each line into an index of an array.
with open("input.txt") as f:
    lines = f.read().splitlines()

# Variable to hold the discrepencies.
contains = 0

# Loop through each line and make each into an array with each number its own index.
for line in lines:
    x = line.replace('-', ',').split(',')

    # Make the first and last 2 elements their own list such that it is a range of numbers between them.
    # Also, make into a set in order to use the is.subset method.
    set1 = set([*range(int(x[0]), int(x[1]) + 1)])
    set2 = set([*range(int(x[2]), int(x[3]) + 1)])

    # If the first set is a subset of the second set or vice versa then there is a range overlap.
    if (set1.issubset(set2) or set2.issubset(set1)):
        contains += 1
    # Else the only other possible way of a range overlap is if the first or second number is equal to or between the last two numbers
    elif ((int(x[0]) >= int(x[2]) and int(x[0]) <= int(x[3])) or ((int(x[1]) >= int(x[2]) and int(x[1]) <= int(x[3])))):
        contains += 1

print(f"The total number of pairs with discrepencies is: {contains}")