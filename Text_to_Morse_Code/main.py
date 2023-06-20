MORSE_CODES = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "×": "-..-",
    "%": "-----",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    " ": "/"
}


def encode(string:str) -> str:
    letters = [item for item in string]

    result = [MORSE_CODES[key] for key in letters]

    return ' '.join(result)


def decode(string:str) -> str:
    morse_letters = string.split(' ')

    result = [list(MORSE_CODES.keys())[list(MORSE_CODES.values()).index(value)] for value in morse_letters]

    return ''.join(result)


def main():
    print('Welcome to console encoder and decoder of Morse Code!')
    user_input = input("Please choose an option: 'encode' or 'decode'   ").lower()

    if user_input == 'encode':
        user_string = input('Enter a string for encoding\n').upper()
        result = encode(user_string)
        print(result)
    elif user_input == 'decode':
        user_string = input('Enter a string for encoding\n').upper()
        result = decode(user_string)
        print(result.capitalize())
    else:
        print('Error, program haven\'t this feature(')


if __name__ == '__main__':
    main()
