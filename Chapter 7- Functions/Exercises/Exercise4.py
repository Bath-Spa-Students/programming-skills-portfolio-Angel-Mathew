#Exercise 4:  Large Shirts :ballot_box_with_check:
#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size="large",text="I love Python"):
      print("you have ordered a_"+size+" shirt that says "+text)
make_shirt("medium")
make_shirt()
make_shirt(size="medium",text="Land of vibgyor")
