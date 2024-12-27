# Dictionary mapping characters to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}

def convert_to_morse_code(input_string):
    input_string = input_string.upper()
    morse_code = ""
    for char in input_string:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += " "
    return morse_code
if __name__ == "__main__":
    input_string = input("Enter a string to convert to Morse code: ")
    morse_code = convert_to_morse_code(input_string)
    print(f"Morse Code: {morse_code}")
