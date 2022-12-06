# Reading the one line of text from the input and then closing the file
f = open("input.txt", "r")
line = f.readline()
f.close()

# Set that will hold 4 characters to check they are all unique 
marker = ""

# Variable that will keep track of the character position in our foor loop
pos = 1

# Variable that can change depending on how many distinct characters you want
#dist_char = 4 # For part 1
dist_char = 14  # For Part 2

for ch in line:
    # Concatenate the character to the marker
    marker = marker + ch 
    marker_set = set(marker)

    # Check to see that the set is less than 4 because that means start-of-packet has not been found
    if(len(marker_set) < dist_char):
        # If the length of the string is 4 and the current character is no unique, then we eliminate the beginning character 
        if (len(marker) == dist_char and marker.find(ch) != -1):
            marker = marker[1:]
    else:
        break
    
    # Add one to the position since we are going to continue the for loop
    pos += 1


print(f"The first start-of-packet marker is detected after character {pos}")