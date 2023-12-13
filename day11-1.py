import advent
import time
import re

inputs = advent.get_input(11).splitlines()
start_time = time.time()
answer = 0

width = len(inputs[0])
expanded = []
for y in inputs:
    expanded.append(list(y))
    if not re.search("#", y):
        expanded.append(["."] * width)

x_count = 0
height_range = range(len(inputs))
for x in range(width):
    if all([inputs[y][x] == "." for y in height_range]):
        for e_y in range(len(expanded)):
            expanded[e_y].insert(x + x_count, ".")
        x_count += 1

galaxies = []

for y, row in enumerate(expanded):
    for x, col in enumerate(row):
        if "#" == col:
            galaxies.append({"x": x, "y": y})


for idx, g in enumerate(galaxies):
    for g1 in galaxies[idx + 1 :]:
        distance = abs(g["x"] - g1["x"]) + abs(g["y"] - g1["y"])
        answer += distance


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
