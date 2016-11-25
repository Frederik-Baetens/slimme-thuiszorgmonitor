def dereform(string):
    """
    Maakt van de ontvangen vlakke string ('aaa.bbb.ccc. ... .zzz') opnieuw tupple van een lijst, een nummer en een lijst.
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

    list.append(int(string[index_last_point+1:-1]))
    return list[:16], list[16], list[17:]

a = '1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.77.28.29.30.31.32.33:'

print dereform(a)
