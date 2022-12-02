# Make a dictionary that will hold the rules for point values for each possible outcome
rules = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}

# Read the text file and put each line into an index of an array
# Also, remove the newspace character from each line
with open("input.txt") as f:
    lines = f.read().splitlines()

# Loop through the each line of the input text to find the point value and add it to the sum
sum_points = 0
for line in lines:
    # Remove the spacing between the opponent's choice and yours
    line = line.replace(" ", "")
    sum_points += rules.get(line) 

print(f"The total score: {sum_points}")