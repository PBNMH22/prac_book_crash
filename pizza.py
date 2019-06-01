def make_pizza(size,*toppings):
    print('\nMaking a '+ str(size)+ '-inch piizza with following toppings : ')
    for topping in toppings:
        print('-'+topping)