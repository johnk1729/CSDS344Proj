'''
- Hexadecimal to binary
- Binary to Hexadecimal
- Create subkeys
- Create sboxes
- X-or function
'''

import math


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
            subKeys.append(hex(abs(int(math.pi*(self.__numericKey ** 1/(x+1)))))[2:10])
        return subKeys

    def __init__(self, key):
        self.__numericKey = self.stringToAsciiInt(key)
        self.__subKeys = self.createSubKeys()

# For testing purposes:
def main():
    test = Blowfish('password2')
    print(test.createSubKeys())

if __name__ == '__main__':
    main()
