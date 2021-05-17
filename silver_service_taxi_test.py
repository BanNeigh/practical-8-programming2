from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("SilverBird", 100, 2)
    taxi.drive(18)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()