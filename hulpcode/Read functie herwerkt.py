def read(NB_READINGS):
    global read_counter

    lst_ecg[read_counter] = ecg_pin.read()
    if read_counter % 2 == 0:
        lst_po[read_counter//2] = po_pin.read()//16

    if read_counter == NB_READINGS - 1:
        read_counter = 0
    else:
        read_counter += 1
    return





#### 2e versie
#### hiervoor moeten lst_ecg en lst_op gewoon als lege lijsten, zonder lengte 

lst_ecg = []
lst_po  =  []

def read(NB_READINGS):
    global read_counter, lst_ecg, lst_po

    if read_counter == 0:
        lst_ecg = []
        lst_po  =[]
   
    lst_ecg.append(ecg_pin.read())
    if read_counter % 2 == 0:
        lst_po.append(po_pin.read()//16)

    if read_counter == NB_READINGS - 1:
        read_counter =  0

    
