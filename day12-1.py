import advent
import time
import re

inputs = advent.re_input("(.*?) (.*)", 12)
start_time = time.time()
answer = 0


def count_arrangements(pattern, groups, used_pattern, pattern_regex):
    if len(groups) == 0:
        if "#" in pattern:
            return 0
        result = used_pattern + "." * len(pattern)
        print(result, ("OK" if re.match(pattern_regex, result) else "BAD"))
        return 1

    first_group = groups[0]
    if len(pattern) < first_group:
        return 0

    if len(groups) == 1:
        if len(pattern) == first_group and not ("." in pattern):
            result = used_pattern + "#" * first_group
            print(result, ("OK" if re.match(pattern_regex, result) else "BAD"))
            return 1

    if pattern[0] == ".":
        return count_arrangements(
            pattern[1:], groups, used_pattern + ".", pattern_regex
        )

    if pattern[0] == "#":
        if "." in pattern[0:first_group]:
            return 0
        if len(pattern) > first_group and pattern[first_group] == "#":
            return 0
        return count_arrangements(
            pattern[first_group + 1 :],
            groups[1:],
            used_pattern + ("#" * first_group) + ".",
            pattern_regex,
        )

    if not ("." in pattern[0:first_group]) and (
        len(pattern) == first_group or pattern[first_group] != "#"
    ):
        retVal = count_arrangements(
            pattern[first_group + 1 :],
            groups[1:],
            used_pattern + ("#" * first_group) + ".",
            pattern_regex,
        )
        retVal += count_arrangements(
            pattern[1:], groups, used_pattern + ".", pattern_regex
        )
        return retVal

    return count_arrangements(pattern[1:], groups, used_pattern + ".", pattern_regex)


for pattern, groups in inputs:
    print("---------------------------------")
    pattern_regex = pattern.replace(".", "\.").replace("?", ".")
    groups = [int(x) for x in groups.split(",")]
    print(pattern, groups)

    test = count_arrangements(pattern, groups, "", pattern_regex)
    print(test)
    answer += test


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
