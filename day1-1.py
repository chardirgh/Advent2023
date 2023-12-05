import advent
import re

inputs = advent.get_input(1).splitlines()
answer = 0

for this_input in inputs:
    digits = re.findall("\d", this_input)
    answer += int(digits[0] + digits[-1])

advent.clip(answer)
