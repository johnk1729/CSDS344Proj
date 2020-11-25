
def vigenereEncrypt(text, key):
    cipherText = []
    for i in range(len(text)):
        x = (ord(text[i]) + (ord(key[i% len(key)]))) % 26
        x += ord('A')
        cipherText.append(chr(x))
    return("".join(cipherText))

def vigenereDecrypt(cipherText, key):
    orgText = []
    for i in range(len(cipherText)):
        x = (ord(cipherText[i]) - (ord(key[i % len(key)])) + 26) % 26
        x += ord('A')
        orgText.append(chr(x))
    return("".join(orgText))



# For testing purposes:
def main():
    text = "BANKBANK"
    key = "WINE"
    print(vigenereEncrypt(text, key))
    text = "XIAOXIAO"
    key = "WINE"
    print(vigenereDecrypt(text, key))

if __name__ == '__main__':
    main()