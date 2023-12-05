import advent

inputs = advent.get_input(5).split("\n\n")
answer = 0
seeds = [int(seed) for seed in inputs[0].split(" ")[1:]]
print(seeds)
seed_ranges = []
seed_ranges.append([seeds[0], seeds[1]])
seed_ranges.append([seeds[2], seeds[3]])
seed_ranges.append([seeds[4], seeds[5]])
seed_ranges.append([seeds[6], seeds[7]])
seed_ranges.append([seeds[8], seeds[9]])
seed_ranges.append([seeds[12], seeds[13]])
seed_ranges.append([seeds[14], seeds[15]])
seed_ranges.append([seeds[16], seeds[17]])
seed_ranges.append([seeds[18], seeds[19]])
print(seed_ranges)

maps = []

for map in inputs[1:]:
    parse = map.splitlines()
    maps.append([])
    for row in parse[1:]:
        elements = row.split()
        dest_start = int(elements[0])
        source_start = int(elements[1])
        dest_range = int(elements[2])
        maps[-1].append([dest_start, dest_range, (source_start - dest_start)])

print(maps)

success = False
location = 0
while not success:
    location += 1
    if location % 1000 == 0:
        print(location, "to be tested")
    candidate = location
    for map in reversed(maps):
        for row in map:
            if candidate >= row[0] and candidate < row[0] + row[1]:
                candidate += row[2]
                break
    for seed_range in seed_ranges:
        if candidate >= seed_range[0] and candidate < seed_range[0] + seed_range[1]:
            answer = location
            success = True
            break


advent.clip(answer)
