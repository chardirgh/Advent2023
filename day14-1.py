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


map = [list(i) for i in inputs]
map = sort_north(map)

factor = len(map)
for m in map:
    count = sum([(x == "O") for x in m])
    answer += count * factor
    factor -= 1

advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
