import math
# obtained using the getMapping.py
mapping = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111', 'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 'Z': '11001', '0': '11010', '1': '11011', '2': '11100', '3': '11101', '4': '11110', '5': '11111'}
inv = {'00000': 'A', '00001': 'B', '00010': 'C', '00011': 'D', '00100': 'E', '00101': 'F', '00110': 'G', '00111': 'H', '01000': 'I', '01001': 'J', '01010': 'K', '01011': 'L', '01100': 'M', '01101': 'N', '01110': 'O', '01111': 'P', '10000': 'Q', '10001': 'R', '10010': 'S', '10011': 'T', '10100': 'U', '10101': 'V', '10110': 'W', '10111': 'X', '11000': 'Y', '11001': 'Z', '11010': '0', '11011': '1', '11100': '2', '11101': '3', '11110': '4', '11111': '5'}
encrypted = "J5A0EDJ2B"

def getKey(l):
    init_vector = [1,1,1,1,1,1]
    cur_vector = init_vector
    table = []
    key = ""
    temp = [0, 0, 0, 0, 0, 0]
    for _ in range(l):
        table.append(cur_vector)
        # print("current vector: ",  cur_vector)
        for i in range(len(cur_vector)-1):
            temp[i+1] = cur_vector[i]
            if i == 0:
                temp[0] = int(math.fmod(cur_vector[-2] + cur_vector[-1], 2))
            elif (i == len(cur_vector)-2):
                key += str(cur_vector[-1])
                break
        #print(temp)
        cur_vector = temp.copy()
    return key

def main():
    enc_bits = ""
    for c in encrypted:
        enc_bits += mapping[c]
    key = getKey(len(enc_bits))
    print('Key: ' + key)

    plaintext_bits = ""
    for i in range(len(enc_bits)):
        n = int(enc_bits[i]) + int(key[i])
        plaintext_bits += str(int(math.fmod(n, 2)))

    print("Decrypted binary: " + plaintext_bits)
    plain_text = ""
    for k in range(0,len(plaintext_bits),5):
        plain_text += inv[plaintext_bits[k:k+5]]

    print("Decrypted text: " + plain_text)

if __name__=='__main__':
    main()