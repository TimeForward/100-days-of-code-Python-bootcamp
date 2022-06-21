#day 3 exercise 4 - Pizza Order Program
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#day 3 exercise 4 - Pizza Order Program

if size=="S":
    size_sum=15
elif size=="M":
    size_sum=20
elif size=="L":
    size_sum=25
else:
    size=input('Please enter correct option: S, M or L')
    
    if size=="S":
        size_sum=15
    elif size=="M":
        size_sum=20
    elif size=="L":
        size_sum=25
if add_pepperoni=="Y":
    if size_sum==15:
        size_sum+=2
    elif size_sum==20:
        size_sum+=3
    elif size_sum==25:
        size_sum+=3


if extra_cheese=="Y":
    size_sum+=1

print(f"Your final bill is: ${size_sum}.")      