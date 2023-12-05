import advent
import re

inputs = advent.get_input(3).splitlines()
answer = 0
width = len(inputs[0]) - 1
height = len(inputs) - 1
star_map = {}

for y, row in enumerate(inputs):
    digit_buffer = ""
    for x, char in enumerate(row):
        if re.match("\d", char):
            digit_buffer += char
        if (re.match("[^\d]", char) or x == width) and len(digit_buffer) > 0:
            min_x = x - len(digit_buffer) - 1
            if min_x < 0:
                min_x = 0
            if y > 0:
                min_y = y - 1
            else:
                min_y = y
            if y < height:
                max_y = y + 1
            else:
                max_y = y

            for y_star in range(min_y, max_y + 1):
                for x_star in range(min_x, x + 1):
                    if inputs[y_star][x_star] == "*":
                        coords = str(y_star) + "|" + str(x_star)
                        if star_map.get(coords):
                            answer += int(digit_buffer) * star_map[coords]
                        else:
                            star_map[coords] = int(digit_buffer)

            digit_buffer = ""

advent.clip(answer)
