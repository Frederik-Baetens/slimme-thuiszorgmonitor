import Subclasses_Encryptie
#[4095,320] [12,2465] [1987,0] [4095,4095]
# Meting van 2 sensors, 4x herhaald

def ListToBlok(lijst):
    matrix = Subclasses_Encryptie.MakeZeroState()
    posistion = 0
    for element in lijst:
        element = str(element)
        if int(element) < 100:
            first = 0
            second = int(element)
        elif int(element) < 1000:
            first = int(element[:1])
            second = int(element[1:])
        else:
            first = int(element[:2])
            second = int(element[2:])
        for place in [first,second]:
            matrix[posistion//4][posistion%4] = place
            posistion += 1
    return matrix

def ReadBlok(matrix):
    lijst = []
    for row in range(4):
        for column in range(2):
            a = matrix[row][column*2]*100
            b = matrix[row][column*2+1]
            lijst += [a+b]
    lijst = lijst[:8]
    return lijst