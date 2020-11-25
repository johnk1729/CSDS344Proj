import math

## gets gcd of two numbers a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

## checks if n is prime
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n%2 == 0 or n%3 == 0):
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

## converts string to ASCII encoding
def plaintextToASCII(message):
    encoding = [ord(c) for c in message]
    return encoding

## convert ASCII encoding to string
def ASCIItoPlainText(encoding):
    plaintext = ''.join(map(chr,encoding))
    return plaintext

## input p and q should be prime numbers
def generateKeys(p, q):

    ## check if p and q are prime
    if not isPrime(p):
        raise ValueError("Input must be prime and " + str(p) + " is not prime.")
    if not isPrime(q):
        raise ValueError("Input must be prime and " + str(q) + " is not prime.")

    ## define modulus, phi, public exponent (E), and private exponent (D)
    N = p*q
    phi = (p-1)*(q-1)
    E = phi - 2
    D = phi - 1

    ## E must only have 1 common factor with phi
    while (gcd(E,phi) > 1):
        E -= 1

    ## ED mod phi must be 1
    while ((E*D)%phi != 1):
        D -= 1

    keys = {'modulus': N,
            'public exponent': E,
            'private exponent': D}

    return keys
    
## encrypt a message using a publc key (N,E)
## message must be smaller than N
def encrypt(p, q, plaintext):

    ## get ASCII encoding of plain text
    encoding = plaintextToASCII(plaintext)

    ## check to make sure p and q are sufficiently large
    if (max(encoding) > p*q):
        raise ValueError("p and q are too small, please choose larger p and q values")

    ## generate keys
    keys = generateKeys(p,q)
    E = keys['public exponent']
    N = keys['modulus']

    ## generate ciphertext
    ciphertext = []
    for i in range(len(encoding)):
        ciphertext.append((encoding[i]**E) % N)

    return ciphertext

# decrypt a message using a private key (N,D)
def decrypt(p, q, ciphertext):

    ## generate keys
    keys = generateKeys(p,q)
    D = keys['private exponent']
    N = keys['modulus']

    ## decrypt ciphertext to ASCII encoding
    message = []
    for i in range(len(ciphertext)):
        message.append((ciphertext[i]**D) % N)

    return ASCIItoPlainText(message)




## example of functionality
## todo: set an example P,Q, and message
EXAMPLE_P = 5
EXAMPLE_Q = 97
EXAMPLE_MESSAGE = "Hello World"

EXAMPLE_CIPHERTEXT = encrypt(EXAMPLE_P, EXAMPLE_Q, EXAMPLE_MESSAGE)
EXAMPLE_DECRYPTED_MESSAGE = decrypt(EXAMPLE_P, EXAMPLE_Q, EXAMPLE_CIPHERTEXT)
print("message is: " + EXAMPLE_MESSAGE)
print("ASCII encoding of " + EXAMPLE_MESSAGE + " is: " + str(plaintextToASCII(EXAMPLE_MESSAGE)))
print("ciphertext is: " + str(EXAMPLE_CIPHERTEXT))
print("decrypted message is " + EXAMPLE_DECRYPTED_MESSAGE)