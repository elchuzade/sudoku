from random import randint
import last_version


input_state = []
for i in range(81):
    input_state.append(0)


def ij_find(index):
    i = index // 9
    j = index % 9
    ij = []
    ij.append(i)
    ij.append(j)
    return ij


def value_find(state, index):
    val = state[index]
    return val


def rowval(state, ij):
    row = []
    row_index = ij[0]
    row_index = row_index * 9
    for i in range(9):
        row.append(state[row_index])
        row_index += 1
    return row


def colval(state, ij):
    col = []
    col_index = ij[1]
    for i in range(9):
        col.append(state[col_index])
        col_index += 9
    return col


def boxval(ij, state):
    box = []
    turow = ij[0] // 3
    tucol = ij[1] // 3
    for i in range(3):
        first_index = turow * 3 * 9 + tucol * 3 + i * 9
        second_index = first_index + 1
        third_index = second_index + 1
        box.append(state[first_index])
        box.append(state[second_index])
        box.append(state[third_index])
    return box


def posvalues_find(ij, row, col, box):
    posval = []
    all_values = [1,2,3,4,5,6,7,8,9]
    for i in all_values:
        if i not in row and i not in col and i not in box:
            posval.append(i)
    return posval


def assign_value(state, ij, pos_val):
    num = randint(0, len(pos_val)-1)
    value = pos_val[num]
    index = ij[0] * 9 + ij[1]
    state[index] = value
    return state


def solve(state):
    for index in range(81):
        ij = ij_find(index)
        row = rowval(state, ij)
        col = colval(state, ij)
        box = boxval(ij, state)
        pos_val = posvalues_find(ij, row, col, box)
        if len(pos_val) > 0:
            state = assign_value(state, ij, pos_val)


def fancy_output(state):
    print(state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8],)
    print(state[9],state[10],state[11],state[12],state[13],state[14],state[15],state[16],state[17])
    print(state[18],state[19],state[20],state[21],state[22],state[23],state[24],state[25],state[26])
    print(state[27],state[28],state[29],state[30],state[31],state[32],state[33],state[34],state[35])
    print(state[36],state[37],state[38],state[39],state[40],state[41],state[42],state[43],state[44])
    print(state[45],state[46],state[47],state[48],state[49],state[50],state[51],state[52],state[53])
    print(state[54],state[55],state[56],state[57],state[58],state[59],state[60],state[61],state[62])
    print(state[63],state[64],state[65],state[66],state[67],state[68],state[69],state[70],state[71])
    print(state[72],state[73],state[74],state[75],state[76],state[77],state[78],state[79],state[80])


state = input_state[:]
zeros = state.count(0)
while zeros > 0:
    state = input_state[:]
    solve(state)
    zeros = state.count(0)


fancy_output(state)
k = 0
hide_state = state[:]

nozero_state = []
count = 0
for i in state:
    substate = []
    if i != 0:
        substate.append(i)
        substate.append(count)
        nozero_state.append(substate)
    count += 1
print('length - ',len(nozero_state))
print('nozero - ',nozero_state)

while k < 81:
    numb = randint(0,len(nozero_state)-1)
    print('numb - ',numb)
    value = nozero_state[numb]
    x = value[1]
    print('value to delete - ',hide_state[x])
    y = hide_state[x]
    hide_state[x] = 0

    some_state = hide_state[:]
    solved_state = last_version.sudoku(some_state)
    if solved_state.count(0) < 1:
        state = hide_state[:]
        print('its cool')
        nozero_state.pop(numb)
    else:
        hide_state[x] = y
        nozero_state.pop(numb)
    print('solution - ',solved_state)
    print('state - ',state)
    print('hide state',hide_state)

    k += 1
    print(k)
print('\n',state, '\n')
fancy_output(state)
print('\n')
