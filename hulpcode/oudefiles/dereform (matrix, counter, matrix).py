def string_naar_lijst(string):
    lijst_waarden= []
    current_number = ''
    for i in range(len(string)):
        if string[i] != '.' and string[i] != ':':
            current_number += string[i]
        else:
            lijst_waarden.append(int(current_number))
            current_number = ''

    return lijst_waarden

def dereform(string):
    waarden = string_naar_lijst(string)
    matrix_1 = [ [waarden[i] for i in range(4)], [waarden[i] for i in range(4, 8)], [waarden[i] for i in range(8, 12)], [waarden[i] for i in range(12, 16)] ]
    counter = waarden[16]
    matrix_2 = [ [waarden[i] for i in range(17, 21)], [waarden[i] for i in range(21, 25)], [waarden[i] for i in range(25, 29)], [waarden[i] for i in range(29, 33)] ]

    return (matrix_1, counter, matrix_2)
