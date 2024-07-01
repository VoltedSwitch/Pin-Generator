import random

from screen_manager import ScreenManager

sm = ScreenManager()

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
        
        colors = [sm.black, sm.red, sm.green, sm.yellow, sm.blue,
        sm.purple, sm.cyan, sm.white, sm.brightBlack, sm.brightRed,
        sm.brightGreen, sm.brightYellow, sm.brightBlue, sm.brightPurple, 
        sm.brightCyan, sm.brightWhite, sm.blackDark, sm.redDark, 
        sm.greenDark, sm.yellowDark, sm.blueDark, sm.purpleDark, 
        sm.cyanDark, sm.whiteDark]
        
        counter = 0
        self.pin = ""
        while counter < self.number_of_digits:
            random_element = random.choice(combination)
            random_color = random.choice(colors)
            random_mixed = random_color + random_element + sm.colorLimit
            self.pin += random_mixed
            counter += 1

while True: 
    try: 
        sm.bold_text()
        sm.show_cursor()
        number_of_digits = int(input(f"{sm.blueDark}How many digit pin "
        f"{sm.colorLimit}: "))
        sm.cls()
        pg = PinGenerator(number_of_digits)
        while True:   
            pg.pin_process()
            print(f"{sm.underlineText}PIN:{sm.underlineLimit} {sm.boldText}{pg.pin}")
            print()
            sm.hide_cursor()
            print(f"{sm.purpleDark}Click {sm.colorLimit}'"
            f"{sm.brightYellow}Enter{sm.colorLimit}'{sm.colorLimit} "
            f"{sm.purpleDark}to regenerate or\nClick{sm.colorLimit} "
            f"'{sm.brightGreen}Space Bar{sm.colorLimit}'{sm.colorLimit} Then "
            f"{sm.purpleDark}Click{sm.colorLimit} {sm.colorLimit}'{sm.brightCyan}"
            f"Enter{sm.colorLimit}'{sm.purpleDark} to choose new pin digits "
            f"{sm.colorLimit}")
            user_options = input()
            if user_options == "":
                sm.cls()
            elif user_options == " ":
                sm.cls()
                sm.show_cursor()
                break
            else:
                sm.cls()
                print("\033[31m Please choose from one of the options!\033[0m")
                sm.delay_cls(1)
    
    except ValueError:
        sm.hide_cursor()
        print("\033[31mInvalid number! Try Again!\033[0m")
        sm.delay_cls(0.5)
