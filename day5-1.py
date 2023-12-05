import advent

inputs = advent.get_input(5).split("\n\n")
answer = 100000000000
seeds = [int(seed) for seed in inputs[0].split(" ")[1:]]
maps = []

for map in inputs[1:]:
    parse = map.splitlines()
    maps.append([])
    for row in parse[1:]:
        elements = row.split()
        dest_start = int(elements[0])
        source_start = int(elements[1])
        source_range = int(elements[2])
        maps[-1].append([source_start, source_range, (dest_start - source_start)])


for seed in seeds:
    print(seed)
    for map in maps:
        for row in map:
            if seed >= row[0] and seed < row[0] + row[1]:
                seed += row[2]
                break
    print("maps to", seed)
    if seed < answer:
        answer = seed


advent.clip(answer)
