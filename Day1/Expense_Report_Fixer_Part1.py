text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

# Efficient? Not even a little.
data = [int(i) for i in lines]
for int1 in data:
    for int2 in data:
        if int1 + int2 == 2020:
            number = int1 * int2
print(number)