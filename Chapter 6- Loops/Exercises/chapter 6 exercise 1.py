#Exercise 1: Pizza Toppings :ballot_box_with_check:
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.
pizza_topping=(input("enter your favorite toppings:"))
pizza_topping+="enter 'quit' when you are finished:"
while pizza_topping!='quit':
    pizza_topping=input(pizza_topping)
    if pizza_topping !='quit':
       print("I will add"+pizza_topping+"to your pizza.")
    else:
        break
