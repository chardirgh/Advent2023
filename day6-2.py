import advent
import time
import re

answer = 0
inputs = advent.get_input(6).splitlines()
start_time = time.time()

race_time = int(re.sub("\D", "", inputs[0]))
record = int(re.sub("\D", "", inputs[1]))
print(race_time)
print(record)

speed = 0
while speed < race_time:
    distance = speed * (race_time - speed)
    if distance > record:
        answer += 1
    speed += 1

advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
