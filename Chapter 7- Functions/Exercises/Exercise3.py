## Exercise 3: T-Shirt  :ballot_box_with_check:
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size,text):
    print("you have ordered a_"+size+" shirt that says "+text)
make_shirt("large","medium")
make_shirt(size="medium",text="smile smileyyy..")
