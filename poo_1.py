class Car:
    def __init__(self):
        self.__longChassis = 250
        self.__widthChassis = 120
        self.__wheel = 4
        self.__onGoing = False

    def starUp(self, starups):
        self.__onGoing = starups

        if self.__onGoing:
            return "The car is running"
        else:
            return "the car is stopped"

    def state(self):
        print(
            "the car has ",
            self.__wheel,
            " wheel. a width of ",
            self.__widthChassis,
            " and a length of ",
            self.__longChassis,
        )


myCar = Car()


print(myCar.starUp(True))

myCar.state()

print("-----------Next we create the second object")

myCar2 = Car()

print(myCar2.starUp(False))


myCar2.state()
