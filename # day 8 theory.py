# day 8 theory 
# functions with input
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greeting():
#   print("Hello there")
#   print("You smell like a winner")
#   print("You can do it, and I'll be the first one to congratulate you.I am also there all along the way. Jesus loves and supports you.")
# greeting()
# def greeting_with_name(name):
#   print(f"Hello there {name}")
#   print(f"You smell like a winner {name}")
#   print("You can do it, and I'll be the first one to congratulate you.I am also there all along the way. Jesus loves and supports you.")
# greeting_with_name("Roman")
# FUNCTIONS with more than 1 paramter:
# POSITIONAL PARAMETERS
# def greet_with(name, location):
#     print (f"Hello, {name}.\n What is it like in {location}?")
# greet_with("Roman", "Navoi")
# KEYWORD PARAMETERS
def greet_with(name, location):
    print (f"Hello, {name}.\n What is it like in {location}?")
greet_with(location="Navoi",  name="Roman")