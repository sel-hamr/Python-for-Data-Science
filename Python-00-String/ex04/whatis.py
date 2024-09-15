import sys

argv = sys.argv
if len(argv) == 3:
    print("AssertionError: more than one argument is provided")
elif len(argv) == 1:
    print("")
else :
    try :
        result = int(argv[1])
    except :
        print('AssertionError: argument is not an integer')
    else :
        if result % 2 == 0:
                print('I\'m Even.')
        else:
                print('I\'m Odd.')