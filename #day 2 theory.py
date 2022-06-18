# #day 2
# # data types
# #String
# #subtsring with index
# # prints H
# print("Hello"[0])
# # prints O
# print("Hello"[4])
# #concatenation
# print("123"+"345")
# #Integer
# #print sum
# print(123 + 345)
# #Python ignores underscores -they are for ease of visual pereceiving 
# 123_456_789
# #float
# 3.14159
# #Boolean
# True
# False

# results in error : str + int
#num_char = len(input("What is your name?"))
#print("Your name has " + num_char + "characters")
# <class 'int'>
# print(type(num_char))
# # <class 'int'>
# #type conversion/casting
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")
# Mathematical operations
#6/3 = 2.0 : float
# PEMDASLR
# rounding number swith "round(number, precision_degree)" with a given precision :
# print(round(8/3,2)) : 2.67
print(round(2.666666666,2)) #: 2.67
# FLOOR DIVISION: WHOLE NUMBERS RESULT ONLY-CHPPING OFF THE DIGITS AFTER DECIMAL POINT
print(8//3) #2
# F-Strings:
score = 0
height =1.8
isWinning = True
print(f"your scorу is {score}, your height is {height}, you are winning is {isWinning}")