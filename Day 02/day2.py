# read in the data file and split it into lines
data = open("data.txt")
lines = data.readlines()

# set up a counter
goodpass = 0

# split each item in lines into an array of its component pieces
for line in lines:
    bits = line.split()

    # pull the minimum required number and the maximum required number
    minmax = bits[0]
    min = int(minmax[0])
    max = int(minmax[-1])

    # pull the required character
    reqchar = bits[1]
    char = reqchar[0]

    # define the password
    password = bits[-1]

    # count how many times the required character appears in the password
    count = password.count(char)

    # if the count is correct (between min and max), increment the overall counter
    if min <= count <= max:
        goodpass += 1

print(f"The number of good passwords is {goodpass}.")

