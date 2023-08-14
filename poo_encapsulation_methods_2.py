class Car:
    def __init__(self):
        self.__longChassis = 250
        self.__widthChassis = 120
        self.__wheel = 4
        self.__onGoing = False

    def star_up(self, starups):
        self.__onGoing = starups

        if self.__onGoing:
            check = self.__internal_check()

        elif self.__onGoing and check:
            return "The car is running"

        elif self.__onGoing and check == False:
            return "Something is wrong in the check, we can not start"
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

    def __internal_check(self):
        print("Performing internal check")

        self.gasoline = "ok"
        self.oil = "ok"
        self.doors = "closed"

        if self.gasoline == "ok" and self.oil == "ok" and self.doors == "closed":
            return True
        else:
            return False


myCar = Car()


print(myCar.star_up(True))

myCar.state()

print("-----------------------Next we create the second object")

myCar2 = Car()

print(myCar2.star_up(False))

myCar2.state()
