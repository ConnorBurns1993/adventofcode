with open('day2.in') as file:
    rounds = [i for i in file.read().strip().split('\n')]

scores = {'A': 1, 'B': 2, 'C': 3}

score = 0

for r in rounds:

    # Draw the round
    if r[2] == 'Y':
        score += scores[r[0]]
        score += 3

    # Win the round
    if r[2] == 'Z':
        score += 6
        if r[0] == 'A':
            score += 2
        if r[0] == 'B':
            score += 3
        if r[0] == 'C':
            score += 1

    # Lose the round
    if r[2] == 'X':
        if r[0] == 'A':
            score += 3
        if r[0] == 'B':
            score += 1
        if r[0] == 'C':
            score += 2

print(score)
