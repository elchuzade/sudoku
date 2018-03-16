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
    values_list = []
    for i in range(9):
        for j in range(9):
            cell_value = input('type in the value for X ' + str(i+1) + str(j+1) + ' - ')
            values_list.append(int(cell_value))
    return values_list



values_list = input_board(i,j)
print(values_list)
