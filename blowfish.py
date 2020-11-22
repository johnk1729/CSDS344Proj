'''
- Hexadecimal to binary
- Binary to Hexadecimal
- Create subkeys
- Create sboxes
- X-or function
'''

import math
import random

class Blowfish:
    __numericKey = 0
    __subKeys = []
    __sBoxes = []

    def stringToAsciiInt(self, string):
        numericKey = ''
        for x in string:
            numericKey = int(str(ord(x)) + str(numericKey))
        return numericKey

    def hexToBinary(self, hexValue):
        return int(hexValue, 16)

    def binaryToHex(self, binaryValue):
        return hex(int(str(binaryValue), 2))[2:]

    def createSubKeys(self):
        subKeys = []
        for x in range(18):
            subKeyValue = ''
            for y in range(8):
                subKeyValue += hex(random.randint(0, 15))[2:]
            subKeys.append(subKeyValue)
        return subKeys
    
    def createSBoxes(self):
        sBoxes = []
        for x in range(4):
            sbox = []
            for y in range(32):
                sbox_row = []
                for z in range(8):
                    sbox_value = ''
                    for i in range(8):
                        sbox_value += hex(random.randint(0, 15))[2:]
                    sbox_row.append(sbox_value)
                sbox.append(sbox_row)
            sBoxes.append(sbox)
        return sBoxes
    
    def hexAdd()
        

    def __init__(self, key):
        self.__numericKey = self.stringToAsciiInt(key)
        random.seed(abs(int(math.pi*(self.__numericKey))))
        self.__subKeys = self.createSubKeys()
        self.__sBoxes = self.createSBoxes()

# For testing purposes:
def main():
    test = Blowfish('password')
    print(test.createSubKeys())

if __name__ == '__main__':
    main()
