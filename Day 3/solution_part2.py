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
sum_group_priority = 0

# Loop through each group in the text file
for i in range(0, len(lines), 3):
    # Make each group the next 3 indices in the list
    group = lines[i: i+3]

    # Create a set for each member of the group
    set_1 = set(group[0])
    set_2 = set(group[1])
    set_3 = set(group[2])

    # Find and access the character that is shared by the 3 members of the group
    shared_item = (set_1.intersection(set_2)).intersection(set_3)
    char_shared_item = shared_item.pop()

    # Use the helper method to find the priority value (according to the prompt rules) for that character
    sum_group_priority += get_Value(char_shared_item)

print(f"The sum of the priorities is {sum_group_priority}")