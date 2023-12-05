import advent
import re

inputs = advent.re_input("Game (\d*):(.*)", 2)
answer = 0

for this_input in inputs:
    grabs = re.findall(" .*?;", this_input[1] + ";")
    possible = True
    for grab in grabs:
        red = re.search("(\d\d?) red", grab)
        red = int(red.groups()[0]) if red else 0

        green = re.search("(\d\d?) green", grab)
        green = int(green.groups()[0]) if green else 0

        blue = re.search("(\d\d?) blue", grab)
        blue = int(blue.groups()[0]) if blue else 0

        if red > 12 or green > 13 or blue > 14:
            possible = False
            break

    if possible:
        answer += int(this_input[0])


advent.clip(answer)
