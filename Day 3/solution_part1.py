# Helper function that will convert an ASCII value of a character to the priority values in the question prompt and return that value.
def get_Value(letter):
    ASCII_val = ord(letter)
    # If the ASCII value of the character is 97 or greater then it means it is a lowercase letter.
    # Else we know it is an uppercase character.
    if ASCII_val >= 97:
        val = ASCII_val - 96
    else:
        val = ASCII_val - 38
    
    return val

# Read the text file and put each line into an index of an array.
with open("input.txt") as f:
    lines = f.read().splitlines()

# Variable that will hold the sum of the priorities.
sum_priority = 0

# Loop through each line and split them into 2 of equal length
for line in lines:
    length = len(line)//2

    # Create sets for each length in order to remove duplicates
    s1 = set(line[0: length])
    s2 = set(line[length:])

    # Find and access the character that is shared by the sets
    char_shared_item = s1.intersection(s2).pop()

    # Use the helper method to find the priority value (according to the prompt rules) for that character
    sum_priority += get_Value(char_shared_item)

print(f"The sum of the priorities is {sum_priority}")