import advent
import time

answer = 0
inputs = advent.re_input("(.)(.)(.)(.)(.) (\d*)", 7)
start_time = time.time()

print(inputs)


def get_hand_rank(hand):
    hand_dict = {}
    for card in hand:
        if hand_dict.get(card):
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1
    values = list(hand_dict.values())
    maxi = max(values)
    if maxi == 1:
        return "1" + "".join(hand)
    elif maxi == 2:
        if values.count(2) == 2:
            return "3" + "".join(hand)
        else:
            return "2" + "".join(hand)
    elif maxi == 3:
        if values.count(2) == 1:
            return "5" + "".join(hand)
        else:
            return "4" + "".join(hand)
    elif maxi == 4:
        return "6" + "".join(hand)
    elif maxi == 5:
        return "7" + "".join(hand)


bids = {}
for hand in inputs:
    new_hand = []
    for card in hand[:5]:
        new_hand.append(
            card.replace("A", "e")
            .replace("K", "d")
            .replace("Q", "c")
            .replace("J", "b")
            .replace("T", "a")
        )
    rank = get_hand_rank(new_hand[:5])
    bids[rank] = hand[5]

sorted_bids = dict(sorted(bids.items()))

idx = 1
for bid in sorted_bids.values():
    answer += int(bid) * idx
    idx += 1


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
