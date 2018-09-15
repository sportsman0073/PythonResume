# Bubbles.py
# This program displays 8 bubbles on the screen and waits
#    for the user to click the mouse.  If a click is detected
#    on one of the bubbles, it moves across the screen.
#    After 10 total clicks the program terminates.
from graphics import *
from random import randint, choice
from time import sleep

# Create a 400x400 graphics window named 'win'
win = GraphWin("Pretty Bubbles!",400,400)

# The make function creates n bubbles using a random
#     selection of colors. Each bubble has a random
#     radius of 15 - 25 pixels and is appended to the
#     list named 'bubbles'.  The completed list has the
#     structure:   [ [Circle, dx, dy], [Circle, dx, dy]... ]
#     The values dx and dy are set to 0 by default indicating
#     that the bubble will not move initially.
def make(n):
    bubbles = []
    colors = ['red','blue','green','pink','yellow','cyan']

    for i in range(n):
        center = Point(randint(50,350),randint(50,350))
        radius = randint(15,25)
        newbubble = Circle(center,radius)
        newbubble.setFill(choice(colors))
        bubbles.append([newbubble,0,0])
    return bubbles

# The draw function increments through the list of bubbles
#    one at a time and draws them on the Graphics window
def draw(bubbles):
    for bubble in bubbles:
        bubble[0].draw(win)

# The distance function accepts 2 points then returns
#    algorithm to determine their distance in pixels.
def distance(p1, p2):
    x1, y1 = p1.getX(), p1.getY()
    x2, y2 = p2.getX(), p2.getY()
    return ((x1-x2)**2+(y1-y2)**2)**.5

# The walls function accepts a single 'bubble' entry
#    in the format [ circle, dx, dy ] and checks to see
#    if the next movement of the circle will take it outside
#    the 400x400 graphics window.  If so, it multiplies
#    the dx or dy value by -1 to change the direction of movement
def walls(bubble):
    center = bubble[0].getCenter()
    radius = bubble[0].getRadius()
    x,y = center.getX(), center.getY()
    if x + bubble[1] < radius or x + bubble[1] > 400-radius:
        bubble[1] *= -1
    if y + bubble[2] < radius or y + bubble[2] > 400-radius:
        bubble[2] *= -1
    return bubble

# The move function accepts a list of bubbles (circles) then
#     looks at each individual element to move it across the
#     graphics window.  After moving it, the dx and dy variables
#     are decreased by 10% so the movement slows back to 0
def move(bubbles):
    for bubble in bubbles:
        walls(bubble)
        bubble[0].move(bubble[1],bubble[2])
        bubble[1] *= .9
        bubble[2] *= .9

# The check function determines if a mouse click is within
#    the radius of any of the bubbles.  If so, it randomly
#    assigns a movement dx and dy value from a short list
#    This dx and dx value is stored in index [1] and [2]
#    for that bubble in the list of bubbles
def check(click, bubbles):
    for bubble in bubbles:
        if distance(click,bubble[0].getCenter()) < bubble[0].getRadius():
            speeds = [-10,-8,-6,-4,4,6,8,10]
            bubble[1], bubble[2] = choice(speeds),choice(speeds)

# This is the main control loop for Bubbles.
#    After 10 clicks on the graphics window, it
#    displays a message, waits for one more click
#    then closes the window and exits the program
def main():
    message = Text(Point(200,40),"Click on a bubble to push it!")
    message.draw(win)
    bubbles = make(8)
    draw(bubbles)
    clicks = 0
    while clicks < 10:
        click = win.checkMouse()
        if click:
            clicks += 1
            check(click, bubbles)
        move(bubbles)
        sleep(0.0025)              # uncomment if program runs too fast
    message.undraw()
    message = Text(Point(200,200),"10 Clicks is enough \n Click in Window to End")
    message.draw(win)
    win.getMouse()
    win.close()

main()
