from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from binascii import unhexlify, hexlify   # Jin on 15 Oct: The binascii has a "unhexlify" function that can translate hex to binary.
# from Crypto.Cipher import AES

# key = os.urandom(32) # generates the 32-bit number?
# print(len(key))
# key2 = bytes("8dfa318cb2fbcaf11635475163586d90", "ascii")
# print(type(key2))
# print(len(key2))
# iv = os.urandom(16)  # generates the 16-bit number?

'''
# Jin on 15 Oct: I suspect we won't need this if „unhexlify" can perform the dirty work of transforming hex to binary. :)
def to_bin_of_str(utf8bin):
    s = ""
    for ch in utf8bin:
        s += chr(int(ch,2))
    return s
'''
keyDoc = open("keys.txt", 'r') # generates the 32-bit number?

# iv = b"09080706050403020100A2B2C2D2E2F2"  # generates the 16-bit number?
# plain = b"255044462d312e350a25d0d4c5d80a34"
# cipher = b"d06bf9d0dab8e8ef880660d2af65aa82"

# Jin on 15 Oct: „unhexlify" transforms our given hex values to binary
plaintext = "255044462d312e350a25d0d4c5d80a34" 
ciphertext = "d06bf9d0dab8e8ef880660d2af65aa82"
iv = "09080706050403020100A2B2C2D2E2F2"
plain_b = unhexlify(plaintext)
cipher_b = unhexlify(ciphertext)
iv_b = unhexlify(iv)

f = open("task2_results.txt", "w")

for key in keyDoc.readlines():
    k = unhexlify(key.strip())

    aesCipher = Cipher(algorithms.AES(k),
                   modes.CBC(iv_b),
                   backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    aesDecryptor = aesCipher.decryptor()
    cipher = aesEncryptor.update(plain_b)
    f.write(str(hexlify(cipher)) + '\n')
    
    '''
    recover = aesDecryptor.update(cipher)
    if plain == recover:
        print("[PASS]")
    else:
        print("plain",plain)
        print("cipher",cipher.hex())
        print("recover",recover)
        print("[FAIL]")
    '''