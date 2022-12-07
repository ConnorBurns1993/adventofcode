# PART 1 ------------

# Read the Data
with open('day3.in') as file:
    rucksacks = [i for i in file.read().strip().split('\n')]

# Create an index count for letters
priority = '#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
counter = 0

# Look through each line and create a set of the unique values in each different compartment, then if any characters from the first compartment is in the second compartment, we add the
# index count to our total.
for rucksack in rucksacks:
    half = len(rucksack) // 2
    compartment1 = set(rucksack[:half])
    compartment2 = set(rucksack[half:])

    for c in compartment1:
        if c in compartment2:
            total += priority.index(c)

# PART 2 -----------------

total = 0
j = 3

# Make groups of 3
for i in range(0, len(rucksacks), 3):
    groups = rucksacks[i:j]
    j += 3

# Check if the letter is in all three of the groups and if it is, add the priority values to the total.
    for p in priority:
        if p in groups[0] and p in groups[1] and p in groups[2]:
            total += priority.index(p)

print(total)
