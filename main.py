import random

from screen_manager import sm


class PinGenerator:
    def __init__(self, number_of_digits, pin_complexity_level):
        self.number_of_digits = number_of_digits
        self.pin_complexity_level = pin_complexity_level
        self.pin = ""


    def pin_process(self):
        mixed_combination = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
                             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                             'y', 'z','!', '@', '#', '$', '%', '^', '&', '*', 
                             '(', ')', '-', '_', '=','+', '[', ']', '{', '}',
                             '\\', '|', ';', ':', '"', "'", ',', '.',  '<', 
                             '>', '/', '?', '~', '`']

        colors = [sm.black, sm.red, sm.green, sm.yellow, sm.blue,
        sm.purple, sm.cyan, sm.white, sm.brightBlack, sm.brightRed,
        sm.brightGreen, sm.brightYellow, sm.brightBlue, sm.brightPurple, 
        sm.brightCyan, sm.brightWhite, sm.blackDark, sm.redDark, 
        sm.greenDark, sm.yellowDark, sm.blueDark, sm.purpleDark, 
        sm.cyanDark, sm.whiteDark]
        if self.pin_complexity_level == "3":
            counter = 0
            self.pin = ""
            while counter < self.number_of_digits:
                random_element = random.choice(mixed_combination)
                random_color = random.choice(colors)
                
                random_mixed = random_color + random_element + sm.colorLimit
                self.pin += random_mixed
        
                counter += 1
        elif self.pin_complexity_level == "2":
            number_counter = 0 
            upper_counter = 0
            lower_counter = 0
            special_counter = 0

            self.pin = ""
            while True:
                random_element = random.choice(mixed_combination)
                
                if random_element.isdigit():
                    if number_counter < 2:
                        number_counter += 1
                    else:
                        continue
                elif random_element.isupper():
                    if upper_counter < 2:
                        upper_counter += 1
                    else:
                        continue
                elif random_element.islower():
                    if lower_counter < 2:
                        lower_counter += 1
                    else:
                        continue
                else:
                    if special_counter < 2:
                        special_counter += 1
                    else:
                        continue
                    
                random_color = random.choice(colors)
                
                random_mixed = random_color + random_element + sm.colorLimit
                self.pin += random_mixed
                if (number_counter == 2 and 
                    upper_counter == 2 and 
                    lower_counter == 2 and
                    special_counter == 2):
                    break

        else:
            number_counter = 0 
            upper_counter = 0
            lower_counter = 0
            special_counter = 0

            self.pin = ""
            while True:
                random_element = random.choice(mixed_combination)

                if random_element.isdigit():
                    if number_counter < 1:
                        number_counter += 1
                    else:
                        continue
                elif random_element.isupper():
                    if upper_counter < 1:
                        upper_counter += 1
                    else:
                        continue
                elif random_element.islower():
                    if lower_counter < 1:
                        lower_counter += 1
                    else:
                        continue
                else:
                    if special_counter < 1:
                        special_counter += 1
                    else:
                        continue

                random_color = random.choice(colors)

                random_mixed = random_color + random_element + sm.colorLimit
                self.pin += random_mixed
                if (number_counter == 1 and 
                    upper_counter == 1 and 
                    lower_counter == 1 and
                    special_counter == 1):
                    break

while True: 
    try: 
        while True:
            print(f"{sm.redDark}Disclaimer:{sm.brightPurple} Pin digit length is" 
                  "\nsubject to a custom pin length for options other than option" 
                  f" '3'.{sm.colorLimit}")
            print()
            pin_complexity_level = input(
                f"{sm.brightGreen}Enter{sm.colorLimit} a {sm.blueDark}number"
                f"{sm.colorLimit} of {sm.blackDark}pin complexity{sm.colorLimit}" 
                f" {sm.brightYellow}type:{sm.colorLimit} ({sm.redDark}1"
                f"{sm.colorLimit}), ({sm.brightCyan}2{sm.colorLimit}) or" 
                f" ({sm.brightGreen}3{sm.colorLimit}): "
                ).strip()
            if (pin_complexity_level == "1" or
                  pin_complexity_level == "2" or
                  pin_complexity_level == "3"):
                break
            else:
                sm.cls()
        sm.bold_text()
        sm.show_cursor()
        if pin_complexity_level == "3":
            number_of_digits = int(input(f"{sm.blueDark}How many digit" 
                                         f" pin{sm.colorLimit}: "))
        else:
            number_of_digits = ""
        sm.cls()
        pg = PinGenerator(number_of_digits, pin_complexity_level)
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
