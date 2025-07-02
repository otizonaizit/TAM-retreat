from italianfood.make_pizzas import make_margherita_pizza


def pizza_tasting_menu():
    pizza_margherita = make_margherita_pizza(num_pizzas=10)

    all_pizzas = [pizza_margherita]

    return all_pizzas


if __name__ == "__main__":
    pizzas = pizza_tasting_menu()
