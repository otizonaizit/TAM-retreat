def bake_pizza(pizza, baking_time=2, temperature=450):
    # just pretend there is some complicated code 
    print(
        f"The Pizza was baked for {baking_time} min at {temperature} C. It is now ready!\n..."
    )
    pizza.is_ready = True
    return pizza
