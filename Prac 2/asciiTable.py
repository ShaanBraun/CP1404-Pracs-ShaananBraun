
LOWER_ASCII = 33
UPPER_ASCII = 127

endProgram = False

while not endProgram:
    menuOption = int(input("Menu Options\n1: Character and ASCII Number Lookup\n2: ASCII Table\n3: Exit\n\nYour choice:"))
    if menuOption == 1:
        character = input("Enter a character: ")
        print("The ASCII code for {} is {}".format(character, ord(character)))

        asciiNumber = int(input("Enter a number between {} and {}: ".format(LOWER_ASCII, UPPER_ASCII)))
        if LOWER_ASCII <= asciiNumber <= UPPER_ASCII:
            print("The character for {} is {}".format(asciiNumber, chr(asciiNumber)))
        else:
            print("Number out of Range given.")
    elif menuOption == 2:
        print("{:>3}{:>5}".format("ASCII", "Char"))
        for i in range(LOWER_ASCII, UPPER_ASCII+1):
            print("{:>3}{:>5}".format(i, chr(i)))
    elif menuOption == 3:
        endProgram = True
    else:
        print("Not a valid choice, please make another selection.")
