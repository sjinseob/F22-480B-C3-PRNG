def getMap():
    m = {}
    inv ={}
    c = 'A'
    bin_val = 0
    for i in range(1,27):
        bin_val = ord(c)-ord('A')
        s = "{0:b}".format(bin_val)
        if len(s)<5:
            padding_len = 5 - len(s)
            s = '0'*padding_len + s
        m[c] = s
        inv[s] = c
        c = chr(ord(c) + 1)
    for j in range(6):
        c = str(j)
        bin_val = bin_val + 1
        s = "{0:b}".format(bin_val)
        if len(s)<5:
            padding_len = 5 - len(s)
            s = '0'*padding_len + s
        m[c] = s
        inv[s] = c
    return (m,inv)

def main():
    (m, inv) = getMap()
    print(m)
    print(inv)
if __name__=='__main__':
    main()