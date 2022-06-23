# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
# import random
# # 🚨 Don't change the code below 👇
# print("Welcome to Heads or Tails random number generator")
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#  # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
# #Write the rest of your code below this line 👇

# toss=random.randint(0,1)
# if toss==1:
#     print("Heads")
# else:
#     print("Tails")
# lists
# states=["Delaware", "Pennsylvania","New Jersey"]
# #index notation
# print(states[0])
# print(states[-1])
# #ammending lists:
# states[1]="Pencilvania"
# #appending list at the end
# states.append("Romanland")
# states.extend(["Nomansland","Someonesland"])
# print(states)

#******** NESTED LISTS
fruits=["Strawberries","Nectarines"
,"Apples",
"Grapes"
,"Peaches",
"Cherries"
,"Pears",
"Tomatoes"
]
vegetables=["Celery",
"Potatoes","Spinach"
,"Kale"
]
dirty_dozen=[fruits, vegetables]
print(dirty_dozen)
