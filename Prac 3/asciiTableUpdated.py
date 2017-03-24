
def main():
    LOWER_ASCII = 33
    UPPER_ASCII = 127

    end_program = False
    while not end_program:
        menu_option = int(input("Menu Options\n1: Character and ASCII Number Lookup\n2: ASCII Table\n3: Exit\n\nYour choice:"))
        if menu_option == 1:
            character = input("Enter a character: ")
            print("The ASCII code for {} is {}".format(character, ord(character)))

            ascii_number = get_number(LOWER_ASCII, UPPER_ASCII)
            print("The character for {} is {}".format(ascii_number, chr(ascii_number)))
        elif menu_option == 2:
            print("{:>3}{:>5}".format("ASCII", "Char"))
            for i in range(LOWER_ASCII, UPPER_ASCII+1):
                print("{:>3}{:>5}".format(i, chr(i)))
        elif menu_option == 3:
            end_program = True
        else:
            print("Not a valid choice, please make another selection.")


def get_number(lower_bound, upper_bound):
    valid_number = False
    while not valid_number:
        try:
            ascii_number = int(input("Enter a number between {} and {}: ".format(lower_bound, upper_bound)))
            if lower_bound <= ascii_number <= upper_bound:
                return ascii_number
            else:
                "Not within the given range, please try again."
        except ValueError:
            print("Ivalid input, please choose a number")


main()