name = str(input("What is your name?: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
print()

choice = str(input("Menu Choice: "))

while choice != "Q":
    if choice == "H":
        print("Hello "+name)
    elif choice == "G":
        print("Goodbye "+name)
    else:
        print("Invalid Choice")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    print()
    choice = str(input("Menu Choice: "))

print('Finished')