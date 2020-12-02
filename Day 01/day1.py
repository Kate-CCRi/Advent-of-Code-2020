# Import itertools for better iteration
import itertools

# read in the data file and split it into lines
data = open("data.txt")
lines = data.readlines()

# PART ONE

# Use itertools to compare all possible combinations of two numbers in the list of input data
for num1, num2 in itertools.combinations(lines, 2):
    sum = int(num1) + int(num2)

    if sum == 2020:
        product = int(num1) * int(num2)
        print(f"The first number is {num1}")
        print(f"The second number is {num2}")
        print(f"Their sum is {sum}")
        print(f"Their product is {product}")
        break


