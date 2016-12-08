import Subclasses_Encryptie


def Encryption(matrix,key):
    """
      Opeenvolgende bewerkingen toegepast op een 4x4-matrix.
      De functies van deze bewerkingen zijn terug te vinden in de functieklas 'Subclasses_Encryptie'.
    :param matrix: 4x4-matrix
    :param key: 4x44-matrix
    :return: 4x4-matrix
    """

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


def Ontcijfering(final_result):
    """
      De ontvercijfering van een gegeven lijst.
      De ontvercijfering maakt gebruik van AES-128 (zie functie 'Encryption').

    :param final_result: Een tuppel met (geincrypteerde matrix, counter (getal), tag)
    :return: Een lijst, van vorm precies dezelfde als in de functieklasse 'Encryptie' ingegeven werd
    """

    ### Opstellen van een nul-matrix
    zero_state = Subclasses_Encryptie.ZeroState

    ### Persoonlijke (geheime) sleutels
    # De sleutel voor de vercijfering van de code
    Key = Subclasses_Encryptie.Key
    # De code voor het maken van de tag
    MAC = Subclasses_Encryptie.MAC

    ### Aanmaken van de state
    number = final_result[1]
    state = Subclasses_Encryptie.MakeCTR(number)
    EncryptionState = Encryption(state,Key)


    ### DECRYPTIE ###

    ### Lees de tag
    EncryptedMessage = final_result[0]
    Tag2 = Encryption(zero_state,MAC)
    Subclasses_Encryptie.ImplementMessage(Tag2,EncryptedMessage)
    Encryption(Tag2,MAC)

    ### Lees de Message
    Subclasses_Encryptie.ImplementMessage(EncryptedMessage,EncryptionState)
    if final_result[2] == Tag2:
        return Subclasses_Encryptie.BlokToList(EncryptedMessage)