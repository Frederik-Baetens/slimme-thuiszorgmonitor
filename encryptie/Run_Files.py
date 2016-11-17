import Subclasses_Encryptie
import time
# START MY TIMER
start = time.time()


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

### Opstellen van de counter
number = 16584
counter = Subclasses_Encryptie.MakeCTR(number)

### Opstellen van de state
state = Subclasses_Encryptie.CreateState(counter)
zero_state = Subclasses_Encryptie.MakeZeroState()
zero_state2 = Subclasses_Encryptie.MakeZeroState()

### Persoonlijke (geheime) sleutels
# De sleutel voor de vercijfering van de code
Key = Subclasses_Encryptie.Key
# De code voor het maken van de tag
MAC = Subclasses_Encryptie.MAC

### De boodschap
Message = [[1,1,1,1],[22,22,22,22],[123,123,123,123],[0,0,0,0]]



### ENCRYPTIE ###

### Opstelling van de encryptie
EncryptionState = Encryption(state,Key)
### Implementatie van de boodschap
Subclasses_Encryptie.ImplementMessage(Message,EncryptionState)
### Aanmaken van de tag
Tag = Encryption(zero_state,MAC)
Subclasses_Encryptie.ImplementMessage(Tag,Message)
### Het geïncrypteerde resultaat, gelinked met de counter
final_result = (Message,number,Tag)


### VERZENDING VAN DE BOODSCHAP ###


### DECRYPTIE ###

### Lees de tag
EncryptedMessage = final_result[0]
EncryptedTag = final_result[2]
Tag2 = Encryption(zero_state2,MAC)
Subclasses_Encryptie.ImplementMessage(Tag2,EncryptedMessage)
### Lees de Message
Subclasses_Encryptie.ImplementMessage(EncryptedMessage,EncryptionState)
assert EncryptedMessage == [[1,1,1,1],[22,22,22,22],[123,123,123,123],[0,0,0,0]]
assert Tag == Tag2



# STOP MY TIMER
elapsed_time = time.time() - start # in seconds
print ('The script took ',elapsed_time,' seconds !')


# HAAL FOUT UIT DE COUNTERMODE VIA DE TAG!!!!