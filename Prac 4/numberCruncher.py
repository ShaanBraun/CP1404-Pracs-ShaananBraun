INPUT_LENGTH = 5

def main():
    number_list = []
    for i in range(INPUT_LENGTH):
        try:
            number_list.append(float(input("Number: ")))
        except ValueError:
            print("Invalid Number, number ignored.")

    max_number = max(number_list)
    min_number = min(number_list)
    avg_number = sum(number_list)/len(number_list)

    print("First number is {}".format(number_list[0]))
    print("Last number is {}".format(number_list[-1]))
    print("The smallest number is {}".format(min_number))
    print("The largest number is {}".format(max_number))
    print("The average of the numbers is {}".format(avg_number))






main()