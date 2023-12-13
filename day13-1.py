import advent
import time

inputs = advent.get_input(13).split("\n\n")
start_time = time.time()
answer = 0


def find_horizontal_reflection(map):
    height = len(map) - 1
    for i in range(height):
        if map[i] == map[i + 1]:
            low = i
            high = i + 1
            match = True
            while low >= 0 and high <= height:
                if map[low] != map[high]:
                    match = False
                    break
                low -= 1
                high += 1
            if match:
                print("horiz match on", i)
                for row in map:
                    print(row)
                return i + 1
    return 0


def find_vertical_reflection(map):
    width = len(map[0])
    for i in range(width - 1):
        if all(row[i] == row[i + 1] for row in map):
            low = i
            high = i + 1
            match = True
            while low >= 0 and high <= width - 1:
                if not all(row[low] == row[high] for row in map):
                    match = False
                    break
                low -= 1
                high += 1
            if match:
                print("vert match on", i)
                for row in map:
                    print(row)
                return i + 1
    return 0


for i in inputs:
    h = find_horizontal_reflection(i.splitlines()) * 100
    v = find_vertical_reflection(i.splitlines())
    answer += h + v


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
