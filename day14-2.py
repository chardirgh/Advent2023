import advent
import time

inputs = advent.get_input(14).splitlines()
start_time = time.time()
answer = 0


def sort_north(map):
    width_range = range(len(map[0]))
    height_range = range(1, len(map))
    for x in width_range:
        done = False
        while not done:
            done = True
            for y in height_range:
                if map[y][x] == "O" and map[y - 1][x] == ".":
                    map[y][x] = "."
                    map[y - 1][x] = "O"
                    done = False
    return map


def sort_south(map):
    width_range = range(len(map[0]))
    height_range = range(len(map) - 1)
    for x in width_range:
        done = False
        while not done:
            done = True
            for y in height_range:
                if map[y][x] == "O" and map[y + 1][x] == ".":
                    map[y][x] = "."
                    map[y + 1][x] = "O"
                    done = False
    return map


def sort_east(map):
    width_range = range(len(map[0]) - 1)
    height_range = range(len(map))
    for y in height_range:
        done = False
        while not done:
            done = True
            for x in width_range:
                if map[y][x] == "O" and map[y][x + 1] == ".":
                    map[y][x] = "."
                    map[y][x + 1] = "O"
                    done = False
    return map


def sort_west(map):
    width_range = range(1, len(map[0]))
    height_range = range(len(map))
    for y in height_range:
        done = False
        while not done:
            done = True
            for x in width_range:
                if map[y][x] == "O" and map[y][x - 1] == ".":
                    map[y][x] = "."
                    map[y][x - 1] = "O"
                    done = False
    return map


map = [list(i) for i in inputs]

cycles = []

for i in range(500):
    map = sort_north(map)
    map = sort_west(map)
    map = sort_south(map)
    map = sort_east(map)
    factor = len(map)
    load = 0
    for m in map:
        count = sum([(x == "O") for x in m])
        load += count * factor
        factor -= 1

    cycles.append(load)

start = -1
length = -1
for i in range(len(cycles) - 30):
    # guess pattern at 5-20 length:
    for j in range(5, 20):
        if cycles[i : i + j] == cycles[i + j : i + (j * 2)]:
            start = i
            length = j
            break
    if start > 0:
        break


print(start, length)
print(cycles[start : start + length])

position = (1000000000 - start) % length
print(position)

answer = cycles[position + start - 1]

advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
