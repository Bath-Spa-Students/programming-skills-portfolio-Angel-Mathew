#Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#•If the person is less than 2 years old, print a message that the person is a baby.
#•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#•If the person is age 65 or older, print a message that the person is an elder.
years_old=int(input("Enter the years_old:"))
if years_old<2:
    print("person is a baby")
if years_old<4:
    print("person is a toddler")
elif years_old<13:
    print("person is a kid")
elif years_old<20:
    print("person is a teenager")
if years_old<65:
    print("person is a adult")
if years_old ==65:
    print("person is elder")
else:
    print("person is a elder")