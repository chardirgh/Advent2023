import advent
import re

inputs = advent.get_input(3).splitlines()
answer = 0
width = len(inputs[0]) - 1
height = len(inputs) - 1

for y, row in enumerate(inputs):
    digit_buffer = ""
    for x, char in enumerate(row):
        if re.match("\d", char):
            digit_buffer += char
        if (re.match("[^\d]", char) or x == width) and len(digit_buffer) > 0:
            min_x = x - len(digit_buffer) - 1
            if min_x < 0:
                min_x = 0
            if (
                (y > 0 and re.search("[^\d\.]", inputs[y - 1][min_x : x + 1]))
                or re.search("[^\d\.]", inputs[y][min_x : x + 1])
                or (y < height and re.search("[^\d\.]", inputs[y + 1][min_x : x + 1]))
            ):
                answer += int(digit_buffer)
            digit_buffer = ""

advent.clip(answer)
