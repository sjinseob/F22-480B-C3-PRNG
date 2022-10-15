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
keyDoc = open("test_keys.txt", 'r') # generates the 32-bit number?
iv = b"09080706050403020100A2B2C2D2E2F2"  # generates the 16-bit number?

# plain = b"255044462d312e350a25d0d4c5d80a34"
# cipher = b"d06bf9d0dab8e8ef880660d2af65aa82"

plain = b"0123456789ABCDEF"

for key in keyDoc.readlines():
    k = bytes(key.strip(), "ascii")
    aesCipher = Cipher(algorithms.AES(k),
                   modes.CBC(iv),
                   backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    aesDecryptor = aesCipher.decryptor()
    #plaintext = aesDecryptor.update(cipher)
    #print(plaintext)
    cipher = aesEncryptor.update(plain)
    recover = aesDecryptor.update(cipher)
    if recover == plain:
        print("[PASS]")
        print(key)

'''cipher = aesEncryptor.update(plain)
recover = aesDecryptor.update(cipher)
if plain == recover:
    print("[PASS]")
else:
    print("plain",plain)
    print("cipher",cipher.hex())
    print("recover",recover)
    print("[FAIL]")'''