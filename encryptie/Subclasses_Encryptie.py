# De S-Blok
s_blok = [[0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76],
          [0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0],
          [0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15],
          [0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75],
          [0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84],
          [0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf],
          [0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8],
          [0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2],
          [0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73],
          [0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb],
          [0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79],
          [0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08],
          [0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a],
          [0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e],
          [0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf],
          [0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]]

# De sleutel voor de vercijfering van de code
Key = [[72, 109, 105, 133, 58, 87, 62, 187, 217, 142, 176, 11, 235, 101, 213, 222, 253, 152, 77, 147, 239, 119, 58, 169, 29, 106, 80, 249, 179, 217, 137, 112, 190, 103, 238, 158, 94, 57, 215, 73, 131, 186, 109, 36],
       [51, 225, 149, 143, 27, 250, 111, 224, 81, 171, 196, 36, 162, 9, 205, 233, 71, 78, 131, 106, 216, 150, 21, 127, 101, 243, 230, 153, 56, 203, 45, 180, 49, 250, 215, 99, 114, 136, 95, 60, 156, 20, 75, 119],
       [41, 170, 249, 238, 225, 75, 178, 92, 219, 144, 34, 126, 230, 118, 84, 42, 102, 16, 68, 110, 247, 231, 163, 205, 4, 227, 64, 141, 110, 141, 205, 64, 100, 233, 36, 100, 48, 217, 253, 153, 173, 116, 137, 16],
       [244, 208, 160, 177, 99, 179, 19, 162, 137, 58, 41, 139, 162, 152, 177, 58, 191, 39, 150, 172, 99, 68, 210, 126, 176, 244, 38, 88, 41, 221, 251, 163, 120, 165, 94, 253, 115, 214, 136, 117, 72, 158, 22, 99]]
# De code voor het maken van de tag
MAC = [[26, 177, 2, 63, 57, 136, 138, 181, 170, 34, 168, 29, 204, 238, 70, 91, 186, 84, 18, 73, 58, 110, 124, 53, 229, 139, 247, 194, 59, 176, 71, 133, 15, 191, 248, 125, 32, 159, 103, 26, 12, 147, 244, 238],
       [238, 172, 251, 148, 111, 195, 56, 172, 252, 63, 7, 171, 25, 38, 33, 138, 27, 61, 28, 150, 202, 247, 235, 125, 190, 73, 162, 223, 242, 187, 25, 198, 76, 247, 238, 40, 114, 133, 107, 67, 25, 156, 247, 180],
       [75, 169, 240, 145, 234, 67, 179, 34, 248, 187, 8, 42, 243, 72, 64, 106, 51, 123, 59, 81, 219, 160, 155, 202, 172, 12, 151, 93, 156, 144, 7, 90, 28, 140, 139, 209, 211, 95, 212, 5, 135, 216, 12, 9],
       [77, 186, 74, 241, 56, 130, 200, 57, 237, 111, 167, 158, 73, 38, 129, 31, 112, 86, 215, 200, 75, 29, 202, 2, 221, 192, 10, 8, 248, 56, 50, 58, 111, 87, 101, 95, 144, 199, 162, 253, 50, 245, 87, 170]]


### Make zero-state
def MakeZeroState():
    matrix = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    return matrix

### Gebruik van een gegeven nummer in de counter
def MakeCTR(number):
    matrix = MakeZeroState()
    result = ""
    for k in range(127,-1,-1):
        if 2**k <= number:
            result += "1"
            number -= 2**k
        else:
            result += "0"
    for j in range(16):
        string = result[j*8:j*8+8]
        byte = 0
        for number in range(8):
            if string[number] == '1':
                byte += 2**(7-number)
        matrix[j%4][j//4] = byte
    return matrix


### Create state
def CreateState(counter):
    state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in range(4):
        for column in range(4):
            state[row][column] = counter[row][column]
    return state


### Sub-bytes
def SubBytes(matrix):
    for row in range(4):
        for column in range(4):
            hexa = matrix[row][column]
            x_coordinate = hexa//16
            y_coordinate = hexa%16
            matrix[row][column] = s_blok[x_coordinate][y_coordinate]
    return matrix


### Inverse Sub-bytes
def InvSubBytes(matrix):
    for row in range(4):
        for column in range(4):
            asked = matrix[row][column]
            for row_2 in s_blok:
                if asked in row_2:
                    X = s_blok.index(row_2)
                    Y = row_2.index(asked)
                    number = X*16+Y
                    matrix[row][column] = number
    return matrix


### Shift-rows
def ShiftRows(matrix):
    for i in range(4):
        first = matrix[i][:i]
        second = matrix[i][i:]
        matrix[i] = second+first
    return matrix


### Inverse shift-rows
def InvShiftRows(matrix):
    for i in range(4):
        first = matrix[i][:(4-i)]
        second = matrix[i][(4-i):]
        matrix[i] = second+first
    return matrix


### Mix columns
def MixColumns(matrix):
    for place_x in range(4):
        column = []
        for place_y in range(4):
            column += [matrix[place_y][place_x]]
        mixColumn(column)
        for place_y in range(4):
            matrix[place_y][place_x] = column[place_y]
    return matrix

def vermenigvuldigen(x,y):
    if y == 1:
        return x
    elif y == 2:
        if x>=128:
            return ((x << 1) % 256) ^ 0x1b
        else:
            return ((x << 1) % 256)
    else:
        result = vermenigvuldigen(x,2) ^ x
        return result

def mixColumn(column):
    temp = []
    for i in range(len(column)):
        temp += [0]
    temp[0] = vermenigvuldigen(column[0],2) ^ vermenigvuldigen(column[3],1) ^ \
              vermenigvuldigen(column[2],1) ^ vermenigvuldigen(column[1],3)
    temp[1] = vermenigvuldigen(column[1],2) ^ vermenigvuldigen(column[0],1) ^ \
                vermenigvuldigen(column[3],1) ^ vermenigvuldigen(column[2],3)
    temp[2] = vermenigvuldigen(column[2],2) ^ vermenigvuldigen(column[1],1) ^ \
                vermenigvuldigen(column[0],1) ^ vermenigvuldigen(column[3],3)
    temp[3] = vermenigvuldigen(column[3],2) ^ vermenigvuldigen(column[2],1) ^ \
                vermenigvuldigen(column[1],1) ^ vermenigvuldigen(column[0],3)
    for i in range(len(column)):
        column[i] = temp[i]


### Add round key
def AddRoundKey(matrix,key,i):
    for row in range(4):
        for column in range(4):
            matrix[row][column] = matrix[row][column] ^ key[row][column+i*4]
    return matrix


### Expand the key
def KeySchedule(key):
    CreateEmptyKey(key)
    for i in range(4,44): #range (4,44) !
        if i%4 == 0:
            woord = RotWord(key,i)
            SubWord(woord)
            XorSpecial(key,i,woord)
        else:
            Xor(key,i)

Rcon = [[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36],
        [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
        [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
        [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]]

def CreateEmptyKey(CipherKey):
    for row in range(4):
        CipherKey[row] = CipherKey[row] +[0,]*40
    return CipherKey

def RotWord(key,i):
    woord = [key[1][i-1],key[2][i-1],key[3][i-1],key[0][i-1]]
    return woord

def SubWord(woord):
    for position in range(4):
        hexa = woord[position]
        x_coordinate = hexa//16
        y_coordinate = hexa%16
        woord[position] = s_blok[x_coordinate][y_coordinate]

def XorSpecial(key,i,woord):
    for row in range(4):
        key[row][i] = key[row][i-4] ^ woord[row] ^ Rcon[row][i//4-1]

def Xor(key,i):
    for row in range(4):
        key[row][i] = key[row][i-4] ^ key[row][i-1]


### Implementeer de boodschap
def ImplementMessage(Encryption,Message):
    for row in range(4):
        for column in range(4):
            Encryption[row][column] = Encryption[row][column] ^ Message[row][column]
    return Encryption