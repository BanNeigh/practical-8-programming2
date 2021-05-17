from taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        fare = self.flagfall + super().get_fare()
        return fare

    def __str__(self):
        print(f"{super().__str__()} plus flagfall of ${self.flagfall}")

