with open("day10.in") as file:
    x = 1
    cycle = 0
    display = []
    row = ''
    cycles = set([20, 60, 100, 140, 180, 220])

    def matching(cycle):
        if cycle in cycles:
            return True
        return False

    strengths = 0
    for line in file:
        instructions = line.rstrip().split()

        if instructions[0] == 'noop':
            cycle += 1

            row += '#' if len(row) in range(x - 1, x + 2) else '.'
            if len(row) == 40:
                display.append(row)
                row = ''

            if matching(cycle):
                strengths += (x * cycle)

        if instructions[0] == 'addx':
            t = 2
            while t > 0:
                cycle += 1

                row += '#' if len(row) in range(x - 1, x + 2) else '.'
                if len(row) == 40:
                    display.append(row)
                    row = ''

                if matching(cycle):
                    strengths += (x * cycle)
                t -= 1
            x += int(instructions[1])

    print(*display, sep='\n')
