import advent
import time
import re

inputs = advent.get_input(15).replace("\n", "").split(",")
start_time = time.time()
answer = 0


def get_hash(value):
    hash_value = 0
    for char in value:
        hash_value += ord(char)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


boxes = {}

for i in inputs:
    parse = re.match("([^-=]*?)([-=])(\d?)", i).groups()
    code = parse[0]
    box = get_hash(code)
    op = parse[1]
    focal_length = int(parse[2] or 0)
    lens = {"code": code, "focal_length": focal_length}
    if op == "=":
        if boxes.get(box):
            found = False
            for b in boxes[box]:
                if b["code"] == code:
                    b["focal_length"] = focal_length
                    found = True
            if not found:
                boxes[box].append(lens)
        else:
            boxes[box] = [lens]
    else:
        new_box = []
        if boxes.get(box):
            for b in boxes[box]:
                if b["code"] != parse[0]:
                    new_box.append(b)
        boxes[box] = new_box

for box_no, box in boxes.items():
    for idx, lens in enumerate(box):
        answer += (box_no + 1) * (idx + 1) * lens["focal_length"]


advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
