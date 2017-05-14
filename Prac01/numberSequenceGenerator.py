
print("Welcome to the number generator!")
print()
print("Choose from the folowing options by typing in the right number.")
print()
print("Menu:")
print("1. Show the Even numbers from X to Y")
print("2. Show the odd numbers from X to Y")
print("3. Show the squares from X to Y")
print("4. Exit the program")
print()
choice = int(input("Your menu choice: "))

while choice != 4:
    print("Nice choice! Now input X and Y.")
    x = int(input("X: "))
    y = int(input("Y: "))

    if choice == 1:
        if x%2 != 0:
            x += 1
        for i in range(x, y+1, 2):
            print(i, end=' ')
    elif choice == 2:
        if x%2 == 0:
            x+=1
        for i in range(x, y+1, 2):
            print(i, end=' ')
    elif choice == 3:
        for i in range(x, y+1, 1):
            print(i^2, end=' ')
    else:
        print("Invalid Menu option, try again.")

    print()
    print("Menu:")
    print("1. Show the Even numbers from X to Y")
    print("2. Show the odd numbers from X to Y")
    print("3. Show the squares from X to Y")
    print("4. Exit the program")
    print()
    choice = int(input("Your menu choice: "))