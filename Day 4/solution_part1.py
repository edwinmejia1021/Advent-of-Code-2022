# Read the text file and put each line into an index of an array.
with open("input.txt") as f:
    lines = f.read().splitlines()

# Variable to hold the discrepencies
contains = 0

# Loop through each line and make each into an array with each number its own index
for line in lines:
    x = line.replace('-', ',').split(',')
    if ((int(x[0]) >= int(x[2]) and int(x[1]) <= int(x[3])) or (int(x[2]) >= int(x[0]) and int(x[3]) <= int(x[1]))):
        contains += 1

print(f"The total number of pairs with discrepencies is: {contains}")