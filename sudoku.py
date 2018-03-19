import numpy as np

'''

x00 x01 x02   x03 x04 x05   x06 x07 x08
x10 x11 x12   x13 x14 x15   x16 x17 x18
x20 x21 x22   x23 x24 x25   x26 x27 x28

x30 x31 x32   x33 x34 x35   x36 x37 x38
x40 x41 x42   x43 x44 x45   x46 x47 x48
x50 x51 x52   x53 x54 x55   x56 x57 x58

x60 x61 x62   x63 x64 x65   x66 x67 x68
x70 x71 x72   x73 x74 x75   x76 x77 x78
x80 x81 x82   x83 x84 x85   x86 x87 x88

'''

'''

x68 = [6,8,0, 1,2,3,4,5,6,7,8,9]
       i j v   possible values

'''

i, j = 0, 0

# Asking user to make an input of the board
def input_board(i,j):
    result = []
    values_list = []
    i_list = []
    j_list = []
    for i in range(9):
        for j in range(9):
            cell_value = input('type in the value for X ' + str(i+1) + str(j+1) + ' - ')
            values_list.append(int(cell_value))
    return values_list

# Fake input

# lets turn 4 into 0 row5 col4
values_list = [ 9,3,4,   7,6,5,   2,1,8,
                2,7,6,   9,8,1,   3,5,4,
                8,5,1,   2,3,4,   6,7,9,

                6,9,2,   5,1,3,   4,8,7,
                4,8,3,   6,7,9,   5,2,1,
                7,1,5,   8,0,2,   9,6,3,

                3,4,7,   1,2,6,   8,9,5,
                1,2,9,   3,5,8,   7,4,6,
                5,6,8,   4,9,7,   1,3,2 ]

# show fake input that will be used for future coding
print(values_list)

'''
x68 = 5
order = 62
9*6 + 8
'''

# Find an ijv list from the values_list with all i and j and v included
def ijv_finder(values_list, index):
    ijv_list = []
    v = values_list[index]
    i = index // 9
    j = index % 9
    ijv_list.append(i)
    ijv_list.append(j)
    ijv_list.append(v)
    return ijv_list

# Make a whole state of ijv lists
def ijv_state_maker(values_list):
    ijv_state = []
    for index in range(81):
        ijv_list = ijv_finder(values_list, index)
        ijv_state.append(ijv_list)
    return ijv_state

# Index finder from its i and j coordinates
def index_finder(i_index, j_index):
    return i_index * 9 + j_index

# Finding the row to the West of the current cell including current cell
def row_west(ijv_state, current_cell_index):
    result = []
    current_cell = ijv_state[current_cell_index]
    i_index = current_cell[0]
    j_index = current_cell[1]
    v_index = current_cell[2]
    result.append(v_index)
    while j_index > 0:
        j_index -= 1
        index = index_finder(i_index, j_index)
        current_cell = ijv_state[index]
        v_index = current_cell[2]
        result.append(v_index)
    result.reverse()
    return result

# Finding the row to the East of the current cell excluding current cell
def row_east(ijv_state, current_cell_index):
    result = []
    current_cell = ijv_state[current_cell_index]
    i_index = current_cell[0]
    j_index = current_cell[1]
    v_index = current_cell[2]
    while j_index < 8:
        j_index += 1
        index = index_finder(i_index, j_index)
        current_cell = ijv_state[index]
        v_index = current_cell[2]
        result.append(v_index)
    return result

def full_row(ijv_state, current_cell_index):
    result, rw_east, rw_west = [], [], []
    rw_east = row_east(ijv_state, current_cell_index)
    rw_west = row_west(ijv_state, current_cell_index)
    result.extend(rw_west)
    result.extend(rw_east)
    return result

# Finding the column to the North of the current cell including current cell
def col_north(ijv_state, current_cell_index):
    result = []
    current_cell = ijv_state[current_cell_index]
    i_index = current_cell[0]
    j_index = current_cell[1]
    v_index = current_cell[2]
    result.append(v_index)
    while i_index > 0:
        i_index -= 1
        index = index_finder(i_index, j_index)
        current_cell = ijv_state[index]
        v_index = current_cell[2]
        result.append(v_index)
    result.reverse()
    return result


# Finding the column to the South of the current cell excluding current cell
def col_south(ijv_state, current_cell_index):
    result = []
    current_cell = ijv_state[current_cell_index]
    i_index = current_cell[0]
    j_index = current_cell[1]
    v_index = current_cell[2]
    while i_index < 8:
        i_index += 1
        index = index_finder(i_index, j_index)
        current_cell = ijv_state[index]
        v_index = current_cell[2]
        result.append(v_index)
    return result

def full_col(ijv_state, current_cell_index):
    result, cl_north, cl_south = [], [], []
    cl_north = col_north(ijv_state, current_cell_index)
    cl_south = col_south(ijv_state, current_cell_index)
    result.extend(cl_north)
    result.extend(cl_south)
    return result

# Finding a tricol of the current cell
def tribox(ijv_state, current_cell_index):
    result = []
    result_index = []
    current_cell = ijv_state[current_cell_index]
    i_index = current_cell[0]
    j_index = current_cell[1]
    trirow = i_index // 3    # i value of a tribox among all 9 triboxes = 1
    tricol = j_index // 3    # j value of a tribox among all 9 triboxes = 1
    for n in range(3):
        first_index = trirow * 3 * 9 + tricol * 3 + n * 9
        second_index = first_index + 1
        third_index = second_index + 1
        result_index.append(first_index)
        result_index.append(second_index)
        result_index.append(third_index)
    for i in result_index:
        value_list = ijv_state[i]
        value = value_list[2]
        result.append(value)
    return result

# Combine the impossible values for a current cell from its row column and box
def unique_numbers(full_row, full_col, tribox):
    result, total_list = [], []
    total_list.extend(full_row)
    total_list.extend(full_col)
    total_list.extend(tribox)
    for x in total_list:
        if x not in result:
            result.append(x)
    return result

def constraint1(full_row, full_col, tribox):
    impossible_values = unique_numbers(full_row, full_col, tribox)
    all_values = [0,1,2,3,4,5,6,7,8,9]
    pos_values = np.setdiff1d(all_values, impossible_values)
    return pos_values




ijv_state = ijv_state_maker(values_list)
current_cell_index = 49
print(ijv_state)
print('\n')
full_row = full_row(ijv_state, current_cell_index)
print('full row', full_row)
full_col = full_col(ijv_state, current_cell_index)
print('full col', full_col)
tribox = tribox(ijv_state, current_cell_index)
print('tribox', tribox)
pos_values = constraint1(full_row, full_col, tribox)
print('pos values', pos_values)




#values_list = input_board(i,j)
#print(values_list)
