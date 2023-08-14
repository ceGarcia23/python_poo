class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.on_going = False
        self.accelerate = False
        self.brakes = False

    def start_up(self):
        self.on_going = True

    def speed_up(self):
        self.accelerate = True

    def curb(self):
        self.brakes = True

    def state(self):
        print(
            "BRAND: ",
            self.brand,
            "\nMODEL: ",
            self.model,
            "\nON GOING: ",
            self.on_going,
            "\nACCELERATE: ",
            self.accelerate,
            "\nBRAKES: ",
            self.brakes,
        )


class Motorcycle(Vehicle):
    pass


myMotorcycle = Motorcycle("Honda", "CBR")

myMotorcycle.state()
