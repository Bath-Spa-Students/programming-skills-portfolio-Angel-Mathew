#Exercise 5: USB Shopper ☑️
#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.
#1method: Number_of_USBStick=(50/6)
#print(Number_of_USBStick)
#Total=((50/8))
##print(Total)
#Balance=((50/8))
#print(Balance)
             
#2nd method:#Number_of_USBsticks=(50/6)
#print(Number_of_USBsticks)
#Total=(50-Number_of_USBsticks)
#print(Total)
#Balance=(50-Number_of_USBsticks)
#print(Balance)

#3 method:
#Total_Number_of_USBsticks=(50/6)
#print(int(Total_Number_of_USBsticks))
#Total_amount_of_the_USBsticks=(6*Total_Number_of_USBsticks)
#print(int(Total_amount_of_the_USBsticks))
#Number_of_USBsticks=int(input("Enter Number_of_USBsticks:"))
#Total_amount_to_pay=(Total_amount_of_the_USBsticks-Number_of_USBsticks)
#print(int(Total_amount_to_pay))
#Balance=(Total_amount_to_pay-Number_of_USBsticks)
#print(int(Balance))

#4th method:
#Number_of_USBSticks=int(input("Enter Number_of_USBsticks:"))
#Total_amount_to_pay=(6*Number_of_USBSticks)
#print(int(Total_amount_to_pay))
#Balance=(50-Total_amount_to_pay)
#print(int(Balance))

# 5th method
Number_of_USBSticks=(50/6)
print(int(Number_of_USBSticks))
Total_amount=int(Number_of_USBSticks)
Balance=(50-Total_amount)
print(Balance)