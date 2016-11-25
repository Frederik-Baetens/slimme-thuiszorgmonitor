"""
blok= [[0,255,144,165],[14,156,254,10],[0,255,144,165],[14,156,254,10]]
lijst=[hex(i)[2:] for l in blok for i in l]
lijst2=[i if len(i)==2 else '0'+i for i in lijst]
lijst3=[eval('0x'+i)for i in lijst2]

print (lijst)
print (lijst2)
print (lijst3)
"""

#zoals in main:
lijst1=[0,4095,1555,1489,2098,255,1023,1024]
lijst2=[0,255,16,15]

lijst2_1 = [hex(i)[2:] for i in lijst2]
lijst2_2 = [i if len(i)==2 else '0'+i for i in lijst2_1]
lijst2_3 = [i for string in lijst2_2 for i in string]
lijst2_4 = [eval('0x'+i) for i in lijst2_3]
'''
print (lijst2_1)
print (lijst2_2)
print (lijst2_3)
print (lijst2_4)
'''
lijst1_1 = [hex(i)[2:] for i in lijst1]
lijst1_2 = ['0'*(3-len(i))+i for i in lijst1_1]
lijst1_3 = [i for string in lijst1_2 for i in string]
lijst1_4 = [eval('0x'+i) for i in lijst1_3]
'''
print (lijst1_1)
print (lijst1_2)
print (lijst1_3)
print (lijst1_4)
'''

totlijst=lijst1_4+lijst2_4
print (len(totlijst))
print (totlijst)


#duurt te lang, mss niet aanvullen met nullen
