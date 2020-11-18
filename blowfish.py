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

    def keyToAsciiCode(self, stringKey):
        numericKey = ''
        for x in stringKey:
            numericKey = int(str(ord(x)) + str(numericKey))
        return numericKey

    def hexToBinary(self, hexValue):
        return int(hexValue, 16)

    def binaryToHex(self, binaryValue):
        return hex(int(str(binaryValue), 2))[2:]

    def createSubKeys(self):
        subKeys = []
        for x in range(18):
            print(self.__numericKey)
            subKeys.append(hex(abs(int(math.pi*(self.__numericKey ** 1/(x+1)))))[2:10])

    def __init__(self, key):
        self.__numericKey = self.keyToAsciiCode(key)

# For testing purposes:
def main():
    test = Blowfish('password1')
    print(test.createSubKeys())

if __name__ == '__main__':
    main()
