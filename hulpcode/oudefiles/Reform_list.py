def reform_list2(tup):
    output = str()

    boodschap = [str(i) for l in tup[0] for i in l]
    counter = str(tup[1])
    tag = lst =[str(i) for l in tup[2] for i in l]

    output += '.'.join(boodschap) + '.' + counter + '.' + '.'.join(tag) + ':'

    return output


    
def reform_list(tup):
    boodschap =  [str(i) for i in tup[0]]
    counter =str(tup[1])
    tag = [str(i) for i in tup[2]]

    return '.'.join(boodschap)  + '.' + counter + '.' + '.'.join(tag) + ':'
