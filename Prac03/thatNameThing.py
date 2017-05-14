
def main():
    name = get_name()
    try:
        frequency = int(input("Frequency: "))
    except ValueError:
        print("Invalid integer, default value of 2 set.")
        frequency = 2
    print_name(name, frequency)

def print_name(string, frequency):
    for ch in range(1, len(string), frequency):
        print(string[ch])

def get_name():
    name = input("Name: ")
    while name == "":
        print("Please input a name.")
        name = input("Name: ")
    return name


main()