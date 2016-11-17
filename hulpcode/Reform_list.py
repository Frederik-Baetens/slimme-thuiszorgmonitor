def reform_list2(tup):
    output = str()

    boodschap = [str(i) for l in tup[0] for i in l]
    counter = str(tup[1])
    tag = lst =[str(i) for l in tup[2] for i in l]

    output += '.'.join(boodschap) + '.' + counter + '.' + '.'.join(tag) + '.'

    return output


    

