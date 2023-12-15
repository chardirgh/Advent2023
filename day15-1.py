import advent
import time

inputs = advent.get_input(15).replace("\n", "").split(",")
start_time = time.time()
answer = 0

for i in inputs:
    hash_value = 0
    for char in i:
        hash_value += ord(char)
        hash_value *= 17
        hash_value = hash_value % 256
    answer += hash_value


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
