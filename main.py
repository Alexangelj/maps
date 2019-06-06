"""
This will start the program and ask which study session to start.
This will also contain a class to define the window with the correct buttons.
"""
import tkinter as tkinter
from maps import Session

closing_msg = 'Closing Program.'
invalid_input_msg = 'Input invalid. Please choose Y or N. '
open_msg = 'Would you like to start a session? Y or N? '

def main():
    start = input(open_msg).lower()
    yes = ['y','ye','yes','es','true','t']
    no = ['n','no','false','o']
    if start in yes:
        session = Session()
        session.choose_session()

    elif start in no:
        print(closing_msg)
        return
    else:
        print(invalid_input_msg)
        main()

if __name__ == "__main__":
    main()