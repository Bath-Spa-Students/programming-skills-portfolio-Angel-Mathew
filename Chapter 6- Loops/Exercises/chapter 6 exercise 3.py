## Exercise 3: Infinity :ballot_box_with_check:
#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
pizza_topping=(input("enter your favorite toppings:"))
pizza_topping+="enter 'quit' when you are finished:"
while True:
    prompt=input(pizza_topping)
    if pizza_topping !='quit':
       print("I will add_"+pizza_topping+"to the pizza.")
    else:
        break
       