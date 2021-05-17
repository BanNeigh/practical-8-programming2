from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    total = 0
    menu_choices = "q)uit, c)hoose, d)rive"
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's Drive")
    print(menu_choices)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            choose_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                total += cost

            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option")

        print(f"Bill to date : ${total:.2f}")
        print(menu_choices)
        menu_choice = input(">>> ").lower()

    print("Taxis are now: ")
    choose_taxi(taxis)


def choose_taxi(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
