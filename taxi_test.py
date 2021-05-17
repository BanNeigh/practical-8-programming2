from prac_08.taxi import Taxi


def main():
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print(prius)
    print(prius.get_fare())

    prius.start_fare()
    prius.drive(100)
    print(prius)
    print(prius.get_fare())


if __name__ == '__main__':
    main()

