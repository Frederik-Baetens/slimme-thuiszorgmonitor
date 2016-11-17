import Subclasses_Encryptie
import EncryptieCode
import ReadSensor

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



final_result = EncryptieCode.final_result

def Ontcijfering(final_result):
    # Lees de EncryptieCode
    zero_state = Subclasses_Encryptie.MakeZeroState()

    # Sleutels
    Key = Subclasses_Encryptie.Key
    MAC = Subclasses_Encryptie.MAC

    # Aanmaken van de state
    number = final_result[1]
    counter = Subclasses_Encryptie.MakeCTR(number)
    state = Subclasses_Encryptie.CreateState(counter)
    EncryptionState = Encryption(state,Key)


    ### DECRYPTIE ###

    ### Lees de tag
    EncryptedMessage = final_result[0]
    EncryptedTag = final_result[2]
    Tag2 = Encryption(zero_state,MAC)
    Subclasses_Encryptie.ImplementMessage(Tag2,EncryptedMessage)
    ### Lees de Message
    Subclasses_Encryptie.ImplementMessage(EncryptedMessage,EncryptionState)
    assert final_result[2] == Tag2

    return ReadSensor.ReadBlok(EncryptedMessage)

Message = Ontcijfering(final_result)
print(Message)
assert Message == [1,2,3,4,5,6,7,8]