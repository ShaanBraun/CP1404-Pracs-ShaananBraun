import random

endProgram = False

while not endProgram:
    menuOption = int(input(
        "Menu Options\n1: Name Input\n2: Read name from file\n3: Write Numbers to file\n4: Add Numbers from File\n5: Exit\n\nYour choice:"))
    if menuOption == 1:
        nameFile = open("name.txt", "w")
        userName = input("What is your name: ")
        print(userName, file=nameFile)
        print("Your name has successfully been written to the file.")
        nameFile.close()
    elif menuOption == 2:
        nameFile = open("name.txt", "r")
        print("Your name is: {}\n".format(nameFile.readline()))
        nameFile.close()
    elif menuOption == 3:
        numberFile = open("numbers.txt", "r")
        result = int(numberFile.readline()) + int(numberFile.readline())
        print("Result is {}\n".format(result))
        numberFile.close()
    elif menuOption == 4:
        numberLongFile = open("numbersLong.txt", "w+")
        result = 0
        # Generate random list of numbers so we can add them all together
        for i in range(1, random.randint(5, 100)):
            print(str(random.randint(1, 20)), file=numberLongFile)

        # Reset file position to beggining
        numberLongFile.seek(0, 0)

        # Add all lines together
        for line_str in numberLongFile:
            result += int(line_str)
        print("The total of all values in the file are {}.\n".format(result))
        numberLongFile.close()
    elif menuOption == 5:
        endProgram = True
    else:
        print("Not a valid choice, please make another selection.")
