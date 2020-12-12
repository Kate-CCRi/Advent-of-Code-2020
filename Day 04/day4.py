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
passwords = []

for line in lines:
    if line != '\n':
        break
        # This code doesn't work - it wants to iterate by single characters - need to put in a "split on :" kind of deal instead and then put the first thing in as the key and the second thing in as the value
        # for item in line:
        #    print(item)
        #    data = {}
        #    data[item[0]] = item[2]
        # passwords.append(data)
    else:
        print("I found a naked newline!")

print(passwords)