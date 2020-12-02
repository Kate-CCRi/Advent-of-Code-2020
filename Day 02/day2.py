# read in the data file and split it into lines
data = open("data.txt")
lines = data.readlines()

# set up some counters
goodpass1 = 0
goodpass2 = 0

# iterate through the lines file
for line in lines:

    # split each item in lines into an array of its component pieces
    bits = line.split()

    # pull the minimum required number and the maximum required number
    # note that you have to do it with "split" because just pulling the character by index reference doesn't work for
    # two-character numbers
    minmax = bits[0].split("-")
    minval = int(minmax[0])
    maxval = int(minmax[-1])

    # pull the required character
    reqchar = bits[1]
    char = reqchar[0]

    # define the password
    password = bits[-1]

    # count how many times the required character appears in the password
    count = password.count(char)

    # if the count is correct (between min and max), increment the overall counter
    if minval <= count <= maxval:
        goodpass1 += 1

    # notes: need to -1 from place values because they're starting from 1
    # notes: need to handle case where maxval > length of string

print(f"The number of Part 1 good passwords is {goodpass1}.")





