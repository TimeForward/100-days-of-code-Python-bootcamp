#day 4 exercise 2 - bam=nker's roulette
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total=len(names)
#adjust for zero-based index
total-=1
#generate a random number in the same range as there are number of list items, zero-based index-wise
random=random.randint(0 ,total)
print(f"{names[random]} is going to buy the meal today!")

#alternative ,easy solution:
# random=random.choice(names)
#print(f"{random} is going to buy the meal today!")
