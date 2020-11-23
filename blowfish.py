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
    
    
    #Takes in a decimal value as int and returns a binary value as string
    def decimalToBinary(self, decimalValue):
        return bin(decimalValue)[2:]
    
    
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
    def hexAddLimit2ToThe32(self, hexNum1, hexNum2):
        return self.decimalToHex((self.hexToDecimal(hexNum1)+self.hexToDecimal(hexNum2))%(2**32))
    
    #TODO: Remove this 
    def getSubKeys(self):
        return self.__subKeys
    
    
    def addLeadingBinaryZeros(self, binaryValue, length):
        value = binaryValue
        while len(value) < length:
            value = '0' + value
        return value

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
        
        binaryMessageChunk = self.addLeadingBinaryZeros(binaryMessageChunk, 8)
        
        if len(binaryMessageChunk) != 8:
            print('Error: Blowfish::subBoxObfuscation given messageChunk wrong size')
            return
            
        
        
        xAxis = self.binaryToDecimal(binaryMessageChunk[2:7])
        yAxis = self.binaryToDecimal(binaryMessageChunk[0:2]+binaryMessageChunk[7:])
        return self.subBoxLookup(boxNum, xAxis, yAxis)
    
    
    #Performs f Function on a hexadecimal message block as string
    def fFunction(self, messageBlock):
        cipherText = ''
        index = 0
        substitutions = []
        binaryMessageBlock = self.addLeadingBinaryZeros(self.hexToBinary(messageBlock), 32)
        
        if len(binaryMessageBlock) != 32:
            print('Error: Blowfish::fFunction given messageBlock wrong size')
            return
        
        while index < 32:
            start = index
            index += 8
            substitutions.append(self.subBoxObfuscation(int(start/8), binaryMessageBlock[start:index]))
        
        return self.hexAddLimit2ToThe32(substitutions[3], self.decimalToHex(self.hexToDecimal(self.hexAddLimit2ToThe32(substitutions[0], substitutions[1])) ^ self.hexToDecimal(substitutions[2])))
    
    
    #Performs a round of encryption on a hexadecimal 64 bit message as string given corresponding hexadecimal 32 bit subkey as string and returns hexadecimal 64 bit ciphertext as string
    def encryptionRound(self, messageBlock, subKey):
        binaryMessageBlock = self.addLeadingBinaryZeros(self.hexToBinary(messageBlock), 64)
        halfBlockSize = int(len(binaryMessageBlock)/2)
        
        if len(binaryMessageBlock) != 64:
            print('Error: Blowfish::fFunction given messageBlock wrong size')
            return
        
        fFunction = self.fFunction(self.decimalToHex(self.hexToDecimal(subKey) ^ self.binaryToDecimal(binaryMessageBlock[0:halfBlockSize])))
        return (self.decimalToHex(self.hexToDecimal(fFunction) ^ self.binaryToDecimal(binaryMessageBlock[halfBlockSize:])) + self.binaryToHex(binaryMessageBlock[0:halfBlockSize]))
    
    def encryptionPostProcessing(self, messageBlock):
        binaryMessageBlock = self.addLeadingBinaryZeros(self.hexToBinary(messageBlock), 64)
        halfBlockSize = int(len(binaryMessageBlock)/2)
        
        return (self.decimalToHex(self.binaryToDecimal(binaryMessageBlock[halfBlockSize:]) ^ self.hexToDecimal(self.__subKeys[0])) + self.decimalToHex(self.binaryToDecimal(binaryMessageBlock[0:halfBlockSize]) ^ self.hexToDecimal(self.__subKeys[1])))
    
    def encryptPiece(self, messageChunk):
        message = messageChunk
        for i in range(len(self.__subKeys)):
            message = self.encryptionRound(message, self.__subKeys[i])
        return self.encryptionPostProcessing(message)
        
        
    def encryptMessage(self, message):
        index = 0
        plainText = self.decimalToHex(self.stringToAsciiInt(message))
        cipherText = ''
        
        while len(plainText)%16 != 0:
            plainText = '0' + plainText
            
        while index < len(plainText):
            cipherText += self.encryptPiece(plainText[index:index+16])
            index += 16
            
        return cipherText
    
    #Constructor that takes a string key
    def __init__(self, key):
        self.__numericKey = self.stringToAsciiInt(key)
        random.seed(abs(int(math.pi*(self.__numericKey))))
        self.__subKeys = self.createSubKeys()
        self.__sBoxes = self.createSBoxes()

# For testing purposes:
def main():
    test = Blowfish('password')
    print(test.encryptMessage('Hello everybody! This message will be encrypted.'))

if __name__ == '__main__':
    main()
