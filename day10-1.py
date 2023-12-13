import advent
import time

inputs = advent.get_input(10).splitlines()
start_time = time.time()
answer = 0

width = len(inputs[0])
height = len(inputs)

for y in range(height):
    for x in range(width):
        if inputs[y][x]=="S":
            start_x = x
            start_y = y

print(start_y,start_x)
path = [[start_y,start_x],[start_y+1,start_x]]

pipe = inputs[path[-1][0]][path[-1][1]]
while pipe!="S":
    y = path[-1][0]
    x = path[-1][1]
    pre_y = path[-2][0]
    pre_x = path[-2][1]
    pipe = inputs[y][x]
    print(pipe)
    match pipe:
        case "|":
            if pre_y == y-1:
                path.append([y+1,x])
            else:
                path.append([y-1,x])
        case "-":
            if pre_x == x-1:
                path.append([y,x+1])
            else:
                path.append([y,x-1])
        case "L":
            if pre_y == y-1:
                path.append([y,x+1])
            else:
                path.append([y-1,x])
        case "J":
            if pre_y == y-1:
                path.append([y,x-1])
            else:
                path.append([y-1,x])
        case "7":
            if pre_x == x-1:
                path.append([y+1,x])
            else:
                path.append([y,x-1])
        case "F":
            if pre_x == x+1:
                path.append([y+1,x])
            else:
                path.append([y,x+1])
    
    #print(path)

answer=(len(path)-1)/2




advent.clip(answer)
print("--- %s seconds ---" % (time.time() - start_time))
