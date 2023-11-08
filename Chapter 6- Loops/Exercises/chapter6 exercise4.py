## Exercise 4: Deli :ballot_box_with_check:
#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
Sandwich_order=["Chicken Club sandwich","Prawns sandwich","Zinger sandwich","Veggie sandwich","Dynamit sandwich"]
Finished_Sandwich=[]
while Sandwich_order:
    sandwich=Sandwich_order.pop()
    print("I am working on_"+sandwich)
    Finished_Sandwich.append(sandwich)
for sandwich in Finished_Sandwich:
    print("I made a_"+sandwich )