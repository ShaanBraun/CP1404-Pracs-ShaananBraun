

def main():
    score = float(input("Enter score: "))
    print(calc_grade(score))

def calc_grade(score):
    if score < 50 and score >= 0:
        return "Bad"
    elif score <= 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid Score"

main()