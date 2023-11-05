import sys
from py_1 import main as greeting
from py_2 import main as exiting

def main():
    try:
        if sys.argv[1] == 'greet':
            greeting()
        elif sys.argv[1] == 'goodbye':
            exiting()
        else:
            print('Unknown argument')
    except IndexError:
        print("Argument must be 'greet' or 'goodbye'")

    
if __name__ == "__main__":     
    main()
