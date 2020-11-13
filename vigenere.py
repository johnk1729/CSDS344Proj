
def vigenereEncipher(text, key):
    cipherText = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipherText.append(chr(x))
    return("".join(cipherText))

def vigenereDecipher(cipherText, key):
    orgText = []
    for i in range(len(cipherText)):
        x = (ord(cipherText[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orgText.append(chr(x))
    print("".join(orgText))
    return("".join(orgText))

#text = "BANK"
#key = "WINE"
#print(vigenereEncipher(text, key))