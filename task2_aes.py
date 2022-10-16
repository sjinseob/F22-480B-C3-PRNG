from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from binascii import unhexlify, hexlify   # Jin on 15 Oct: The binascii has a "unhexlify" function that can translate hex to binary.
# from Crypto.Cipher import AES

def main():

    # keys generted by task2_kg.c
    keyDoc = open("keys.txt", 'r')


    # Jin on 15 Oct: „unhexlify" transforms our given hex values to binary
    # plaintext, ciphertext and iv from assignment pdf
    plaintext = "255044462d312e350a25d0d4c5d80a34" 
    ciphertext = "d06bf9d0dab8e8ef880660d2af65aa82"
    iv = "09080706050403020100A2B2C2D2E2F2"
    #convert the above into binary from hex format
    plain_b = unhexlify(plaintext)
    cipher_b = unhexlify(ciphertext)
    iv_b = unhexlify(iv)

    # print all the different ciphertexts obtained using the keys from keys.txt
    f = open("task2_results.txt", "w")

    # for each key in keys.txt, create an encryptor and get the ciphertext for the given plaintext
    for key in keyDoc.readlines():
        k = unhexlify(key.strip())

        aesCipher = Cipher(algorithms.AES(k),
                    modes.CBC(iv_b),
                    backend=default_backend())
        aesEncryptor = aesCipher.encryptor()
        aesDecryptor = aesCipher.decryptor()
        cipher = aesEncryptor.update(plain_b)
        # if the given ciphertext matches the given ciphertext, the right key is found
        if cipher_b == cipher:
            print("[PASS]")
            print(key)


        f.write(str(hexlify(cipher)) + '\n')
    f.close()

if __name__=='__main__':
    main()