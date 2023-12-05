import advent
import re

inputs = advent.get_input(1).splitlines()
answer = 0

for this_input in inputs:
    print(this_input)
    first_digit = re.search(
        "\d|one|two|three|four|five|six|seven|eight|nine", this_input
    )[0]
    last_digit = re.match(
        "(.*)(\d|one|two|three|four|five|six|seven|eight|nine)", this_input
    ).groups()[1]
    for digit, word in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ):
        first_digit = first_digit.replace(word, str(digit + 1))
        last_digit = last_digit.replace(word, str(digit + 1))
    print(first_digit, last_digit)
    answer += int(first_digit + last_digit)

advent.clip(answer)
