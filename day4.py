# Read the Data
with open('day4.in') as file:
    sections = [i for i in file.read().strip().split('\n')]

# Part 1 -------------------

overlap = 0

# Create a overlap variable and break the sections into more readable integer data. Then use logic to check if either first is completely contained in second or vice versa.

for section in sections:
    first, second = section.split(',')
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    first_start = first[0]
    first_end = first[1]

    second_start = second[0]
    second_end = second[1]

    if first_start <= second_start and first_end >= second_end:
        overlap += 1

    elif first_start >= second_start and first_end <= second_end:
        overlap += 1

# Part 2 -----------------------

overlap = 0
# Split the data like in Part 1, and then check if the first start is equal or first end in the range of second, and vice versa.
for section in sections:
    first, second = section.split(',')
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    first_start = first[0]
    first_end = first[1]

    second_start = second[0]
    second_end = second[1]

    if first_start is range(second_start, second_end + 1) or first_end in range(second_start, second_end + 1):
        overlap += 1
    elif second_start is range(first_start, first_end + 1) or second_end in range(first_start, first_end + 1):
        overlap += 1


print(overlap)
