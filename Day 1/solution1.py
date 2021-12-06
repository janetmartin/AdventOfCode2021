# Advent of Code Problem 1 https://adventofcode.com/2021/day/1

# function to compare any reading to the previous reading
def number_increases(data):
    increases_count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increases_count += 1
    return increases_count


# open and read text file, make list, convert str to int
file = open("raw1.txt", "r")
content = file.read()
readings = content.split("\n")
print(readings)
# perform conversion of str to int
for x in range(0, len(readings)):
    readings[x] = int(readings[x])
print(readings)

# create new list of readings in sliding windows of 3 and compare those
three = []
for i in range(2, len(readings)):
    three.append(readings[i] + readings[i - 1] + readings[i - 2])
print(three)

# print results of function on both lists
print("Part 1: Number of Increases:", number_increases(readings))
print("Part 2: Number of Increases:", number_increases(three))
