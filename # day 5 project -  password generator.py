# day 5 project: password generator
#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters=[]
#running loop once for each letter as per input  
for i in range(0, nr_letters):
  # generating a random letter between 0 and number of nr_letters items
  random_letters_index=random.randint(0,len(letters)-1)
  # adding to "random_letters" list a random item from "letters" list
  random_letters+=letters[random_letters_index]
# print(random_letters)

random_symbols=[]
#running loop once for each symbol as per input  
for i in range(0, nr_symbols):
    
  # generating a random symbol between 0 and number of nr_symbolss items
  random_symbols_index=random.randint(0,len(symbols)-1)
  # adding to "random_symbols" list a random item from "symbols" list
  random_symbols+=symbols[random_symbols_index]


random_numbers=[]
#running loop once for each number as per input   
for i in range(0, nr_numbers):
  # generating a random number between 0 and number of nr_numbers items
  random_numbers_index=random.randint(0,len(numbers)-1)
  # adding to "random_numbers" list a random item from "numbers" list
  random_numbers+=numbers[random_numbers_index]
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password=random_letters+ random_symbols+ random_numbers

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#randomise the list
random.shuffle(password)
#convert list to string
password_to_string=""
password_to_string=password_to_string.join(password)
print(password_to_string)

