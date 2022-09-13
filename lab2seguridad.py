



def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


def encriptar(message):

    rot_12 = rot_alpha(12)(message)
    password = "JOAN"
    vigenere = encrypt(rot_12,password)

    rot_2 = rot_alpha(2)(vigenere)

    # print(f"El mensaje cifrado -->",rot_2)


    archivo_enviar = open ('mensajeseguro.txt','w')
    archivo_enviar.write(rot_2)
    archivo_enviar.close()

    return rot_2



def desencriptar(mensaje_encriptado):
    password = "JOAN"
    rot_12menos = rot_12 = rot_alpha(-12)(mensaje_encriptado)
    vigenere_des = decrypt(rot_12menos,password)
    rot_2menos = rot_alpha(-2)(vigenere_des)

    return rot_2menos


def main():
    archivo = open ('mensajeentrada.txt','r')
    mensaje = archivo.read()
    archivo.close()


    mensaje_txt = encriptar(mensaje)



    archivo3 = open ('mensajeseguro.txt','r')
    mensaje_descifrar = archivo3.read()
    archivo3.close()

    mensaje_txt_des = desencriptar(mensaje_descifrar)
    print(mensaje_txt_des)


    if hash(mensaje_txt_des) == hash(mensaje):
        print("El mensaje sigue sin dañarse")
   
    
    # if hash(mensaje) == hash(rot_2menos):
    #     print("EL MENSAJE SIGUE SEGURO")
    

    


if __name__ == "__main__":
    main()



#Primero ROT12, LUEGO VIGENERE CON PASSWORD JOAN Y LUEGO ROT 3. 
#SE DEBE DE OBTENER EL HASH DEL DOCUMENTO.



