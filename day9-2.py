import advent
import time

inputs = advent.get_input(9).splitlines()
start_time = time.time()
answer = 0

for row in inputs:
    sequences = [[int(x) for x in row.split()]]
    while not all([x == 0 for x in sequences[-1]]):
        sequences.append([])
        for y in range(len(sequences[-2]) - 1):
            sequences[-1].append(sequences[-2][y + 1] - sequences[-2][y])
    print(sequences)
    extrapolated = [0]
    for seq in reversed(sequences):
        extrapolated.append(seq[0] - extrapolated[-1])
    print(extrapolated)
    answer += extrapolated[-1]


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
