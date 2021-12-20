from modules import Cesar

def main():

    # Lee el mensaje a cifrar
    msg = input("\033[0;33m" + "Ingrese mensaje a cifrar: ")

    # Encripta el mensaje como cadena de caracteres (por su posicion en el alfabeto)
    encripted: str = Cesar.encrypt(msg)
    # Desencripta el mensaje como cadena de caracteres (por su posicion en el alfabeto)
    decripted: str = Cesar.decrypt(encripted)
    # Imprime en pantalla el mensaje encriptado y desencriptado
    print("\033[1;36m" + "\nEncriptado por string" + "\033[0;37m")
    print("\033[0;31m" + encripted)
    print("\033[0;32m" + decripted)

    # Encripta el mensaje como bytes (por su posicion en la tabla ascii)
    bencripted: str = Cesar.bencrypt(bytes(msg, "utf-8"))
    # Desncripta el mensaje como bytes (por su posicion en la tabla ascii)
    bdecripted: str = Cesar.bdecrypt(bencripted)

    # Imprime en pantalla el mensaje encriptado y desencriptado
    print("\033[1;36m" + "\nEncriptado por bytes")
    print("\033[0;31m", end="")
    print(bencripted)
    print("\033[0;32m", end="")
    print(bdecripted)
    print("\033[0;37m", end="")
    return 0

if __name__ == "__main__":
    main()