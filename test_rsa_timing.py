import file_to_hex_letters
import vigenere, RSA2, blowfish
import datetime
import numpy as np
import matplotlib.pyplot as plt
VIGENERE_KEY = "QWERTYUIOP"
BLOWFISH_KEY = "QWERTYUIOP"
file_size = 1
RSA_Es = [379, 2011,9391, 13609, 24697, 34697]
RSA_Ds = [307, 403, 1879, 4537, 8233, 20779]
RSA_Ns = [485, 2147, 9617, 13861, 25021, 35011]

# Encrypt test files with RSA and time how long it takes:
rsa_times = []
rsa_times_stdev = []
file_encrypted_hex_letters_rsa_saved = {}
for ind in range(6):
    file_path = f"{file_size}KB.bin"
    trial_times = []
    RSA_E = RSA_Es[ind]
    RSA_N = RSA_Ns[ind]
    RSA_D = RSA_Ds[ind]

    for trial in range(1):
        start = datetime.datetime.now()
        file_encrypted_hex_letters_rsa_saved[file_size] = RSA2.encrypt(RSA_N, RSA_E, file_to_hex_letters.convert_to_hex_letters(file_path))
        trial_times.append((datetime.datetime.now() - start).total_seconds())
        print(f"{ind},{trial}")
    rsa_times.append(np.mean(trial_times))
    rsa_times_stdev.append(np.std(trial_times))

objects = ('A', 'B', 'C', 'D', 'E', 'F')
y_pos = np.arange(len(objects))
plt.bar(y_pos, rsa_times)
plt.xticks(y_pos, objects)
plt.title("RSA Encryption Time by Key Condition")
plt.xlabel("Condition")
plt.ylabel("Time to encrypt (s)")
plt.show()





# Decrypt test files with RSA and time how long it takes:
rsa_decrypt_times = []
rsa_decrypt_times_stdev = []
for ind in range(6):
    file_path = f"{file_size}KB.bin"
    trial_times = []
    RSA_E = RSA_Es[ind]
    RSA_N = RSA_Ns[ind]
    RSA_D = RSA_Ds[ind]
    for trial in range(1):
        start = datetime.datetime.now()
        RSA2.decrypt(RSA_N, RSA_D, file_encrypted_hex_letters_rsa_saved[file_size])
        trial_times.append((datetime.datetime.now() - start).total_seconds())
    rsa_decrypt_times.append(np.mean(trial_times))
    rsa_decrypt_times_stdev.append(np.std(trial_times))


plt.bar(y_pos, rsa_decrypt_times)
plt.xticks(y_pos, objects)
plt.title("RSA Decryption Time by Key Condition")
plt.xlabel("Condition")
plt.ylabel("Time to decrypt (s)")
plt.show()



