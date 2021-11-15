#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

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
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
	apple.penup()
	apple.right(90)
	apple.forward(200)
	apple.left(90)

def draw_an_A():
	drawer.color("white")
	drawer.write("A", font=("Arial", 50, "bold"))
	drawer.hideturtle()
#-----function calls-----
draw_an_A()
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()

wn.mainloop()