#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.
Names=["Ann","Paul","Annette","Mathew"]
print(Names[0]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print(Names[1]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print(Names[2]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print(Names[3]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print("Ann:Sorry I will not be able to attended the dinner since I my car is at workshop\n")
del(Names[0])
Names.insert(0,"Elizabeth_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
#Names=["Elizabeth","Paul","Annette","Mathew"]
print(Names[0]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print(Names[1]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print(Names[2]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
print(Names[3]+"_Inviting all to a dinner on 21 October 2023, at 8:00pm,at Olive Rose Theodore's house")
