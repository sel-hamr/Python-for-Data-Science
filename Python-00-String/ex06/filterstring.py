from ft_filter import ft_filter
import sys

def checkArgs():
    """Check the number of arguments"""
    if len(sys.argv) != 3:
        raise ("AssertionError: the arguments are bad")

def main():
    """Main function"""
    try:
        checkArgs()
        arrayArg = sys.argv[1].split(" ")
        count = sys.argv[2]
        
        print(ft_filter(lambda x: len(x) > int(count) , arrayArg))
    except AssertionError as e:
        print(e)
        sys.exit()
    pass

if __name__ == "__main__":
    main()

