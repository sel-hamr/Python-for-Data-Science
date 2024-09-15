import sys

def checkArgv():
    """Check the number of arguments"""
    argv = sys.argv
    if(len(argv) >= 3):
        raise AssertionError("error: should have one argument")
    
def getValue():
    """Get the text to analyse from the command line or from the user input"""
    argv = sys.argv
    if(len(argv) == 1):
        return(input("What is the text to count?\n"))
    else :
        return argv[1]
    
def analyseText(text :str):
    """Analyse the text and return the number of upper, lower, digits, spaces and special characters"""
    analyseObj = {
        "upper": 0,
        "lower": 0,
        "special": 0,
        "spaces": 0,
        "digits": 0
    }
    
    for item in text:
        if item.islower():
            analyseObj["lower"] += 1
        elif item.isdigit():
            analyseObj['digits'] += 1
        elif item.isspace():
            analyseObj["spaces"] += 1
        elif item.isupper():
            analyseObj["upper"] += 1
        else :
            analyseObj["special"] += 1
    return analyseObj
    
    
def main():
    """Main function"""
    try:
        checkArgv()
    except AssertionError as msj:
        print(msj)
        exit(1)
    text = getValue()
    analyseObj = analyseText(text)
    print(f"The text contains {len(text)} characters:")
    print(f"- {analyseObj['upper']} upper letters")
    print(f"- {analyseObj['lower']} lower letters")
    print(f"- {analyseObj['special']} punctuation marks")
    print(f"- {analyseObj['spaces']} spaces")
    print(f"- {analyseObj['digits']} digits")
    pass

if __name__ == "__main__":
    main()