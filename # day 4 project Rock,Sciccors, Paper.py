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
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
computer_choice=random.randint(0,2)
user_choice_converted=None
computer_choice_converted=None

if computer_choice==0:
    computer_choice_converted="Rock"
    print(rock)
elif computer_choice==1:
    computer_choice_converted="Paper"
    print(paper)
else:
    computer_choice_converted="Scissors"
    print(scissors)
print(f"Computer chose {computer_choice_converted}")     

if user_choice==0:
    user_choice_converted="Rock"
    print(rock)
elif user_choice==1:
    user_choice_converted="Paper"
    print(paper)
elif user_choice==2:
    user_choice_converted="Scissors"
    print(scissors)

#


if user_choice==0 and computer_choice==1:
    print("Computer wins")  
elif user_choice==0 and computer_choice==2:   
    print("User wins")
elif user_choice==1 and computer_choice==0:   
    print("Computer wins")
elif user_choice==1 and computer_choice==2:   
    print("Computer wins")
elif user_choice==2 and computer_choice==0:   
    print("Computer wins")
elif user_choice==2 and computer_choice==1:   
    print("User wins")
elif user_choice>=3 or user_choice<0:
    print(f"User chose an invalid number {user_choice}, user loses")
else:
    print("It's a draw")

   