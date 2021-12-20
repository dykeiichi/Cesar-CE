# Listas para el encriptado por cadena de caracteres
__alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
__upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
__numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Agrega los 3 saltos al mensaje
def __add_3(value: int, limit: int):
    add3 : int = value + 3
    if add3 >= limit:
        add3 -= limit
    return add3

# Resta los 3 saltos al mensaje
def __substract_3(value: int, limit: int):
    sub3: int = value - 3
    if sub3 < 0:
        sub3 += limit
    return sub3

# Realiza el encriptado para cada letra y lo une en una sola cadena de caracteres
def encrypt(msg: str):
    enc: str = ""
    for ch in msg:
        if ch in __alphabet:
            enc = enc + __alphabet[__add_3(__alphabet.index(ch), len(__alphabet))]
        elif ch in __upperAlphabet:
            enc = enc + __upperAlphabet[__add_3(__upperAlphabet.index(ch), len(__upperAlphabet))]
        elif ch in __numbers:
            enc = enc + __numbers[__add_3(__numbers.index(ch), len(__numbers))]
        else:
            enc = enc + ch
    return enc

# Realiza el desencriptado para cada letra y lo une en una sola cadena de caracteres
def decrypt(enc: str):
    msg: str = ""
    for ch in enc:
        if ch in __alphabet:
            msg = msg + __alphabet[__substract_3(__alphabet.index(ch), len(__alphabet))]
        elif ch in __upperAlphabet:
            msg = msg + __upperAlphabet[__substract_3(__upperAlphabet.index(ch), len(__upperAlphabet))]
        elif ch in __numbers:
            msg = msg + __numbers[__substract_3(__numbers.index(ch), len(__numbers))]
        else:
            msg = msg + ch
    return msg
    
# Realiza el encriptado para cada letra y lo une en un solo arreglo de bytes
def bencrypt(msg: bytes):
    enc: bytes = b""
    for ch in msg:
        enc = b"".join([enc, int(__add_3(ch, 256)).to_bytes(1, "big")])
    return enc

# Realiza el desencriptado para cada letra y lo une en un solo arreglo de bytes
def bdecrypt(enc: bytes):
    msg: bytes = b""
    for ch in enc:
        msg = b"".join([msg, int(__substract_3(ch, 256)).to_bytes(1, "big")])
    return msg