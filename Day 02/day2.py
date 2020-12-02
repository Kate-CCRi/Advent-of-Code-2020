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
    char = bits[1][0]

    # define the password
    password = bits[-1]

    # count how many times the required character appears in the password
    count = password.count(char)

    # if the count is correct (between min and max), increment the overall counter
    if minval <= count <= maxval:
        goodpass1 += 1

    # notes: need to handle case where maxval > length of string

    # Python counts from 0, the problem wants me to count from 1
    minpos = minval - 1
    maxpos = maxval - 1

    # check to make sure you're still within the word, then check for "only one instance of the character in either
    # position" per the instructions
    if minpos < len(password) and password[minpos] == char:
        if maxpos > len(password):
            goodpass2 += 1
        elif maxpos < len(password) and password[maxpos] != char:
            goodpass2 +=1
    else:
        if maxpos < len (password) and password[maxpos] == char:
            goodpass2 += 1


print(f"The number of Part 2 good passwords is {goodpass2}.")
print(f"The number of Part 1 good passwords is {goodpass1}.")





