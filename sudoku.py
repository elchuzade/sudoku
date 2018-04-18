import numpy as np

input_state = [ 0,0,0,   0,0,0,   0,0,0,
                0,0,0,   0,1,0,   0,3,2,
                7,3,1,   5,0,0,   8,0,0,
                6,0,0,   0,0,8,   0,0,0,
                5,0,9,   0,2,0,   0,4,0,
                3,0,7,   0,0,5,   0,0,0,
                0,0,0,   0,0,1,   4,0,0,
                0,2,8,   0,4,3,   9,6,0,
                0,0,0,   0,0,0,   0,2,7 ]

next_state = input_state[:]

# Find all zero entries
def find_zeros(next_state):
    zeros = []
    for i in range(len(next_state)):
        if next_state[i] == 0:
            zeros.append(i)
    return zeros

# Find coordinates of zeros
def zeros_coordinates(zeros):
    coord_zeros = []
    for i in zeros:
        coord = []
        i_coord = i // 9
        j_coord = i % 9
        coord.append(i_coord)
        coord.append(j_coord)
        coord_zeros.append(coord)
    return coord_zeros

# Finding full row
def row(i, next_state):
    full_row = []
    row = i[0]
    begin = row * 9
    for i in range(9):
        full_row.append(next_state[begin])
        begin += 1
    return full_row

# Finding full column
def col(i, next_state):
    full_col = []
    col = i[1]
    begin = col
    for i in range(9):
        full_col.append(next_state[begin])
        begin += 9
    return full_col

# Finding full tribox
def box(i, next_state):
    box = []
    trirow = i[0] // 3
    tricol = i[1] // 3
    for i in range(3):
        first_index = trirow * 3 * 9 + tricol * 3 + i * 9
        second_index = first_index + 1
        third_index = second_index + 1
        box.append(next_state[first_index])
        box.append(next_state[second_index])
        box.append(next_state[third_index])
    return box

# Finding full info about all zeros
def zeros_info(i, next_state):
    value = [0]
    full_info = []
    full_row = row(i, next_state)
    full_col = col(i, next_state)
    tribox = box(i, next_state)
    info = []
    for number in range(9):
        number += 1
        if number not in full_row and number not in full_col and number not in tribox:
            info.append(number)
    full_info.append(i)
    full_info.append(info)
    full_info.append(value)
    return full_info

# creating a full state
def find_full_state(next_state, zeros_coord):
    result = []
    for i in zeros_coord:
        zeros = zeros_info(i, next_state)
        result.append(zeros)
    return result

# Solving with simple steps
def solve_one(next_state, full_state):
    subresult = []
    for i in full_state:
        index = i[0][0] * 9 + i[0][1]
        if len(i[1]) == 1:
            subresult.append(i)
            next_state[index] = i[1][0]
    return next_state

# Showing output
def fancy_output(value):
    print(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],)
    print(value[9],value[10],value[11],value[12],value[13],value[14],value[15],value[16],value[17])
    print(value[18],value[19],value[20],value[21],value[22],value[23],value[24],value[25],value[26])
    print(value[27],value[28],value[29],value[30],value[31],value[32],value[33],value[34],value[35])
    print(value[36],value[37],value[38],value[39],value[40],value[41],value[42],value[43],value[44])
    print(value[45],value[46],value[47],value[48],value[49],value[50],value[51],value[52],value[53])
    print(value[54],value[55],value[56],value[57],value[58],value[59],value[60],value[61],value[62])
    print(value[63],value[64],value[65],value[66],value[67],value[68],value[69],value[70],value[71])
    print(value[72],value[73],value[74],value[75],value[76],value[77],value[78],value[79],value[80])

# Finding all the possible values in empty cells of the row
def find_rows_all_pos_values(i, full_state):
    possible_values = []
    zeros_coordinates = []
    for j in full_state:
        if j[0][0] == i:
            zeros_coordinates.append(j[0])
            possible_values.append(j[1])
    return zeros_coordinates, possible_values

# Counting amount of each number from 1 to 9 in the current row
def find_row_pos_values(row_pos_values):
    result = []
    for i in range(9):
        sub_result = []
        i += 1
        count = 0
        for j in range(len(row_pos_values)):
            if i in row_pos_values[j]:
                count += 1
        sub_result.append(i)
        sub_result.append(count)
        result.append(sub_result)
    return result

# Finding all the possible values in empty cells of the column
def find_cols_all_pos_values(i, full_state):
    possible_values = []
    zeros_coordinates = []
    for j in full_state:
        if j[0][1] == i:
            zeros_coordinates.append(j[0])
            possible_values.append(j[1])
    return zeros_coordinates, possible_values

# Counting amount of each number from 1 to 9 in the current column
def find_col_pos_values(col_pos_values):
    result = []
    for i in range(9):
        sub_result = []
        i += 1
        count = 0
        for j in range(len(col_pos_values)):
            if i in col_pos_values[j]:
                count += 1
        sub_result.append(i)
        sub_result.append(count)
        result.append(sub_result)
    return result

# Finding all the possible values in empty cells of the box
def find_boxs_all_pos_values(i, full_state):
    trirow = i // 3
    tricol = i % 3
    possible_values = []
    zeros_coordinates = []
    for j in full_state:
        if j[0][0] // 3 == trirow and j[0][1] // 3 == tricol:
            zeros_coordinates.append(j[0])
            possible_values.append(j[1])
    return zeros_coordinates, possible_values

# Counting amount of each number from 1 to 9 in the current box
def find_box_pos_values(box_pos_values):
    result = []
    for i in range(9):
        sub_result = []
        i += 1
        count = 0
        for j in range(len(box_pos_values)):
            if i in box_pos_values[j]:
                count += 1
        sub_result.append(i)
        sub_result.append(count)
        result.append(sub_result)
    return result

# Assigning the value to the empty cell if that value has been found only once in its row's all possible values list
def row_solve_two(coordinates, row_pos_values, next_state, count_row_pos_values):
    for j in count_row_pos_values:
        if j[1] == 1:
            assign_value = j[0]
            for value in row_pos_values:
                if assign_value in value:
                    index = row_pos_values.index(value)
                    assign_coord = coordinates[index]
                    total_coord = assign_coord[0] * 9 + assign_coord[1]
                    next_state[total_coord] = assign_value
    return next_state

# Assigning the value to the empty cell if that value has been found only once in its col's all possible values list
def col_solve_two(coordinates, col_pos_values, next_state, count_col_pos_values):
    for j in count_col_pos_values:
        if j[1] == 1:
            assign_value = j[0]
            for value in col_pos_values:
                if assign_value in value:
                    index = col_pos_values.index(value)
                    assign_coord = coordinates[index]
                    total_coord = assign_coord[0] * 9 + assign_coord[1]
                    next_state[total_coord] = assign_value
    return next_state

# Assigning the value to the empty cell if that value has been found only once in its box's all possible values list
def box_solve_two(coordinates, box_pos_values, next_state, count_box_pos_values):
    for j in count_box_pos_values:
        if j[1] == 1:
            assign_value = j[0]
            for value in box_pos_values:
                if assign_value in value:
                    index = box_pos_values.index(value)
                    assign_coord = coordinates[index]
                    total_coord = assign_coord[0] * 9 + assign_coord[1]
                    next_state[total_coord] = assign_value
    return next_state


def easy(next_state):
    current_state = []
    while next_state != current_state:
        current_state = next_state[:]
        zeros = find_zeros(next_state)
        zeros_coord = zeros_coordinates(zeros)
        full_state = find_full_state(next_state, zeros_coord)
        next_state = solve_one(next_state, full_state)
    return next_state

def medium(next_state):
    zeros = find_zeros(next_state)
    zeros_coord = zeros_coordinates(zeros)
    full_state = find_full_state(next_state, zeros_coord)
    for i in range(9):
        coordinates, row_pos_values = find_rows_all_pos_values(i, full_state)
        count_row_pos_values = find_row_pos_values(row_pos_values)
        next_state = row_solve_two(coordinates, row_pos_values, next_state, count_row_pos_values)
    for i in range(9):
        coordinates, col_pos_values = find_cols_all_pos_values(i, full_state)
        count_col_pos_values = find_col_pos_values(col_pos_values)
        next_state = col_solve_two(coordinates, col_pos_values, next_state, count_col_pos_values)
    for i in range(9):
        coordinates, box_pos_values = find_boxs_all_pos_values(i, full_state)
        count_box_pos_values = find_box_pos_values(box_pos_values)
        next_state = box_solve_two(coordinates, box_pos_values, next_state, count_box_pos_values)
    return next_state


def hard(next_state):
    zeros = find_zeros(next_state)
    zeros_coord = zeros_coordinates(zeros)
    full_state = find_full_state(next_state, zeros_coord)
    for k in range(9):
        i = k
        coordinates, box_pos_values = find_boxs_all_pos_values(i, full_state)
        count_box_pos_values = find_box_pos_values(box_pos_values)
        for m in count_box_pos_values:
            if m[1] == 2 or m[1] == 3:
                pos_coord_box = []
                pos_values_box = []
                for y in full_state:
                    if y[0] in coordinates:
                        pos_coord_box.append(y[0])
                        pos_values_box.append(y[1])
                pos_coord_box_total = []
                pos_values_box_total = []
                iter = 0
                for ii in pos_values_box:
                    if m[0] in ii:
                        pos_coord_box_total.append(pos_coord_box[iter])
                        pos_values_box_total.append(ii)
                    iter += 1
                total_first_values = []
                total_second_values = []
                for r in pos_coord_box_total:
                    total_first_values.append(r[0])
                    total_second_values.append(r[1])
                unique_first_values = list(set(total_first_values))
                unique_second_values = list(set(total_second_values))
                row_col = -1
                row_col_index = -1
                if len(unique_first_values) == 1:
                    row_col = 0     # 0 means it is in a row
                    row_col_index = set(unique_first_values)
                    full_pos_values_row_box = []
                    whole_row =[]
                    for e in full_state:
                        if e[0] in pos_coord_box_total:
                            full_pos_values_row_box.append(e)
                        if e[0][0] == unique_first_values[0]:
                            whole_row.append(e)
                    excluded_row = []
                    for x in whole_row:
                        if x not in full_pos_values_row_box:
                            excluded_row.append(x)
                    for hhr in excluded_row:
                        if hhr in full_state:
                            row_index = full_state.index(hhr)
                            pos_values_update = hhr[1]
                            if m[0] in pos_values_update:
                                pos_values_update.remove(m[0])
                            full_state[row_index][1] = pos_values_update
                if len(unique_second_values) == 1:
                    row_col_index = set(unique_second_values)
                    full_pos_values_col_box = []
                    whole_col = []
                    for e in full_state:
                        if e[0] in pos_coord_box_total:
                            full_pos_values_col_box.append(e)
                        if e[0][1] == unique_second_values[0]:
                            whole_col.append(e)
                    excluded_col = []
                    for x in whole_col:
                        if x not in full_pos_values_col_box:
                            excluded_col.append(x)
                    for hhc in excluded_col:
                        if hhc in full_state:
                            col_index = full_state.index(hhc)
                            pos_values_update = hhc[1]
                            if m[0] in pos_values_update:
                                pos_values_update.remove(m[0])
                            full_state[col_index][1] = pos_values_update
    for i in range(9):
        coordinates, row_pos_values = find_rows_all_pos_values(i, full_state)
        count_row_pos_values = find_row_pos_values(row_pos_values)
        next_state = row_solve_two(coordinates, row_pos_values, next_state, count_row_pos_values)
    for i in range(9):
        coordinates, col_pos_values = find_cols_all_pos_values(i, full_state)
        count_col_pos_values = find_col_pos_values(col_pos_values)
        next_state = col_solve_two(coordinates, col_pos_values, next_state, count_col_pos_values)
    for i in range(9):
        coordinates, box_pos_values = find_boxs_all_pos_values(i, full_state)
        count_box_pos_values = find_box_pos_values(box_pos_values)
        next_state = box_solve_two(coordinates, box_pos_values, next_state, count_box_pos_values)
    return next_state



state = 0
while state != next_state:
    state = next_state[:]
    next_state = easy(next_state)
    next_state = medium(next_state)
    next_state = hard(next_state)

value = next_state
fancy_output(value)
print(next_state)
print('\n')
