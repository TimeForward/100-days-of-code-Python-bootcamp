#day 2 project -tip calculator -to run the code - https://replit.com/@nothuuu/tip-calculator-start?embed=|&output=|#main.py
# #If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total=input("What was the total bill?")
tip=input("What percentage tip would you like to give? 10, 12, or 15?")
split_by=int(input("How many people to split this bill to?"))
amount = float(total)*(1+(int(tip)/100))
amount_each =amount/split_by
<<<<<<< HEAD
print(f"Each person should pay ${round(amount_each,2)}")
=======
print(f"Each person should pay {round(amount_each,3)}")
>>>>>>> 76a558f9defb1f5335975fc7a286bbb4dc142a4b
