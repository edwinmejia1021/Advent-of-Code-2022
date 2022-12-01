# Read the text file and put each line into an index of an array
with open("input.txt") as f:
    lines = f.readlines()

# Keep track of the calorie count for one elf and the biggest total calorie count
count = 0
biggest = 0

# Loop through the text file array
for line in lines:
    # Replace all newline characters with no character at all
    s2 = line.replace("\n", "")

    # If the current element is an empty string then we know we are done counting an elf's calories
    if s2 == '':
        # If the count of the current elf is greater than the biggest calorie count so far, then make this the biggest count
        # And reset the counter back to 0 for the next elf
        if count >= biggest:
            biggest = count
        count = 0
    else: 
         # If it is not an empty string, then keep counting the calories
        count += int(s2)

print(f"The elf carrying the most calories has a total of {biggest} calories")