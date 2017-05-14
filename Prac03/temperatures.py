"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Shaanan Braun'

def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c_to_f(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = f_to_c(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def c_to_f(c):
    fahrenheit = c * 9.0 / 5 + 32
    return fahrenheit

def f_to_c(f):
    celsius = (5 * f - 160) / 9
    return celsius

main()