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

    #Takes in a string and returns a numeric value based on the ASCII codes of the string
    def stringToAsciiInt(self, string):
        numericKey = ''
        for x in string:
            numericKey = int(str(ord(x)) + str(numericKey))
        return numericKey
    
    def decimalToHex(self, decimalValue):
        return hex(int(decimalValue))[2:]

    #Takes in a hexadecimal value as string and returns a binary value as string
    def hexToBinary(self, hexValue):
        return bin(self.hexToDecimal(hexValue))[2:]
    
    #Takes in a hexadecimal value as string and returns a decimal value as int
    def hexToDecimal(self, hexValue):
        return int(hexValue, 16)
    
    #Takes in a binary value as a string or int and returns hexadecimal value as string
    def binaryToHex(self, binaryValue):
        return hex(int(str(binaryValue), 2))[2:]
    
    #Takes in a binary value as a string or int and returns a decimal value as int
    def binaryToDecimal(self, binaryValue):
        return int(str(binaryValue), 2)
    
    #Takes in two strings of hexadecimal values and returns a string of the sum
    def hexAdd(self, hexNum1, hexNum2):
        return self.decimalToHex(self.hexToDecimal(hexNum1)+self.hexToDecimal(hexNum2))

    #Creates and returns 18 subkeys of 32 bits in hexadecimal based on the numeric key
    def createSubKeys(self):
        subKeys = []
        for x in range(18):
            subKeyValue = ''
            for y in range(8):
                subKeyValue += hex(random.randint(0, 15))[2:]
            subKeys.append(subKeyValue)
        return subKeys
    
    #Creates and returns 4 substitution boxes of 32 rows of 8 columns of 32 bits in hexadecimal based on the numeric key
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
    
    #Looks up and returns value at given s box number, row index, and col index
    def subBoxLookup(self, boxNum, rowIndex, colIndex):
        return self.__sBoxes[boxNum][rowIndex][colIndex]
    
    #Obfuscates message chunk with s box given in s box number (1 to 4) and 32 bit message chunk in hex as string
    def subBoxObfuscation(self, boxNum, binaryMessageChunk):
        if len(binaryMessageChunk) > 8:
            print('Error: Blowfish::subBoxObfuscation given messageChunk too large')
            return
            
        #TODO: May need to deal with if the chunk converts to a binary less than 8 bits (we might need to add leading 0s)
        
        xAxis = self.binaryToDecimal(binaryMessageChunk[2:7])
        yAxis = self.binaryToDecimal(binaryMessageChunk[0:2]+binaryMessageChunk[7:])
        return self.subBoxLookup(boxNum, xAxis, yAxis)
    
    def fFunction(self, messageBlock):
        cipherText = ''
        index = 0
        substitutions = []
        binaryMessageBlock = self.hexToBinary(messageBlock)
        
        if len(binaryMessageBlock) > 32:
            print('Error: Blowfish::fFunction given messageBlock too large')
            
        #TODO: May need to deal with if the chunk converts to a binary less than 8 bits (we might need to add leading 0s)
        
        while index < 32:
            start = index
            index += 8
            substitutions.append(self.subBoxObfuscation(int(start/8), binaryMessageBlock[start:index]))
        
        
        return self.hexAdd(substitutions[3], self.decimalToHex(self.hexToDecimal(self.hexAdd(substitutions[0], substitutions[1])) ^ self.hexToDecimal(substitutions[2])))
            
    #Constructor that takes a string key
    def __init__(self, key):
        self.__numericKey = self.stringToAsciiInt(key)
        random.seed(abs(int(math.pi*(self.__numericKey))))
        self.__subKeys = self.createSubKeys()
        self.__sBoxes = self.createSBoxes()

# For testing purposes:
def main():
    test = Blowfish('password')
    print(test.fFunction('FFFFFFFF'))

if __name__ == '__main__':
    main()
