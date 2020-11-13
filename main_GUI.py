import PySimpleGUI as sg
import vigenere
# TODO: Restrict inputs to only valid characters
# Encipher dfeciper pjrasomgh


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
                [sg.Text("To cipher:")],
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
                [sg.Text("Ciphered:")],
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
        sg.Button("Cipher", key="vigenere_encrypt_button"),
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
                [sg.Text("To decipher:")],
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
                [sg.Text("Deciphered:")],
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
        sg.Button("Decipher", key="vigenere_decrypt_button"),
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

# Define the elements (tab groups) that will go in the main window:
layout = [
            [
                sg.TabGroup([
                    [
                        sg.Tab("Vigenere Cipher", vigenere_encrypt_tab),
                        sg.Tab("Vigenere Decipher", vigenere_decrypt_tab),

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
        to_encrypt = values_dict['vigenere_encrypt_input'].strip('\n')
        key = values_dict['vigenere_encrypt_key'].strip('\n')
        print(f"encrypting by vigenere: {to_encrypt} with key {key}")
        encrypted = vigenere.vigenereEncipher(to_encrypt, key)
        window["vigenere_encrypt_output"].update(encrypted)

    if event == "vigenere_decrypt_button":
        to_decrypt = values_dict['vigenere_decrypt_input'].strip('\n')
        key = values_dict['vigenere_decrypt_key'].strip('\n')
        print(f"decrypting by vigenere: {to_decrypt} with key {key}")
        decrypted = vigenere.vigenereDecipher(to_decrypt, key)
        window["vigenere_decrypt_output"].update(decrypted)

    if event == "blowfish_encrypt_button":
        to_encrypt = values_dict['blowfish_encrypt_input'].strip('\n')
        key = values_dict['blowfish_encrypt_key'].strip('\n')
        print(f"encrypting by blowfish: {to_encrypt} with key {key}")
        window["blowfish_encrypt_output"].update(f"%{to_encrypt}X{key}")

    if event == "blowfish_decrypt_button":
        to_decrypt = values_dict['blowfish_decrypt_input'].strip('\n')
        key = values_dict['blowfish_decrypt_key'].strip('\n')
        print(f"decrypting by blowfish: {to_decrypt} with key {key}")
        window["blowfish_decrypt_output"].update(f"%{to_decrypt}X{key}")


window.close()
