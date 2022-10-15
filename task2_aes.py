from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# key = os.urandom(32) # generates the 32-bit number?
# print(len(key))
# key2 = bytes("8dfa318cb2fbcaf11635475163586d90", "ascii")
# print(type(key2))
# print(len(key2))
#iv = os.urandom(16)  # generates the 16-bit number?

def to_bin_of_str(utf8bin):
    s = ""
    for ch in utf8bin:
        s += chr(int(ch,2))
    return s
keyDoc = open("keys.txt", 'r') # generates the 32-bit number?
iv = b"0908070605040302" #0100A2B2C2D2E2F2"  # generates the 16-bit number?

# plain = b"255044462d312e350a25d0d4c5d80a34"
# cipher = b"d06bf9d0dab8e8ef880660d2af65aa82"

plain = b"255044462d312e350a25d0d4c5d80a34"
cipher = b"d06bf9d0dab8e8ef880660d2af65aa82"
    
for key in keyDoc.readlines():
    k = bytes(key.strip(), "ascii")
    aesCipher = Cipher(algorithms.AES(k),
                   modes.CBC(iv),
                   backend=default_backend())
    #aesEncryptor = aesCipher.encryptor()
    aesDecryptor = aesCipher.decryptor()
    plaintext = aesDecryptor.update(cipher)
    #for l in plaintext:
       # plaintxt += chr(l)
    #print(plaintext)
    #recover = aesDecryptor.update(cipher)
    #print(plaintxt)
    if plaintext == plain:
        print("[PASS]")
        print(key)
        break

'''cipher = aesEncryptor.update(plain)
recover = aesDecryptor.update(cipher)
if plain == recover:
    print("[PASS]")
else:
    print("plain",plain)
    print("cipher",cipher.hex())
    print("recover",recover)
    print("[FAIL]")'''