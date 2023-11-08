# Exercise 5: No Pastrami :ballot_box_with_check:
#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
Sandwich_order=["pastrami sandwich","Chicken Club sandwich","Prawns sandwich","Zinger sandwich","Veggie sandwich","Dynamit sandwich"]
Finished_Sandwich=[]
print("I am sorry,we are out of pastrami today")
while 'pastrami sandwich'in Sandwich_order:
    Sandwich_order.remove('pastrami sandwich')
while Sandwich_order:
    sandwich=Sandwich_order.pop()
    print("I am working on_"+sandwich)
    Finished_Sandwich.append(sandwich)
for sandwich in Finished_Sandwich:
    print("I made a_"+sandwich )