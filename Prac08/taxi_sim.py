from Prac08.taxi import Taxi, SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    choice = input("q)uit, c)hoose, d)rive\n")
    bill_to_date = 0
    taxi_choice = Taxi
    while choice not in ["q", "Q"]:
        if choice in ["c", "C"]:
            print_taxis(taxis)
            try:
                taxi_choice_input = int(input("Choose taxi: "))
                taxi_choice = taxis[taxi_choice_input]
                print(taxi_choice)
            except ValueError:
                print("Not a valid number")
            except IndexError:
                print("That taxi does not exist")

        elif choice in ["d", "D"]:
            try:
                distance = int(input("Drive how far? "))
                taxi_choice.start_fare()
                if taxi_choice.drive(distance) == 0:
                    print("Oh dear the taxi is out of fuel! Better call another.")
                bill_to_date += taxi_choice.get_fare()
                print("Your {} trip cost you ${}".format(taxi_choice.name, taxi_choice.get_fare()))
            except TypeError:
                print("You must choose a taxi first.")
            except ValueError:
                print("That is not a valid distance.")

        else:
            print("That is not a valid option, try again.")

        print("Bill to date: ${}".format(bill_to_date))
        choice = input("q)uit, c)hoose, d)rive\n")
    print("Total trip cost: ${}".format(bill_to_date))
    print("Taxis are now:")
    print_taxis(taxis)

def print_taxis(taxis):
    id = 0
    for taxi in taxis:
        print("{} - {}".format(id, taxi))
        id += 1


main()
