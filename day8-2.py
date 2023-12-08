import advent
import time
import re

inputs = advent.get_input(8).split("\n\n")
start_time = time.time()

instructions = inputs[0]
max_steps = len(instructions)

map = {}
for row in inputs[1].splitlines():
    regex = re.match("(...) = \((...), (...)\)", row).groups()
    map[regex[0]] = {"L": regex[1], "R": regex[2]}

step_totals = []

for location in map:
    if location[2] == "A":
        step = 0
        while location[2] != "Z":
            location = map[location][instructions[step % max_steps]]
            step += 1
        step_totals.append(step)


def find_GCD(x, y):
    if x == 0:
        return y
    low = min(x, y)
    return find_GCD(max(x, y) % low, low)


answer = step_totals[0]
for x in step_totals[1:]:
    answer = (answer * x) / find_GCD(answer, x)  # LCM

advent.clip(int(answer))
print("--- %s seconds ---" % (time.time() - start_time))
