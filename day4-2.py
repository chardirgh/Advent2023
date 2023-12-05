import advent

inputs = advent.re_input(
    "Card ...: (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) \| (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..) (..)",
    4,
)
answer = 0
cards = [1 for card in inputs]

for card, this_input in enumerate(inputs):
    score = 0
    winners = [int(num) for num in this_input[:10]]
    numbers = [int(num) for num in this_input[10:]]
    for test in numbers:
        if test in winners:
            score += 1
    for x in range(card + 1, card + 1 + score):
        cards[x] = cards[x] + cards[card]

answer = sum(cards)

advent.clip(answer)
