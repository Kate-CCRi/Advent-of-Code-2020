# read in the data file
data = open("test.txt")
lines = data.readlines()

print(lines)

'''
Approach:
    * pull items off the list of lines until you get to a newline
        lines.pop(0) will get you the first thing in a list
    * read the things you've now got into a k,v dictionary for each person
    * check the list of keys vs. the list of all the keys you're supposed to have
    * if you find them all, increment a counter
'''

newdata = []
passports = {}

for line in lines:

    # Each set of valid data is separated by a naked newline, so we can assume that data between newlines is all one set of information.
    # Check to make sure tht your line isn't a new line:
    if line != '\n':

        # This splits the line into the individual pieces of data and aggregates all the data between newlines
        newdata += line.split()
        print(newdata)

    else:
        # Next step: Figure out how to take the aggregated newline and read it into a single list of dictionary entries per person

        tempdict = {}

        for item in newdata:

            # Splits each item in the newdata list into a two item list at the colon
            templist = item.split(":")

            # This is *supposed* to read the items into a temporary dictionary but doesn't work for some reason
            tempdict[templist[0]] = tempdict[templist[1]]

            print(tempdict)

        # Reset the newline to an empty list when you find a naked newline, which distinguishes a new person's data
        newdata = []
        print("I found a naked newline!")

