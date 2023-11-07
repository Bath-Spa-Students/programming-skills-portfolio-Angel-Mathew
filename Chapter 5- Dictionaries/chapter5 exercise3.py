#Exercise 3: Glossary 2 :ballot_box_with_check:
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
glossary={"string":"a collection of alphabets,words,other characters",
          "boolean":"it determines the value is true or false",
          "dictionary":"A dictionary are collection of key value pairs",
          "if":"if statement evaluates condition",
          "elif":"used to test multiple condition",
          "else":"used to execute both the true part and the false part of a given condition"}
for word,meaning in glossary.items():
    print("\n"+word.title()+":"+meaning)
glossary={"string":"a collection of alphabets,words,other characters",
          "boolean":"it determines the value is true or false",
          "dictionary":"A dictionary are collection of key value pairs",
          "if":"if statement evaluates condition","elif":"used to test multiple condition",
          "else":"used to execute both the true part and the false part of a given condition",
          "range":"returns a sequence of numbers,starting from 0 by default and increments by 1 and stops before a specified number",
          "for_loop":"used for ilerating over a sequence","while":"allows code to be executed repeatedly,whether a condition is satisfied or not",
          "break":"allows to exit the nearest enclosing while or for loop",
          "append()":"takes an argument and adds it to the end of an existing list"}
for word,meaning in glossary.items():
    print("\n"+word.title()+":"+meaning)

