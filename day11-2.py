import advent
import time

inputs = advent.get_input(11).splitlines()
start_time = time.time()
answer = 0

width_range = range(len(inputs[0]))
height_range = range(len(inputs))
expanded_y = []
expanded_x = []
for y, row in enumerate(inputs):
    if not "#" in row:
        expanded_y.append(y)

x_count = 0
for x in width_range:
    if all([inputs[y][x] == "." for y in height_range]):
        expanded_x.append(x)


galaxies = []

for y, row in enumerate(inputs):
    for x, col in enumerate(row):
        if "#" == col:
            galaxies.append({"x": x, "y": y})

expansion_factor = 1000000 - 1

for idx, g in enumerate(galaxies):
    for g1 in galaxies[idx + 1 :]:
        min_x = min(g["x"], g1["x"])
        max_x = max(g["x"], g1["x"])
        min_y = min(g["y"], g1["y"])
        max_y = max(g["y"], g1["y"])
        distance = (max_x - min_x) + (max_y - min_y)
        for x in expanded_x:
            if min_x < x < max_x:
                distance += expansion_factor
        for y in expanded_y:
            if min_y < y < max_y:
                distance += expansion_factor
        answer += distance


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
