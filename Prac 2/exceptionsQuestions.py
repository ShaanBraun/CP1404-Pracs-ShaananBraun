try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1: ValueError occurs when Numerator or Denominator are not numbers
# Q2: ZeroDivisionError occurs when the denominator is zero\
# Q3: not that I can see......
