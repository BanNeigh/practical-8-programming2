from unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Taxi", 100, 70)
    print(car.drive(55))

    print(car)


if __name__ == '__main__':
    main()

