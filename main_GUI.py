import PySimpleGUI as sg
import vigenere
import blowfish
import os
import file_to_hex_letters
import binascii


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
                [sg.Text(f"Encrypted file will be in the same folder with 've' appended to the extension.", key="vigenere_encrypt_file_output_message")],
            ]
        ),
        sg.Button("Encrypt", key="vigenere_encrypt_file_button"),
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

                        sg.Tab("Blowfish Encrypt", blowfish_encrypt_tab),
                        sg.Tab("Blowfish Decrypt", blowfish_decrypt_tab),
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
            continue # TODO: test that this continue does what we want

        file_encrypted_hex_letters = vigenere.vigenereEncrypt(file_to_hex_letters.convert_to_hex_letters(file_path, file_path + "ve"), key)

        #with open(file_path + "ve", "wb") as f_out:
        #    f_out.write(
        #        binascii.unhexlify(file_encrypted_hex_letters)
        #    )

        #file_to_hex_letters.convert_letters_string_to_regular_file(file_encrypted_hex_letters, file_path + "ve")

        head, tail = os.path.split(file_path)
        sg.popup(f"Success! File saved as {head}ve in {tail}")

        sg.popup(f"trying to decrypt JUST FOR TESTING ***")

        sg.popup(f"Success! File saved as {head}ve in {tail}")

        decrypted_hex_letters = vigenere.vigenereDecrypt(file_to_hex_letters.open_encrypted_file_as_letters_string(file_path + "ve"), key)
        file_to_hex_letters.convert_letters_string_to_regular_file(decrypted_hex_letters, file_path + "veun")

    ''' event doesn't trigger?
    if event == "vigenere_encrypt_file_selector":
        print(window)

        file_path = window["vigenere_encrypt_file_path"]
        head, tail = os.path.split(file_path)

        window["vigenere_encrypt_file_output_message"].update(f"Encrypted file will be saved in same folder as {head}ve")
    '''


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


window.close()
