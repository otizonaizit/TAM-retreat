class PizzaDough:
    flour_weight: int
    water_weight: int
    salt_weight: int
    yeast_weight: int

    def __init__(self, flour_weight, water_weight, salt_weight, yeast_weight):
        self.hydration = water_weight / flour_weight
        self.total_weight = flour_weight + water_weight + salt_weight + yeast_weight
        self.prepare_dough()

    def prepare_dough(self):
        print("Kneading the dough. This will be delicious!\n...")



