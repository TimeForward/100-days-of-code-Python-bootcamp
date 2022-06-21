# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower=name1.lower()
name2_lower=name2.lower()

t=name1_lower.count("t")
t+=name2_lower.count("t")
r=name1_lower.count("r")
r+=name2_lower.count("r")
u=name1_lower.count("u")
u+=name2_lower.count("u")
e=name1_lower.count("e")
e+=name2_lower.count("e")

l=name1_lower.count("l")
l+=name2_lower.count("l")
o=name1_lower.count("o")
o+=name2_lower.count("o")
v=name1_lower.count("v")
v+=name2_lower.count("v")
e=name1_lower.count("e")
e+=name2_lower.count("e")

# print(f"T occurs {t} times")
# print(f"R occurs {r} times")
# print(f"U occurs {u} times")
# print(f"E occurs {e} times")
total1=t+r+u+e

# print(f"Total = {total1}")

# print(f"L occurs {l} times")
# print(f"O occurs {o} times")
# print(f"V occurs {v} times")
# print(f"E occurs {e} times")
total2=l+o+v+e

# print(f"Total = {total2}")
score=str(total1)+str(total2)
score=int(score)

if (score <=10) or (score >=90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


