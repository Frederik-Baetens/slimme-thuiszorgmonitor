import pyb

def MakeCTRstd(number):
    """
      Een nummer (de counter) wordt omgezet in een vier op vier matrix.

    :param number: Een getal tussen de 0 en de 2**128-1
    :return matrix: 4x4-matrix
    """
	start = pyb.micros()
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

    return matrix, pyb.elapsed_micros(start)


def MakeCTRimproved(number):
    """
      Een nummer (de counter) wordt omgezet in een vier op vier matrix.

    :param number: Een getal tussen de 0 en de 2**128-1
    :return matrix: 4x4-matrix
    """
	start = pyb.micros()
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

    lijst.extend([0]*(16-teller))

    for position in range(4):
        matrix.append(lijst[position*4:position*4+4])

    return matrix, pyb.elapsed_micros(start)

