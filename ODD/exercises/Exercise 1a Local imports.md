## Exercise 1a: Local importing

#### Goal

Retrival practice in "basic" importing.

#### Preparation

(none)

#### Tasks

We are simulating having code in one folder and calling the code from the folder above. 

0. Create a file in the `src/` folder called `daily_menu.py` and copy the code below
   into it.

```python
def todays_special():
    pizza_margherita = make_margherita_pizza()

    schorle = make_apfelschorle()

    print("Today's special is ready! Buon Appetito!")
    return pizza_margherita, schorle

pizza, drink = todays_special()
```

1. Figure out what import statements are missing, either by visual inspection or
   by running the code and seeing what does. Add the missing import statements at
   the top of the file. You may need to inspect the files in `src/italianfood/`.

2. Run `daily_menu.py`. Did it work?
