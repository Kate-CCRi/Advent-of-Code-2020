# read in the data file and split it into lines
data = open("test.txt")
lines = data.readlines()

# Set up some counters
xpos = 0
ypos = 0
trees = 0
# This one had to be -1 because the readlines was including the newline character
linesize = len(lines[0]) - 1

while ypos <= len(lines):

    line = lines[ypos]
    print(line)

    if xpos >= linesize:
        xpos = xpos - linesize

    # If you hit a tree, increment the tree counter
    if line[xpos] == "#":
        trees += 1

    # Do the moves
    xpos += 3
    ypos += 1

else:
    print(f"The number of trees you hit is {trees}.")


'''
# Iterate through the data file

for line in lines:

    # If we wrap around the end of the line, start again at the beginning
    if xpos >= linesize:
        xpos = xpos - linesize

    # If you hit a tree, increment the tree counter
    if line[xpos] == "#":
        trees += 1

    # Do the moves
    xpos += 3
    ypos += 1

# Print the answer
print(f"The number of trees you hit is {trees}.")
'''
