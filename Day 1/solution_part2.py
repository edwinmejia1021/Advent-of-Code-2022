# Read the text file and put each line into an index of an array
with open("input.txt") as f:
    lines = f.readlines()

# Keep track of the calorie count for one elf 
count = 0

# Make an array of calories to hold each elf's calorie count
calories = []

# Loop through the text file array
for line in lines:
    # Replace all newline characters with no character at all
    s2 = line.replace("\n", "")

    # If the current element is an empty string then we know we are done counting an elf's calories
    if s2 == '':
        # Add the elf's calorie count to the array and reset the counter for the next elf
        calories.append(count)
        count = 0
    else: 
        # If it is not an empty string, then keep counting the calories
        count += int(s2)

# Sort the calories array in ascending order and return the sum of the top 3 biggest calorie counts
calories.sort()
top_3 = sum(calories[-3:])
print(f"The total calories for the top three Elves is: {top_3}")


#### DOES NOT TAKE INTO ACCOUNT MORE THAN ONE SPACE IN BETWEEN ELF LISTS