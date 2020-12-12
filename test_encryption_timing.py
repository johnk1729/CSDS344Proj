# Evaluation Data: https://drive.google.com/file/d/18ceSVHWwO26W4zhMWMXsZ4FdGHjS5ujx/view?usp=sharing

import file_to_hex_letters
import vigenere, RSA2, blowfish
import datetime
import numpy as np
import matplotlib.pyplot as plt
# Run each algorithm many times and time how long it takes to encrypt and decrypt
VIGENERE_KEY = "QWERTYUIOP"
BLOWFISH_KEY = "QWERTYUIOP"

RSA_E = 10651
RSA_D = 2131
RSA_N = 10877
vigenere_test_sizes = [10,20,30,40,50]
rsa_test_sizes = [1, 1.5, 2, 2.5, 3]
#rsa_test_sizes = [0.1,0.2,0.3]
blowfish_test_sizes =  [.5, 1, 1.5]
'''
# Encrypt test files with RSA and time how long it takes:
vigenere_times = []
vigenere_times_stdev = []
file_encrypted_hex_letters_vigenere_saved = {}
for file_size in vigenere_test_sizes:
    file_path = f"{file_size}KB.bin"
    trial_times = []
    for trial in range(10):
        start = datetime.datetime.now()
        file_encrypted_hex_letters_vigenere_saved[file_size] =  vigenere.vigenereEncrypt(file_to_hex_letters.convert_to_hex_letters(file_path), VIGENERE_KEY)
        trial_times.append((datetime.datetime.now() - start).total_seconds())
    vigenere_times.append(np.mean(trial_times))
    vigenere_times_stdev.append(np.std(trial_times))

plt.errorbar(vigenere_test_sizes, vigenere_times, yerr=vigenere_times_stdev, label="Vigenere")
plt.title("Vigenere Encryption Time by File Size")
plt.xlabel("File size (KB)")
plt.ylabel("Time to encrypt (s)")
plt.legend()
plt.show()


# Decrypt test files with Vigenere and time how long it takes:
vigenere_decrypt_times = []
vigenere_decrypt_times_stdev = []
for file_size in vigenere_test_sizes:
    trial_times = []
    for trial in range(10):
        start = datetime.datetime.now()
        vigenere.vigenereDecrypt(file_encrypted_hex_letters_vigenere_saved[file_size], VIGENERE_KEY)
        trial_times.append((datetime.datetime.now() - start).total_seconds())
    vigenere_decrypt_times.append(np.mean(trial_times))
    vigenere_decrypt_times_stdev.append(np.std(trial_times))


plt.errorbar(vigenere_test_sizes, vigenere_decrypt_times, yerr=vigenere_decrypt_times_stdev, label="Vigenere")
plt.title("Vigenere Decryption Time by Original File Size")
plt.xlabel("Size of unencrypted file (KB)")
plt.ylabel("Time to decrypt (s)")
plt.show()

'''

# Encrypt test files with RSA and time how long it takes:
rsa_times = []
rsa_times_stdev = []
file_encrypted_hex_letters_rsa_saved = {}
for file_size in rsa_test_sizes:
    file_path = f"{file_size}KB.bin"
    trial_times = []
    for trial in range(10):
        start = datetime.datetime.now()
        file_encrypted_hex_letters_rsa_saved[file_size] = RSA2.encrypt(RSA_N, RSA_E, file_to_hex_letters.convert_to_hex_letters(file_path))
        trial_times.append((datetime.datetime.now() - start).total_seconds())
        print(f"{file_size},{trial}")
    rsa_times.append(np.mean(trial_times))
    rsa_times_stdev.append(np.std(trial_times))


plt.errorbar(rsa_test_sizes, rsa_times, yerr=rsa_times_stdev, label="RSA")
plt.title("RSA Encryption Time by File Size")
plt.xlabel("File size (KB)")
plt.ylabel("Time to encrypt (s)")
plt.show()





# Decrypt test files with RSA and time how long it takes:
rsa_decrypt_times = []
rsa_decrypt_times_stdev = []
for file_size in rsa_test_sizes:
    trial_times = []
    for trial in range(10):
        start = datetime.datetime.now()
        RSA2.decrypt(RSA_N, RSA_D, file_encrypted_hex_letters_rsa_saved[file_size])
        trial_times.append((datetime.datetime.now() - start).total_seconds())
    rsa_decrypt_times.append(np.mean(trial_times))
    rsa_decrypt_times_stdev.append(np.std(trial_times))

plt.errorbar(rsa_test_sizes, rsa_decrypt_times, yerr=rsa_decrypt_times_stdev, label="RSA")
plt.title("RSA Decryption Time by Original File Size")
plt.xlabel("Size of unencrypted file (KB)")
plt.ylabel("Time to decrypt (s)")
plt.show()









# Encrypt test files with Blowfish and time how long it takes:
blowfish_times = []
blowfish_times_stdev = []
file_encrypted_hex_letters_blowfish_saved = {}
for file_size in blowfish_test_sizes:
    file_path = f"{file_size}KB.bin"
    trial_times = []
    for trial in range(10):
        start = datetime.datetime.now()
        blowfishEncryptor = blowfish.Blowfish(BLOWFISH_KEY)
        file_encrypted_hex_letters_blowfish_saved[file_size] = blowfishEncryptor.encryptMessage(file_to_hex_letters.convert_to_hex_letters(file_path))
        trial_times.append((datetime.datetime.now() - start).total_seconds())
    blowfish_times.append(np.mean(trial_times))
    blowfish_times_stdev.append(np.std(trial_times))


plt.errorbar(blowfish_test_sizes, blowfish_times, yerr=blowfish_times_stdev, label="Blowfish")
plt.title("Blowfish Encryption Time by File Size")
plt.xlabel("File size (KB)")
plt.ylabel("Time to encrypt (s)")
plt.show()





# Decrypt test files with Blowfish and time how long it takes:
blowfish_decrypt_times = []
blowfish_decrypt_times_stdev = []
for file_size in blowfish_test_sizes:
    trial_times = []
    for trial in range(10):
        start = datetime.datetime.now()

        decryptor = blowfish.Blowfish(BLOWFISH_KEY)
        decryptor.decryptMessage(file_encrypted_hex_letters_blowfish_saved[file_size])
        trial_times.append((datetime.datetime.now() - start).total_seconds())
    blowfish_decrypt_times.append(np.mean(trial_times))
    blowfish_decrypt_times_stdev.append(np.std(trial_times))

plt.errorbar(blowfish_test_sizes, blowfish_decrypt_times, yerr=blowfish_decrypt_times_stdev, label="BLOWFISH")
plt.title("Blowfish Decryption Time by Original File Size")
plt.xlabel("Size of unencrypted file (KB)")
plt.ylabel("Time to decrypt (s)")
plt.show()


#print(f"Vigenere Encryption Took: {vigenere_times}")
#print(f"RSA Encryption Took: {rsa_times}")


