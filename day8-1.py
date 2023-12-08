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

location = "AAA"
step = 0
while location != "ZZZ":
    location = map[location][instructions[step % max_steps]]
    step += 1

advent.clip(step)
print("--- %s seconds ---" % (time.time() - start_time))
