# Elf Data
with open('day1.in') as file:
    calories = [i for i in file.read().strip().split('\n')]

# Have a Calorie Counter, and a Max Calories
cals_list = []
cals = 0

#Loop through and add the calories, then once you encounter a space, check the max and reset the counter.
for c in calories:
    if c == '':
        cals_list.append(cals)
        cals = 0
    else:
        cals += int(c)

cals_list = sorted(cals_list)
print(cals_list[-1] + cals_list[-2] + cals_list[-3])
