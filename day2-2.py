import advent
import re

inputs = advent.re_input("Game (\d*):(.*)", 2)
answer = 0

for this_input in inputs:
    grabs = re.findall(" .*?;", this_input[1] + ";")
    min_red = 0
    min_green = 0
    min_blue = 0
    for grab in grabs:
        red = re.search("(\d\d?) red", grab)
        red = int(red.groups()[0]) if red else 0
        if red > min_red:
            min_red = red

        green = re.search("(\d\d?) green", grab)
        green = int(green.groups()[0]) if green else 0
        if green > min_green:
            min_green = green

        blue = re.search("(\d\d?) blue", grab)
        blue = int(blue.groups()[0]) if blue else 0
        if blue > min_blue:
            min_blue = blue

    answer += min_red * min_green * min_blue

advent.clip(answer)
