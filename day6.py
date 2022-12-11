# Read the Data
with open('day6.in') as file:
    signals = file.read()

# Part 1 --------------------

# Make an array to consistenly check if the length is 4 and also keep track if which index you are at.
first_marker = []
marker_index = 0

# Iterate through and if the letter is not in the array, append it to the array. If a duplicate is found, clear the array and start over.
for i, s in enumerate(signals):
    if s not in first_marker:
        first_marker.append(s)
        if len(first_marker) == 4:
            marker_index = i
            break
    else:
        first_marker  = []

# print(marker_index)

# Part 2 --------------------

# Iterate through and if the letter is not in the array, append it to the array. If a duplicate is found, clear the array and start over.
for i in range(14, len(signals)):
    unique = set(signals[(i - 14):i])
    if len(unique) == 14:
        print(i)
        break
