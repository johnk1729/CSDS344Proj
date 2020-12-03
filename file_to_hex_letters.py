import binascii
import vigenere
import pickle
# This is an inefficient but functional way of converting any file into a set of all caps letters (compatible with our
# encryption algorithms) and back again. It should satisfy the requirement about images.

def convert_to_hex_letters(input_filename, output_filename = None):
    filename = input_filename
    with open(filename, 'rb') as f:
        content = f.read()
    hex_string = str(binascii.hexlify(content))[2:-1]

    hex_normal_to_letters_map = {
        '0': "A",
        '1': "B",
        '2': "C",
        '3': "D",
        '4': "E",
        '5': "F",
        '6': "G",
        '7': "H",
        '8': "I",
        '9': "J",
        'a': "K",
        'b': "L",
        'c': "M",
        'd': "N",
        'e': "O",
        'f': "P",
    }

    translator = hex_string.maketrans(hex_normal_to_letters_map)
    letters_only_hex = hex_string.translate(translator)

    #if output_filename != None:
    #    with open(output_filename, "wb") as f_out:
    #        f_out.write(bytes(letters_only_hex, encoding="UTF8"))


    return letters_only_hex

def convert_letters_string_to_regular_file(letters_string, output_filename):

    letters_to_hex_normal_map = {
        "A": '0',
        "B": '1',
        "C": '2',
        "D": '3',
        "E": '4',
        "F": '5',
        "G": '6',
        "H": '7',
        "I": '8',
        "J": '9',
        "K": 'a',
        "L": 'b',
        "M": 'c',
        "N": 'd',
        "O": 'e',
        "P": 'f',
    }

    translator = letters_string.maketrans(letters_to_hex_normal_map)
    normal_hex = letters_string.translate(translator)
    print(normal_hex)

    unhexified = binascii.unhexlify(normal_hex)
    with open(output_filename, "wb") as f_out:
        f_out.write(
            unhexified
        )

def open_encrypted_file_as_letters_string(filename): # TODO: somethign wrong is happening here...
    with open(filename, "r", encoding="UTF8") as f_in:
        return str(f_in.read())


def string_to_file(string, filename):
    pickle.dump(string, open(filename, "wb"))

def file_to_string(filename):
    return pickle.load(open(filename, "rb"))
