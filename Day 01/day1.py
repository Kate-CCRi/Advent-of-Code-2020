# Make it so it'll run on my stupid NUC, which has Python 2.7 instead of 3.6
from __future__ import print_function

# read in the data file and split it into lines
data = open("test.txt")
lines = data.readlines()

# PART ONE

# Set num1 to the first item in the "lines" file
num1 = int(lines.pop())
num2 = 0

for line in lines:
    num2 = int(line)

    if num1 + num2 == 2020:
        break

product = num1 * num2

print(f"The first number is {num1}")
print(f"The second number is {num2}")
print(f"Their product is {product}")
