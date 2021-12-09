# Advent of Code Day 3 https://adventofcode.com/2021/day/3
# This was tricky for me so I had to take a look at this solution by Bradley Sware: https://www.youtube.com/watch?v=-z1ZBNfvA8M

# read raw data into list of strings
with open('raw3.txt') as f:
    data = [x for x in f.read().split()]

# PART 1
# set variables
gamma = ""
epsilon = ""
zeros = 0
ones = 0

# nested for-loops to analyze and compare individual bits in each binary number by position
for x in range(0, len(data[0])):
    zeros = 0
    ones = 0
    for y in range(0, len(data)):
        if data[y][x] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# convert binary text to int https://www.kite.com/python/answers/how-to-convert-binary-to-string-in-python
g_hex = int(gamma, 2)
y_hex = int(epsilon, 2)

print("Part 1: Power consumption = ", g_hex * y_hex)

#PART TWO
data2 = data.copy()
index = 0
while len(data2) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for c in range(0, len(data2)):  # loop through list of binaries
        if data2[c][index] == '0':  # if the first str in the binary str is equal to zero
            zero += 1  # count of one added to number of zero bits
            zeros.append(data2[c])  # append the binary value to a new list of numbers beginning with 0
        else:
            one += 1  # same as above but for ones
            ones.append(data2[c])  # same as above but for ones
    if zero > one:  # if number of zeros is great than ones in first position of binary
        data2 = zeros  # use the list of binaries starting with 0
    else:
        data2 = ones  # use othe list of binaries staring with 1
    index += 1  # increment through going to the next index position

oxygen = int(data2[0], 2)  # convert binary to decimal
# for co2 calculation

data3 = data.copy()
index = 0
while len(data3) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for c in range(0, len(data3)):
        if data3[c][index] == '0':
            zero += 1
            zeros.append(data3[c])
        else:
            one += 1
            ones.append(data3[c])
    if one < zero:
        data3 = ones
    else:
        data3 = zeros
    index += 1

co2 = int(data3[0], 2)
print(oxygen, co2)
print("Part 2: oxygen * co2:", co2 * oxygen)
