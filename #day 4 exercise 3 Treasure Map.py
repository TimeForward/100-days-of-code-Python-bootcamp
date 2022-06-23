#day 4 exercise 3 Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# did I use the list at all?
converted_position=list(position) 


a=int(position[0])-1
b=int(position[1])-1
# c=a
# a=b
# b=c
map[b][a]="X"
print((f"{row1}\n{row2}\n{row3}"))