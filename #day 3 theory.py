#conditionals
# == vs = , = vs !=
import this


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("What is your age?"))
  if age < 12:
      print("Child tickets are $5.")
  elif age <= 18:
      print("Teen tickets are $7.")
  else:
      print("Adult tickets are $12.")  
    photo=input('Do you want a photo?')
    if photo == "Yes".lower:
        print("Please, pay your ticket price plus $3 ")
    else:
        print(f"Please, pay your ticket price ")
        
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

