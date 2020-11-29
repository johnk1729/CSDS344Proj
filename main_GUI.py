import PySimpleGUI as sg
import vigenere
import blowfish
import os
import file_to_hex_letters
import binascii
import RSA

# TODO: Restrict inputs to only valid characters

# Define the elements that will go in each window tab:
vigenere_encrypt_tab = [
    [
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="vigenere_encrypt_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("To encrypt:")],
                [
                    sg.Multiline(
                        "(input text goes here)",
                        size=(45, 5),
                        key="vigenere_encrypt_input",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Encrypted:")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(45, 5),
                        key="vigenere_encrypt_output",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Encrypt", key="vigenere_encrypt_button"),
    ]
]
vigenere_decrypt_tab = [
    [
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="vigenere_decrypt_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("To decrypt:")],
                [
                    sg.Multiline(
                        "(input text goes here)",
                        size=(45, 5),
                        key="vigenere_decrypt_input",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Decrypted:")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(45, 5),
                        key="vigenere_decrypt_output",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Decrypt", key="vigenere_decrypt_button"),
    ]
]

blowfish_encrypt_tab = [
    [
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="blowfish_encrypt_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("To encrypt:")],
                [
                    sg.Multiline(
                        "(input text goes here)",
                        size=(45, 5),
                        key="blowfish_encrypt_input",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Encrypted:")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(45, 5),
                        key="blowfish_encrypt_output",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Encrypt", key="blowfish_encrypt_button"),
    ]
]

blowfish_decrypt_tab = [
    [
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="blowfish_decrypt_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("To decrypt:")],
                [
                    sg.Multiline(
                        "(input text goes here)",
                        size=(45, 5),
                        key="blowfish_decrypt_input",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Decrypt:")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(45, 5),
                        key="blowfish_decrypt_output",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Decrypt", key="blowfish_decrypt_button"),
    ]
]


rsa_keygen_tab = [
    [
        sg.Column(
            [
                [sg.T("P:")],
                [
                    sg.Multiline(
                        "",
                        size=(25, 5),
                        key="rsa_keygen_p",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Q:")],
                [
                    sg.Multiline(
                        "",
                        size=(25, 5),
                        key="rsa_keygen_q",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Modulus (N):")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(10, 5),
                        key="rsa_keygen_output_n",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Public Exponent (E):")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(10, 5),
                        key="rsa_keygen_output_e",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Private Exponent (D):")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(10, 5),
                        key="rsa_keygen_output_d",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Generate Keys", key="rsa_keygen_button"),
    ]
]


rsa_encrypt_tab = [
    [
        sg.Column(
            [
                [sg.T("Public Exponent (E):")],
                [
                    sg.Multiline(
                        "",
                        size=(10, 5),
                        key="rsa_encrypt_e",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Modulus (N):")],
                [
                    sg.Multiline(
                        "",
                        size=(10, 5),
                        key="rsa_encrypt_n",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("To encrypt:")],
                [
                    sg.Multiline(
                        "(input text goes here)",
                        size=(45, 5),
                        key="rsa_encrypt_input",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Encrypted:")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(45, 5),
                        key="rsa_encrypt_output",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Encrypt", key="rsa_encrypt_button"),
    ]
]


rsa_decrypt_tab = [
    [
        sg.Column(
            [
                [sg.T("Private Exponent (D):")],
                [
                    sg.Multiline(
                        "",
                        size=(10, 5),
                        key="rsa_decrypt_d",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Modulus (N):")],
                [
                    sg.Multiline(
                        "",
                        size=(10, 5),
                        key="rsa_decrypt_n",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("To decrypt (space-delimited list of int encodings):")],
                [
                    sg.Multiline(
                        "",
                        size=(45, 5),
                        key="rsa_decrypt_input",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text("Decrypted:")],
                [
                    sg.Multiline(
                        "(output will appear here)",
                        size=(45, 5),
                        key="rsa_decrypt_output",
                        visible=True,
                        disabled=True,
                    )
                ],
            ]
        ),
        sg.Button("Decrypt", key="rsa_decrypt_button"),
    ]
]




vigenere_encrypt_file_tab = [
    [
        sg.Column(
            [
                [sg.T("File to encrypt:")],

                [
                    sg.InputText(key="vigenere_encrypt_file_path"),
                    sg.FileBrowse(key="vigenere_encrypt_file_selector", enable_events=True)
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="vigenere_encrypt_file_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text(f"NOTE: Blowfish file encryption is slow and should only be used with very small files.\nEncrypted file will be in the same folder with 've' appended to the extension.",  size=(30,5), key="vigenere_encrypt_file_output_message")],

            ]
        ),
        sg.Button("Encrypt", key="vigenere_encrypt_file_button"),
    ]
]

vigenere_decrypt_file_tab = [
    [
        sg.Column(
            [
                [sg.T("File to encrypt:")],

                [
                    sg.InputText(key="vigenere_decrypt_file_path"),
                    sg.FileBrowse(key="vigenere_decrypt_file_selector", enable_events=True)
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="vigenere_decrypt_file_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text(f"Decrypted file will be in the same folder with 've' removed from the extension (so they will have the original extension).", size=(30,5), key="vigenere_decrypt_file_output_message")],
            ]
        ),
        sg.Button("Decrypt", key="vigenere_decrypt_file_button"),
    ]
]

blowfish_encrypt_file_tab = [
    [
        sg.Column(
            [
                [sg.T("File to encrypt:")],

                [
                    sg.InputText(key="blowfish_encrypt_file_path"),
                    sg.FileBrowse(key="blowfish_encrypt_file_selector", enable_events=True)
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="blowfish_encrypt_file_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text(f"Encrypted file will be in the same folder with 'be' appended to the extension.",  size=(30,5), key="blowfish_encrypt_file_output_message")],
            ]
        ),
        sg.Button("Encrypt", key="blowfish_encrypt_file_button"),
    ]
]

blowfish_decrypt_file_tab = [
    [
        sg.Column(
            [
                [sg.T("File to encrypt:")],

                [
                    sg.InputText(key="blowfish_decrypt_file_path"),
                    sg.FileBrowse(key="blowfish_decrypt_file_selector", enable_events=True)
                ],
            ]
        ),
        sg.Column(
            [
                [sg.T("Key:")],
                [
                    sg.Multiline(
                        "(key text goes here)",
                        size=(45, 5),
                        key="blowfish_decrypt_file_key",
                        visible=True,
                    )
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Text(f"Decrypted file will be in the same folder with 'be' removed from the extension (so they will have the original extension).",  size=(30,5), key="blowfish_decrypt_file_output_message")],
            ]
        ),
        sg.Button("Decrypt", key="blowfish_decrypt_file_button"),
    ]
]




# Define the elements (tab groups) that will go in the main window:
layout = [
            [
                sg.TabGroup([
                    [
                        sg.Tab("Vigenere Encrypt", vigenere_encrypt_tab),
                        sg.Tab("Vigenere Decrypt", vigenere_decrypt_tab),

                        sg.Tab("Vigenere Encrypt (file)", vigenere_encrypt_file_tab),
                        sg.Tab("Vigenere Decrypt (file)", vigenere_decrypt_file_tab),

                        sg.Tab("Blowfish Encrypt", blowfish_encrypt_tab),
                        sg.Tab("Blowfish Decrypt", blowfish_decrypt_tab),

                        sg.Tab("Blowfish Encrypt (file)", blowfish_encrypt_file_tab),
                        sg.Tab("Blowfish Decrypt (file)", blowfish_decrypt_file_tab),

                        sg.Tab("RSA Keygen", rsa_keygen_tab),
                        sg.Tab("RSA Encrypt", rsa_encrypt_tab),
                        sg.Tab("RSA Decrypt", rsa_decrypt_tab),
                    ]
                ]),

            ]
         ]

# Define the main window:
window = sg.Window('CSDS 344 Project Demo', layout, auto_size_buttons = False).Finalize()
values_dict={}

# Event loop that runs the whole time the window is opened.
while True:
    event, values_dict = window.Read() # Waits until a button is pushed or another event happens

    if event == None or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == "vigenere_encrypt_button":
        # Capitalize inputs
        values_dict['vigenere_encrypt_input'] = values_dict['vigenere_encrypt_input'].upper()
        to_encrypt = values_dict['vigenere_encrypt_input'].strip('\n')
        window["vigenere_encrypt_input"].update(to_encrypt)
        values_dict['vigenere_encrypt_key'] = values_dict['vigenere_encrypt_key'].upper()
        key = values_dict['vigenere_encrypt_key'].strip('\n')
        window["vigenere_encrypt_key"].update(key)

        print(f"encrypting by vigenere: {to_encrypt} with key {key}")
        encrypted = vigenere.vigenereEncrypt(to_encrypt, key)
        window["vigenere_encrypt_output"].update(encrypted)

    if event == "vigenere_decrypt_button":
        # Capitalize inputs
        values_dict['vigenere_decrypt_input'] = values_dict['vigenere_decrypt_input'].upper()
        to_decrypt = values_dict['vigenere_decrypt_input'].strip('\n')
        window["vigenere_decrypt_input"].update(to_decrypt)

        values_dict['vigenere_decrypt_key'] = values_dict['vigenere_decrypt_key'].upper()
        key = values_dict['vigenere_decrypt_key'].strip('\n')
        window["vigenere_decrypt_key"].update(key)

        print(f"decrypting by vigenere: {to_decrypt} with key {key}")
        decrypted = vigenere.vigenereDecrypt(to_decrypt, key)
        window["vigenere_decrypt_output"].update(decrypted)


    if event == "vigenere_encrypt_file_button":
        # Capitalize input for key
        values_dict['vigenere_encrypt_file_key'] = values_dict['vigenere_encrypt_file_key'].upper()
        key = values_dict['vigenere_encrypt_file_key'].strip('\n')
        window["vigenere_encrypt_file_key"].update(key)

        file_path = window["vigenere_encrypt_file_path"].get()
        if len(file_path) < 1:
            sg.popup("Select a file to encrypt first.")
            continue

        file_encrypted_hex_letters = vigenere.vigenereEncrypt(file_to_hex_letters.convert_to_hex_letters(file_path), key)

        file_to_hex_letters.string_to_file(file_encrypted_hex_letters,  file_path + "ve")

        head, tail = os.path.split(file_path)
        sg.popup(f"Success! Encrypted file saved as {tail}ve in {head}")


    if event == "vigenere_decrypt_file_button":
        # Capitalize input for key
        values_dict['vigenere_decrypt_file_key'] = values_dict['vigenere_decrypt_file_key'].upper()
        key = values_dict['vigenere_decrypt_file_key'].strip('\n')
        window["vigenere_decrypt_file_key"].update(key)

        file_path = window["vigenere_decrypt_file_path"].get()
        if len(file_path) < 1:
            sg.popup("Select a file to decrypt first.")
            continue

        if file_path[-2:] != "ve":
            sg.popup("Please select a Vigenere encrypted file with 've' at the end of it's extension.")
            continue

        encrypted_letters_string = file_to_hex_letters.file_to_string(file_path)
        decrypted_hex_letters = vigenere.vigenereDecrypt(encrypted_letters_string, key)
        try:
            file_to_hex_letters.convert_letters_string_to_regular_file(decrypted_hex_letters, file_path[:-2])
        except binascii.Error:
            sg.popup("Incorrect key for file.")

        head, tail = os.path.split(file_path)
        sg.popup(f"Success! Decrypted file saved as {tail[:-2]} in {head}")
        pass


    if event == "blowfish_encrypt_button":
        to_encrypt = values_dict['blowfish_encrypt_input'].strip('\n')
        key = values_dict['blowfish_encrypt_key'].strip('\n')

        print(f"encrypting by blowfish: {to_encrypt} with key {key}")
        blowfishEncryptor = blowfish.Blowfish(key)
        encrypted = blowfishEncryptor.encryptMessage(to_encrypt)

        window["blowfish_encrypt_output"].update(encrypted)

    if event == "blowfish_decrypt_button":
        to_decrypt = values_dict['blowfish_decrypt_input'].strip('\n')
        key = values_dict['blowfish_decrypt_key'].strip('\n')
        print(f"decrypting by blowfish: {to_decrypt} with key {key}")
        window["blowfish_decrypt_output"].update(f"%{to_decrypt}X{key}")

    if event == "blowfish_encrypt_file_button":
        # Capitalize input for key
        key = values_dict['blowfish_encrypt_file_key'].strip('\n')
        window["blowfish_encrypt_file_key"].update(key)

        file_path = window["blowfish_encrypt_file_path"].get()
        if len(file_path) < 1:
            sg.popup("Select a file to encrypt first.")
            continue

        blowfishEncryptor = blowfish.Blowfish(key)
        file_encrypted_hex_letters = blowfishEncryptor.encryptMessage(file_to_hex_letters.convert_to_hex_letters(file_path))

        file_to_hex_letters.string_to_file(file_encrypted_hex_letters,  file_path + "be")

        head, tail = os.path.split(file_path)
        sg.popup(f"Success! Encrypted file saved as {tail}be in {head}")


    if event == "blowfish_decrypt_file_button":
        # Capitalize input for key
        key = values_dict['blowfish_decrypt_file_key'].strip('\n')
        window["blowfish_decrypt_file_key"].update(key)

        file_path = window["blowfish_decrypt_file_path"].get()
        if len(file_path) < 1:
            sg.popup("Select a file to decrypt first.")
            continue

        if file_path[-2:] != "ve":
            sg.popup("Please select a blowfish encrypted file with 'be' at the end of it's extension.")
            continue

        encrypted_letters_string = file_to_hex_letters.file_to_string(file_path)
        decryptor = blowfish.Blowfish(key)
        decrypted_hex_letters = blowfish.decryptMessage(encrypted_letters_string)
        try:
            file_to_hex_letters.convert_letters_string_to_regular_file(decrypted_hex_letters, file_path[:-2])
        except binascii.Error:
            sg.popup("Incorrect key for file.")

        head, tail = os.path.split(file_path)
        sg.popup(f"Success! Decrypted file saved as {tail[:-2]} in {head}")
        pass

    if event == "rsa_keygen_button":
        p = values_dict['rsa_keygen_p'].strip('\n')
        q = values_dict['rsa_keygen_q'].strip('\n')


        if not p.isdigit():
            sg.popup("P should be a (prime) number.")
            continue
        p = int(p)
        if not q.isdigit():
            sg.popup("P should be a (prime) number.")
            continue
        q = int(q)

        try:
            keys = RSA.generateKeys(p, q)
            window["rsa_keygen_output_e"].update(keys['public exponent'])
            window["rsa_keygen_output_d"].update(keys['private exponent'])
            window["rsa_keygen_output_n"].update(keys['modulus'])
        except ValueError as e:
            sg.popup(e)
            continue

    if event == "rsa_encrypt_button":
        to_encrypt = values_dict['rsa_encrypt_input'].strip('\n')
        e = values_dict['rsa_encrypt_e'].strip('\n')
        n = values_dict['rsa_encrypt_n'].strip('\n')

        if not n.isdigit():
            sg.popup("N should be an integer")
            continue
        n = int(n)
        if not e.isdigit():
            sg.popup("E should be an integer")
            continue
        e = int(e)

        try:
            print(f"encrypting by rsa: {to_encrypt} with n={n} and e={e}")
            encrypted = RSA.encrypt_given_e_n(e, n, to_encrypt)
            window["rsa_encrypt_output"].update(encrypted)
        except ValueError as e:
            sg.popup(f"Error:\n{e}")
            continue

    if event == "rsa_decrypt_button":
        to_decrypt = values_dict['rsa_decrypt_input'].strip('\n')

        try:
            to_decrypt_list = [int(enc) for enc in to_decrypt.split(" ")]
        except:
            sg.popup("Invalid input")
            continue

        n = values_dict['rsa_decrypt_n'].strip('\n')
        d = values_dict['rsa_decrypt_d'].strip('\n')

        if not n.isdigit():
            sg.popup("N should be an integer")
            continue
        n = int(n)
        if not d.isdigit():
            sg.popup("D should be an integer")
            continue
        d = int(d)

        try:
            print(f"encrypting by rsa: {to_decrypt_list} with n={n} and d={d}")
            decrypted = RSA.decrypt_given_n_d(n, d, to_decrypt_list)
            window["rsa_decrypt_output"].update(decrypted)
        except ValueError as e:

            sg.popup("Confirm you have used prime inputs")
            continue


window.close()
