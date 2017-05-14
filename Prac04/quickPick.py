import random


def main():
    number_of_quick_picks = 0
    while number_of_quick_picks <= 0:
        try:
            number_of_quick_picks = int(input("How many quick picks do you want: "))
        except ValueError:
            print("Invalid value, please try again.")

    for i in range(number_of_quick_picks):
        number_list = number_generator(6)
        for j in number_list:
            print("{:>3}".format(j), end="")
        print()


def number_generator(length):
    number_list = []
    for i in range(length):
        rand = random.randint(1, 45)
        while rand in number_list:
            rand = random.randint(1, 45)

        number_list.append(rand)
    number_list.sort()
    return number_list


main()
