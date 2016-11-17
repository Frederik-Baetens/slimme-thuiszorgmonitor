#initialiseer een lege 4x4 matrix: matrix_1
matrix_1 = []
for i in range(4):
    matrix_1 = matrix_1 + [[0]*4]

#initialiseer een lege 4x4 matrix: matrix_2
matrix_2 = []
for j in range(4):
    matrix_2 = matrix_2 + [[0]*4]


def dereform(string):
    """
    Maakt van de ontvangen vlakke string ('aaa.bbb.ccc. ... .zzz') opnieuw een 4x4 matrix, een nummer en een 4x4 matrix.
    """

    #herwerk de string tot een lijst van afzonderlijke waarden
    list = []
    check_new_point = 1
    index_last_point = -1
    while check_new_point < len(string):
        if string[check_new_point] == '.':
            list.append(int(string[index_last_point + 1:check_new_point]))
            index_last_point = check_new_point
        check_new_point += 1

    #zet de eerste 16 waarden in matrix_1
    current = 0
    for rij in range(4):
        for kolom in range(4):
            matrix_1[rij][kolom] = list[current]
            current += 1

    #de 17de waarde blijft bewaard als een nummer
    nummer = list[current]
    current += 1

    #zet de laatste 16 waarden in matrix_2
    for rij in range(4):
        for kolom in range(4):
            matrix_2[rij][kolom] = list[current]
            current += 1

    return matrix_1, nummer, matrix_2

a = '11.22.33.44.55.66.77.88.99.1010.1111.2222.3333.4444.5555.6666.7777.8888.9999.2020.111111.222222.333333.444444.555555.666666.777777.888888.999999.3030.3131.3232.6969.'