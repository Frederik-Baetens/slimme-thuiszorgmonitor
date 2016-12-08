# De S-Blok
s_blok = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
          [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
          [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
          [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
          [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
          [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
          [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
          [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
          [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
          [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
          [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
          [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
          [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
          [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
          [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
          [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

# De inverse van de S-blok
inv_s_blok =  [[0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
               [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
               [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
               [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
               [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
               [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
               [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
               [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
               [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
               [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
               [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
               [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
               [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
               [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
               [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
               [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]]


# De sleutel voor de vercijfering van de code
Key = [[72, 109, 105, 133, 58, 87, 62, 187, 217, 142, 176, 11, 235, 101, 213, 222, 253, 152, 77, 147, 239, 119, 58, 169, 29, 106, 80, 249, 179, 217, 137, 112, 190, 103, 238, 158, 94, 57, 215, 73, 131, 186, 109, 36],
       [51, 225, 149, 143, 27, 250, 111, 224, 81, 171, 196, 36, 162, 9, 205, 233, 71, 78, 131, 106, 216, 150, 21, 127, 101, 243, 230, 153, 56, 203, 45, 180, 49, 250, 215, 99, 114, 136, 95, 60, 156, 20, 75, 119],
       [41, 170, 249, 238, 225, 75, 178, 92, 219, 144, 34, 126, 230, 118, 84, 42, 102, 16, 68, 110, 247, 231, 163, 205, 4, 227, 64, 141, 110, 141, 205, 64, 100, 233, 36, 100, 48, 217, 253, 153, 173, 116, 137, 16],
       [244, 208, 160, 177, 99, 179, 19, 162, 137, 58, 41, 139, 162, 152, 177, 58, 191, 39, 150, 172, 99, 68, 210, 126, 176, 244, 38, 88, 41, 221, 251, 163, 120, 165, 94, 253, 115, 214, 136, 117, 72, 158, 22, 99]]
# De sleutel voor het aanmaken van de tag
MAC = [[26, 177, 2, 63, 57, 136, 138, 181, 170, 34, 168, 29, 204, 238, 70, 91, 186, 84, 18, 73, 58, 110, 124, 53, 229, 139, 247, 194, 59, 176, 71, 133, 15, 191, 248, 125, 32, 159, 103, 26, 12, 147, 244, 238],
       [238, 172, 251, 148, 111, 195, 56, 172, 252, 63, 7, 171, 25, 38, 33, 138, 27, 61, 28, 150, 202, 247, 235, 125, 190, 73, 162, 223, 242, 187, 25, 198, 76, 247, 238, 40, 114, 133, 107, 67, 25, 156, 247, 180],
       [75, 169, 240, 145, 234, 67, 179, 34, 248, 187, 8, 42, 243, 72, 64, 106, 51, 123, 59, 81, 219, 160, 155, 202, 172, 12, 151, 93, 156, 144, 7, 90, 28, 140, 139, 209, 211, 95, 212, 5, 135, 216, 12, 9],
       [77, 186, 74, 241, 56, 130, 200, 57, 237, 111, 167, 158, 73, 38, 129, 31, 112, 86, 215, 200, 75, 29, 202, 2, 221, 192, 10, 8, 248, 56, 50, 58, 111, 87, 101, 95, 144, 199, 162, 253, 50, 245, 87, 170]]


### Een vier op vier nul-matrix
ZeroStateEnc = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

ZeroStateDec = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]


def MakeCTR(number):
    """
      Een nummer (de counter) wordt omgezet in een vier op vier matrix.

    :param number: Een getal tussen de 0 en de 2**128-1
    :return matrix: 4x4-matrix
    """
    lijst = []
    matrix = []
    teller = 0
    while number is not 0:
        if number <= 255:
            lijst.append(number)
            teller += 1
            number = 0
        else:
            lijst.append(number%256)
            number = number//256
            teller += 1

    while teller < 16:
        lijst.append(0)
        teller += 1

    for position in range(4):
        matrix.append(lijst[position*4:position*4+4])

    return matrix


def SubBytes(matrix):
    """
      De 16 elementen (de bytes) in de 4x4-matrix worden één voor één getransformeerd via de S-blok.

    :param matrix: 4x4-matrix
    :return matrix: 4x4-matrix
    """
    for row in range(4):
        for column in range(4):
            hexa = matrix[row][column]
            matrix[row][column] = s_blok[hexa//16][hexa%16]
    return matrix


def InvSubBytes(matrix):
    """
      Het tegengestelde van de functie 'SubBytes'.

    :param matrix: 4x4-matrix
    :return matrix: 4x4-matrix
    """
    for row in range(4):
        for column in range(4):
            hexa = matrix[row][column]
            matrix[row][column] = inv_s_blok[hexa//16][hexa%16]
    return matrix


def ShiftRows(matrix):
    """
      Schuift de k-de rij, k posities op naar links. De rijen gaan van 0 tot 3.

    :param matrix: 4x4-matrix
    :return matrix: 4x4-matrix
    """
    return [matrix[x][x:]+matrix[x][:x] for x in range(4)]


def InvShiftRows(matrix):
    """
      Schuift de k-de rij, k posities op naar rechts. De rijen gaan van 0 tot 3.

    :param matrix: 4x4-matrix
    :return matrix: 4x4-matrix
    """
    return [matrix[x][(4-x):]+matrix[x][:(4-x)] for x in range(4)]


def MixColumns(matrix):
    """
      Deze functie vermenigvuldigt elke kolom van de matrix met een gegeven matrix.
      De gegeven matrix: [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

    :param matrix: 4x4-matrix
    :return matrix: 4x4-matrix
    """
    for place_x in range(4):
        column = [matrix[place_y][place_x] for place_y in range(4)]
        mixColumn(column)
        for place_y in range(4):
            matrix[place_y][place_x] = column[place_y]
    return matrix

def vermenigvuldigen(x,y):
    """
      De modulo-vermenigvuldiging.

    :param x: Getal (byte) in de kolom
    :param y: Constantes uit de gegeven matrix (zie functie 'MixColumns')
    :return: De gegeven byte (x) modulo-vermenigvuldigd met constante y
    """
    if y == 1:
        return x
    elif y == 2:
        if x>=128:
            return ((x << 1) % 256) ^ 0x1b
        else:
            return ((x << 1) % 256)
    else:
        return (vermenigvuldigen(x,2) ^ x)

def mixColumn(column):
    """
      Behoort tot de functie 'MixColumns' en maakt gebruik van de functie 'vermenigvuldigen'
    """
    temp = [0]*len(column)
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


def AddRoundKey(matrix,key,i):
    """
      Telt bij elke kolom van de blok een kolom van de sleutel bij op.

    :param matrix: 4x4-matrix
    :param key: Vooraf bepaalde sleutel, bovenaan in dit bestand te vinden
    :param i: Geeft aan welke 4x4-blok van de gehele 4x44-matrix gebruikt moet worden
    :return matrix: De bewerkte 4x4-matrix matrix
    """
    for row in range(4):
        for column in range(4):
            matrix[row][column] = matrix[row][column] ^ key[row][column+i*4]
    return matrix


def ImplementMessage(Encryption,Message):
    """
      Implementeer de matrix bekomen via de encryptie op de gegeven boodschap

    :param Encryption: 4x4-geincrypteerde-matrix
    :param Message: 4x4-matrix
    """
    for row in range(4):
        for column in range(4):
            Encryption[row][column] = Encryption[row][column] ^ Message[row][column]


def ListToBlok(List):
    """
      Zet een lijst van 16 elementen om in een 4x4-matrix van 16 bytes

    :param List: Een lijst van 16 cijfers met waarden tussen de 0 en de 255
    :return: 4x4-matrix
    """
    return [List[:4],List[4:8],List[8:12],List[12:16]]


def BlokToList(matrix):
    """
      Zet een 4x4-matrix terug om naar een lijst van 16 cijfers

    :param matrix: 4x4-matrix
    :return: Een lijst van 16 cijfers
    """
    return [matrix[i//4][i%4] for i in range(16)]