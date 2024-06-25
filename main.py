import os
import random
import time


def clear_screen(seconds):
    if isinstance(seconds, (int, float)):
        time.sleep(seconds)
        os.system("cls" if os.name == "nt" else "clear")
    elif seconds == "x":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("\033[31mInvalid input for clear_screen\033[0m")

def hide_cursor():
    print("\033[?25l")


def show_cursor():
    print("\033[?25h")


class PinGenerator:
    def __init__(self, number_of_digits):
        self.number_of_digits = number_of_digits
        self.pin = ""

   
    def pin_process(self):
        combination = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
        '+', '[', ']', '{', '}', '\\', '|', ';', ':', '"', "'", ',', '.', 
        '<', '>', '/', '?', '~', '`']
        counter = 0
        self.pin = ""
        while counter < self.number_of_digits:
            random_element = random.choice(combination)
            self.pin += random_element
            counter += 1
        

while True: 
    try: 
        number_of_digits = int(input("How many digit pin: "))
        clear_screen("x")
        pg = PinGenerator(number_of_digits)
        while True:   
            pg.pin_process()
            print(f"PIN: {pg.pin}")
            print()
            hide_cursor()
            user_options = input("Click 'Enter' to "
            "regenerate or type 'Space/Enter' to choose new pin digits")
            if user_options == "":
                clear_screen("x")
            elif user_options == " ":
                clear_screen("x")
                show_cursor()
                break
            else:
                clear_screen("x")
                print("\033[31m Please choose from one of the options!\033[0m")
                clear_screen(1)

    except ValueError:
        print("\033[31mInvalid number! Try Again!\033[0m")
        clear_screen(0.5)
