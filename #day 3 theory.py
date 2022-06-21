#conditionals
# == vs = , = vs !=
import this


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# version 1
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age=int(input("What is your age?"))
#   if age < 12:
#       print("Child tickets are $5.")
#   elif age <= 18:
#       print("Teen tickets are $7.")
#   else:
#       print("Adult tickets are $12.")
        
#   photo=input('Do you want a photo? Y or N ')
#   if photo == "Y":
#     print("Please, pay your ticket price plus $3 ")
#   else:
#     print("Please, pay your ticket price ")     
# else:
#   print("Sorry, you have to grow taller before you can ride.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("What is your age?"))
  if age < 12:
      bill=5
      print("Child tickets are $5.")
  elif age <= 18:
      bill=7
      print("Teen tickets are $7.")
  else:
      bill=12
      print("Adult tickets are $12.")
        
  photo=input('Do you want a photo? Y or N ')
  if photo == "Y":
    #changing to the bill incrementing :print(f"Please, pay ${bill+3}")
    bill+=3
      #else:
  print(f"Your final bill is ${bill} ")     
else:
  print("Sorry, you have to grow taller before you can ride.")


    
    # *******************
    # nested if /else statements
    # if condition:
    #     if another condition:
    #         do this
    #     else:
    #         do this
    # else:
    #     do this
##Theory ^ important - first make flowchart diagram with logic,
#then it is easy to turn it into code 