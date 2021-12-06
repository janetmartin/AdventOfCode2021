# Advent of Code Day 2 https://adventofcode.com/2021/day/2

# open text file and loopthrough data to add up directions by amounts
# PART 1
with open("raw2.txt", mode="r") as file:
    horizontal = 0
    depth = 0
    for line in file.readlines():
        direction, amount = line.split()
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
        if direction == "down":
            depth += amount
        if direction == "up":
            depth -= amount

print("Part 1: Final horizontal position multiplied by final depth is:", (horizontal * depth))

# PART 2
with open("raw2.txt", mode="r") as file:
    horizontal = 0
    depth = 0
    aim = 0
    for line in file.readlines():
        direction, amount = line.split()
        amount = int(amount)
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount
        if direction == "forward":
            horizontal += amount
            depth += amount * aim


print("Part 2: Final horizontal position multiplied by final depth:", (horizontal * depth))