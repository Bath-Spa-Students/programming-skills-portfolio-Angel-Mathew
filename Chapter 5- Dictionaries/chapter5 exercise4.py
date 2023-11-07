# Exercise 4: Rivers :ballot_box_with_check:
#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#* Use a loop to print the name of each river included in the dictionary.
#* Use a loop to print the name of each country included in the dictionary.
rivers={"Amazon River":"_Brazil",
        "Nile River":"_Egypt",
        "Indus Rivers ":"_India"}
for River,countries in rivers.items():
    print("The"+River+"flow through"+countries+".")
for River in rivers.keys():
    print("\n rivers:")    
    print(rivers)
for countries in rivers.values():    
    print("\n countries:")
    print(countries)
    