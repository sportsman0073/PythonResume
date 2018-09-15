# CS 177 - lab6.py
# Nicholas Koontz, HeeJoon Rnoh, Sarah Hermanek
# This program sti,ulates Plinko in a 500x500 graphics window it will start when click is detected in the window

from graphics import *
import random
from time import sleep
#Make the blue ball
def bball(win):
    x = random.randint(75,425)
    ball = Circle(Point(x,25),25)
    ball.setFill('blue')
    ball.draw(win)
    return ball
#Distance formula
def dist(x,y):
    h = x.getCenter().getY()
    j = x.getCenter().getX()
    c = y.getCenter().getX()
    d = y.getCenter().getY()
    z = (((c-j)**2)+((d-h)**2))**.5
    return z

#Main function
def main():
    win = GraphWin('Plinko', 500,500)
    #Text
    Hello = Text(Point(250,250), 'Click to Play Plinko!')
    Hello.draw(win)
    #Bumper list
    bumplist = []
    #Draw 8 bumpers
    bump = Circle(Point(100,200),5)
    bump.setFill('red')
    bump.draw(win)
    bumplist.append(bump)
    
    bump2 = Circle(Point(250,200),5)
    bump2.setFill('red')
    bump2.draw(win)
    bumplist.append(bump2)
    
    bump3 = Circle(Point(400,200),5)
    bump3.setFill('red')
    bump3.draw(win)
    bumplist.append(bump3)
    
    bump4 = Circle(Point(175,300),5)
    bump4.setFill('red')
    bump4.draw(win)
    bumplist.append(bump4)
    
    bump5 = Circle(Point(325,300),5)
    bump5.setFill('red')
    bump5.draw(win)
    bumplist.append(bump5)
    
    bump6 = Circle(Point(100,400),5)
    bump6.setFill('red')
    bump6.draw(win)
    bumplist.append(bump6)
    
    bump7 = Circle(Point(250,400),5)
    bump7.setFill('red')
    bump7.draw(win)
    bumplist.append(bump7)
    
    bump8 = Circle(Point(400,400),5)
    bump8.setFill('red')
    bump8.draw(win)
    bumplist.append(bump8)
    #Run game 5 times
    for rerun in range(5):
        win.getMouse()
        Hello.setText('')
        b = bball(win)
        l = b.getCenter().getX()
        p = b.getCenter().getY()
        #Runs until ball at the bottom of the screen
        for k in range(501):
            for i in bumplist:
                d = dist(b,i)
                dy = 0
                dx = 0
                #If at that location stop movement
                if b.getCenter().getY() < 475:
                    n = 25 + dy
                    dy = (n*25)//100
                    b.move(dx,dy)
                    sleep(.05)
                if b.getCenter().getX() > 25 and b.getCenter().getX() < 475:
                    if d <= 30:
                        if b.getCenter().getX() > i.getCenter().getX():
                            n = 75 + dx
                            dx = (n*25)//100
                            b.move(dx,dy)
                            sleep(.01)
                        elif b.getCenter().getX() < i.getCenter().getX():
                            n = 75 + dx
                            dx = ((-1*n)*25)//100
                            b.move(dx,dy)
                            sleep(.01)
                        else:
                            n = 0
                            dx = (n*25)//100
                            b.move(dx,dy)
                    else:
                        n = 0
                        dy = (n*25)//100
                        b.move(dx,dy)
#Stop game      
            if k == 500:
                Hello = Text(Point(250,250), 'Click to Play Plinko again!')
                Hello.draw(win)
#Undraw and end program
        b.undraw()
    Hello.undraw()
    bye = Text(Point(250,250), 'Game over - Click to Close')
    bye.draw(win)
    mousekey = win.getMouse()
    while mousekey == None:
        mousekey = win.getMouse()
    if mousekey != None:
#Close window
        win.close()
#End Main Function
main()
