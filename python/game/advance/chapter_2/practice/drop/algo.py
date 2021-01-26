import pprint, copy


data_set = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 4, 0, 0],
    [2, 0, 1, 3, 3, 3, 4, 0],
    [0, 2, 2, 1, 1, 3, 0, 4],
    [0, 2, 2, 1, 1, 4, 3, 0],
    [2, 0, 1, 1, 1, 1, 4, 0],
    [0, 0, 0, 1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


temp = copy.deepcopy(data_set)


#가로
for y in range(10):
    for x in range(1, 7):
        if data_set[y][x] != 0:
            if (data_set[y][x-1] == data_set[y][x]) and (data_set[y][x+1] == data_set[y][x]):
                temp[y][x-1] = 7
                temp[y][x] = 7
                temp[y][x+1] = 7

#세로
for y in range(1, 9):
    for x in range(8):
        if data_set[y][x] != 0:
            if (data_set[y-1][x] == data_set[y][x]) and (data_set[y+1][x] == data_set[y][x]):
                temp[y-1][x] = 7
                temp[y][x] = 7
                temp[y+1][x] = 7

#대각선
for y in range(1, 9):
    for x in range(1, 7):
        if data_set[y][x] != 0:
            if (data_set[y-1][x+1] == data_set[y][x]) and (data_set[y+1][x-1] == data_set[y][x]):
                temp[y-1][x+1] = 7
                temp[y][x] = 7
                temp[y+1][x-1] = 7
            
            if (data_set[y-1][x-1] == data_set[y][x]) and (data_set[y+1][x+1] == data_set[y][x]):
                temp[y-1][x-1] = 7
                temp[y][x] = 7
                temp[y+1][x+1] = 7

pprint.pprint(temp)
        
