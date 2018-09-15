# CS 177 - labprep6.py
# Nicholas Koontz
# Cicrles of various size and colors fall from the top of the screen to the bottom of the screen stopping at the bottom of the screen

from graphics import *
import random
from time import sleep

color = ['red','green','blue','purple','yellow','black','white','teal','skyblue','forestgreen','pink','orange','brown','grey']
#Create create function
def create(demo):
    radius = random.randint(10,20)
    x = random.randint(20,480)
    bubble = Circle(Point(x, radius),radius)
    bubble.setFill(random.choice(color))
    bubble.draw(demo)
    return bubble, radius

#Create fall function
def fall(x):
    dy = 0
    g = x[0].getCenter().getY()
    v = x[1]
    if g < 500 - v:
        n = v + dy
        dy = (n*v)//100
        x[0].move(0,dy)
        return x
    else:
        n = 0
        dy = (n*v)//100
        x[0].move(0,dy)
        return x
#Function
def main():
    demo = GraphWin("Bubbles",500,500)
    #Text
    Hello = Text(Point(250,250), 'Click to Run Program')
    Hello.draw(demo)
    #Start Program
    mousekey = demo.getMouse()
    while mousekey == None:
        mousekey = demo.getMouse()
    if mousekey != None:
        #Get rid of text
        Hello.setText("")
        #Draw 4 objects
        a = create(demo)
        b = create(demo)
        c = create(demo)
        d = create(demo)
        #Loop until all balls are on the bottom of the screen
        for k in range(501):
            fall(a)
            fall(b)
            fall(c)
            fall(d)
            sleep(.05)
            if k == 500:
    #Wait till all bubbles make it to the bottom of the screen
                bye = Text(Point(250,250), 'Click to Close Program')
                bye.draw(demo)
                mousekey = demo.getMouse()
                while mousekey == None:
                    mousekey = win.getMouse()
                if mousekey != None:
    #close program
                    demo.close()
#Close main function       
main()
