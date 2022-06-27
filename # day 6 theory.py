# day 6 theory
# functions:
# DEFINING a function:
def my_function():
    #do this
    #then do that
# CALLING a function
# my_function()
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#     def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def left_square():    
#     move()
#     turn_left()
#     move()
#     turn_left()
    
#     move()
#     turn_left()
#     move()
#     turn_left()
# def left_circle():    
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     jump()
 # hurdle 3 - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
 # solution   
  def jump():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
#The functions move() and turn_left().
#The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#How to use a while loop and an if statement.
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()   