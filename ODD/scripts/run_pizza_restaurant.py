from italianfood.make_pizzas import make_margarita_pizza


def pizza_tasing_menu():
    pizza_margarita = make_margarita_pizza(num_pizzas=1)

    all_pizzas = [pizza_margarita]

    return all_pizzas


if __name__ == "__main__":
    pizzas = pizza_tasing_menu()
