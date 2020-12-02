# read in the data file and split it into lines
data = open("text.txt")
lines = data.readlines()

# PART ONE

# Set num1 to the first item in the "lines" file
num1 = int(lines.pop())
num2 = 0

print("num1")

for line in lines:
    num2 = int(line)

    if num1 + num2 == 2020:
        break

product = num1 * num2

print(f"The first number is {num1}")
print(f"The second number is {num2}")
print(f"Their product is {product}")
