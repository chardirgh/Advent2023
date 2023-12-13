import advent
import time

inputs = advent.get_input(13).split("\n\n")
start_time = time.time()
answer = 0


def find_horizontal_reflection(map):
    height = len(map)
    width = len(map[0])
    for i in range(height - 1):
        low = i
        high = i + 1
        count = 0
        while low >= 0 and high <= height - 1:
            for j in range(width):
                if map[low][j] != map[high][j]:
                    count += 1
            low -= 1
            high += 1
            if count > 1:
                break
        if count == 1:
            print("horiz match on", i)
            for row in map:
                print(row)
            return i + 1
    return 0


def find_vertical_reflection(map):
    height = len(map)
    width = len(map[0])
    for i in range(width - 1):
        low = i
        high = i + 1
        count = 0
        while low >= 0 and high <= width - 1:
            for j in range(height):
                if map[j][low] != map[j][high]:
                    count += 1
            low -= 1
            high += 1
            if count > 1:
                break
        if count == 1:
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
