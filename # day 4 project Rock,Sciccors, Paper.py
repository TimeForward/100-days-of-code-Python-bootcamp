rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
user_choice=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
computer_choice=random.randomint(0,2)

print(f"Computer chose")
if user_choice==computer_choice:
  print("It's a draw")