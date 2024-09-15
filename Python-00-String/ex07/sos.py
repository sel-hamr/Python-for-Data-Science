import sys

def checkArgs():
    """Check the number of arguments"""
    if len(sys.argv) != 2:
        raise ("AssertionError: the arguments are bad")
    
def convertToMorse(text):
    """Convert the text to Morse code"""
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    morseText = ""
    for char in text:
        morseText += morse[char.upper()] + " "
    return morseText
    
def main():
    """Main function"""
    try:
        checkArgs()
        text = sys.argv[1]
        print(convertToMorse(text))
    except AssertionError as e:
        print(e)
        sys.exit()
    pass

if __name__ == "__main__":
    main()