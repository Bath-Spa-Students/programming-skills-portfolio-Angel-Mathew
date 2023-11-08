#Exercise 2: Movie Tickets: :ballot_box_with_check:
#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket
Tickets={"tickets for under age3":"free","tickets for the age between 3 and 12":"$10","tickets for the age over 12":"$15"}
Age=(input("enter your age:"))
Age+="_enter 'quit' when you are finished:"
while True:
   Age=input(Age)
   if Age=='quit':
      break
   Age=int(Age)
   if Age<3:
      print("Tickets are free!")
   elif Age<13:
      print("Tickets are $10")
   else:
      print("Tickets are $15")