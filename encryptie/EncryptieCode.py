import Subclasses_Encryptie

def Encryption(matrix,key):
    ### Eerste fase
    i = 0
    Subclasses_Encryptie.AddRoundKey(matrix,key,i)

    ### Tweede fase
    for phase in range(9):
        i += 1
        Subclasses_Encryptie.SubBytes(matrix)
        Subclasses_Encryptie.ShiftRows(matrix)
        Subclasses_Encryptie.MixColumns(matrix)
        Subclasses_Encryptie.AddRoundKey(matrix,key,i)

    ### Derde fase
    i += 1
    Subclasses_Encryptie.SubBytes(matrix)
    Subclasses_Encryptie.ShiftRows(matrix)
    Subclasses_Encryptie.AddRoundKey(matrix,key,i)
    return matrix


### GEGEVENS ###


def Vercijfering(number,Message):
    ### OP VOORHAND BEPAALDE GEGEVENS ###

    ### Opstellen van de counter
    counter = Subclasses_Encryptie.MakeCTR(number)
    ### Opstellen van de state
    state = Subclasses_Encryptie.CreateState(counter)
    zero_state = Subclasses_Encryptie.MakeZeroState()
    ### Persoonlijke (geheime) sleutels
    # De sleutel voor de vercijfering van de code
    Key = Subclasses_Encryptie.Key
    # De code voor het maken van de tag
    MAC = Subclasses_Encryptie.MAC


    ### ENCRYPTIE ###

    ### Opstelling van de encryptie
    EncryptionState = Encryption(state,Key)
    EncryptionState = Subclasses_Encryptie.ReadBlok(EncryptionState)
    ### Implementatie van de boodschap
    Subclasses_Encryptie.ImplementMessage(Message,EncryptionState)
    ### Aanmaken van de tag
    Tag = Encryption(zero_state,MAC)
    Tag = Subclasses_Encryptie.ReadBlok(Tag)
    Subclasses_Encryptie.ImplementMessage(Tag,Message)
    ### Het geïncrypteerde resultaat, gelinked met de counter
    return (Message,number,Tag)



number = 12
Lijst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
final_result = Vercijfering(number,Lijst)
