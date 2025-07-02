from italianfood.dough import PizzaDough
from italianfood.ovens import bake_pizza


class Pizza:
    dough: PizzaDough
    num_pizzas: int = 1
    is_ready: bool = False

    def __init__(self, dough, num_pizza_balls):
        if num_pizza_balls < 1:
            raise ValueError("Number of pizza balls must be at least 1.")
        self.num_pizzas = num_pizza_balls
        self.dough = dough
        self.make_pizza_balls()

    def make_pizza_balls(self):
        self.weight_per_pizza_ball = self.dough.total_weight / self.num_pizzas
        print(
            f"Each Pizza will be made out of {self.weight_per_pizza_ball} g dough.\n..."
        )
        print("Now imagine expert pizza tossing skills!\n...")
        return self

    def add_toppings(self, toppings):
        self.toppings = toppings
        print(f"Adding {self.toppings} to pizza(s).\n...")
        return self


def make_margherita_pizza(num_pizzas: int = 1):
    total_flour_weight = 180 * num_pizzas
    total_water_weight = 126 * num_pizzas
    total_salt_weight = 2 * num_pizzas
    total_yeast_weight = 1 * num_pizzas

    dough = PizzaDough(
        flour_weight=total_flour_weight,
        water_weight=total_water_weight,
        salt_weight=total_salt_weight,
        yeast_weight=total_yeast_weight,
    )

    toppings = ["tomato sauce", "mozzarella cheese", "fresh basil"]

    pizza = Pizza(dough=dough, num_pizza_balls=num_pizzas)
    pizza.add_toppings(toppings)

    baked_pizza = bake_pizza(pizza)

    return baked_pizza
