# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}

# Joins individual line encoding from encrypt_line()
def encrypt(message):
    return "\n".join(
        encrypt_line(line) for line in message.splitlines()
    )

# Encrypts a line of code using the Morse code dictionary
def encrypt_line(message):
    cipher = ''
    for letter in message:
        cipher += MORSE_CODE_DICT[letter] + ' '

    return cipher

# Joins individual line decoding from decrypt_line()
def decrypt(message):
    return "\n".join(
        decrypt_line(line) for line in message.splitlines()
    )

# Decrypts a line of code using the Morse code dictionary
def decrypt_line(message):
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter

        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher

# Calls encrypt() on each line of code in an input until input is empty
def encryptor():
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    result = encrypt("\n".join(lines).upper())
    return(result)

# Calls decrypt() on each line of code in an input until input is empty
def decryptor():
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    result = decrypt("\n".join(lines).upper())
    return(result)

# Runs the encoder/decoder for a message based on user input
def main():
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
  __  __                        _____          _        _______                  _       _             
 |  \/  |                      / ____|        | |      |__   __|                | |     | |            
 | \  / | ___  _ __ ___  ___  | |     ___   __| | ___     | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
 | |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \    | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
 | |  | | (_) | |  \__ \  __/ | |___| (_) | (_| |  __/    | | | | (_| | | | \__ \ | (_| | || (_) | |   
 |_|  |_|\___/|_|  |___/\___|  \_____\___/ \__,_|\___|    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   
                                                                                                       
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                                                      
                                    M@d3 With ♥ -- VirusZzWarning          
                         Read my blogs on : https://viruszzwarning.medium.com/                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print("Choose from below:")

    opt = input(
        "• Press 1 to translate Text to Morse code. \n• Press 2 to translate Morse code to Text.\nType here: ")
    opt = int(opt)

    if (opt == 1):
        print("Put your text here to encrypt it. Press Enter on a blank line when finished.")
        print(encryptor())
    elif (opt == 2):
        print("Put your Morse code here to decrypt it. Press Enter on a blank line when finished.")
        print(decryptor())
    else:
        print("Please choose a valid input.")


if __name__ == '__main__':
    main()
