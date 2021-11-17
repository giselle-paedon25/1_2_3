#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

letter = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()
drawer.penup()
drawer.goto(-10,100)
drawer.pendown()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
apple.shape("apple.gif")
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 
def new_par(apple):
	new_ypos = rand.randint(-200,200)
	new_xpos = rand.randint(-200,200)
	apple.penup()
	apple.goto(new_xpos,new_ypos)
	apple.pendown()
#TODO Create a function that draws a new letter from the letter list.
def new_letter():
	rand.choice(letter)
	apple.write("Arial", 50, "bold")
#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def new_shape(apple):
	apple.shape("apple.gif")
	new_letter()
	wn.update()
#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
'''for i in range(0, number_of_apples):
  #Your code here
'''
#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter 
# to disappear. Call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
	apple.penup()
	apple.right(90)
	apple.forward(200)
	apple.left(90)
	drawer.hideturtle()
	drawer.clear()
	apple.hideturtle()
	apple.clear()

def draw_an_A():
	drawer.color("white")
	drawer.write("A", font=("Arial", 50, "bold"))
#-----function calls-----
draw_an_A()
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()

wn.mainloop()