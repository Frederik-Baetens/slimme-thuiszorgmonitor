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


def Vercijfering(number,list):
    """
      De vercijfering van een gegeven lijst.
      De vercijfering maakt gebruik van AES-128 (zie functie 'Encryption').

    :param number: De counter
    :param list: Gegeven lijst, dat geincrypteerd zal worden
    :return: (4x4-matrix,number,tag)
    """

    ### Herschrijving van de gegeven lijst tot een 4x4-matrix
    Message = Subclasses_Encryptie.ListToBlok(list)

    ### Opstellen van de counter
    state = Subclasses_Encryptie.MakeCTR(number)

    ### Opstellen van de state
    zero_state = Subclasses_Encryptie.ZeroState

    ### Persoonlijke (geheime) sleutels
    # De sleutel voor de vercijfering van de code
    Key = Subclasses_Encryptie.Key
    # De code voor het maken van de tag
    MAC = Subclasses_Encryptie.MAC


    ### ENCRYPTIE ###

    ### Opstelling van de encryptie
    EncryptionState = Encryption(state,Key)

    ### Implementatie van de boodschap
    Subclasses_Encryptie.ImplementMessage(Message,EncryptionState)

    ### Aanmaken van de tag
    Tag = Encryption(zero_state,MAC)
    Subclasses_Encryptie.ImplementMessage(Tag, Message)
    Encryption(Tag,MAC)

    ### Het geincrypteerde resultaat, inclusief counter en tag
    return (Message,number,Tag)