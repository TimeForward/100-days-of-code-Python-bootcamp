# day 2-3 Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.
# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆
total = 90
left_y = total-age
left_w = left_y*52
left_m = left_y*12
left_d = left_y*365

print(f"You have {left_d} days, {left_w} weeks, and {left_m} months left.")

#Write your code below this line 👇