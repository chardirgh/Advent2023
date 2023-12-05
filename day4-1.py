import advent

inputs = advent.re_input(
    "Card ...: (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) \| (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..)",
    4,
)
answer = 0

for this_input in inputs:
    score = 0
    winners = [int(num) for num in this_input[:10]]
    numbers = [int(num) for num in this_input[10:]]
    for test in numbers:
        if test in winners:
            if score > 0:
                score *= 2
            else:
                score =1
    answer += score


advent.clip(answer)
