import random
from car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        get_num = random.randint(1, 100)
        if get_num < self.reliability:
            drive_distance = super().drive(distance)
        else:
            distance = 0
            drive_distance = super().drive(distance)
        return drive_distance

