# day 5 exercise 3. count sum of evens in a range
# #Write your code below this row 👇
evens=0
for i in range(1 , 101):
    if i%2==0:
        evens+=i
print(evens)
