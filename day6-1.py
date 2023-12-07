import advent
import time

answer = 1
inputs = advent.get_input(6).splitlines()
start_time = time.time()

times = [int(t) for t in inputs[0].split()[1:]]
records = [int(t) for t in inputs[1].split()[1:]]
print(times)
print(records)

for idx, race_time in enumerate(times):
    speed = 0
    wins = 0
    while speed < race_time:
        distance = speed * (race_time - speed)
        if distance > records[idx]:
            wins += 1
        speed += 1
    answer = answer * wins


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
