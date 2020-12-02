# read in the data file and split it into lines
data = open("data.txt")
lines = data.readlines()

# set up a counter
goodpass = 0

# split each item in lines into an array of its component pieces
for line in lines:
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
        goodpass += 1

print(f"The number of good passwords is {goodpass}.")

