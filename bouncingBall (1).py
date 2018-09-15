from graphics import *
from time import sleep

def bounce(ball,dx,dy):         # Function 'bounces' ball off wall
    center=ball.getCenter()     # get center of ball
    if center.getX() not in range(8,293):   # within window?
        dx *= -1                            # change direction
    if center.getY() not in range(8,293):
        dy *= -1
    return dx,dy                            # return new values

def main():
    win = GraphWin("Win",300,300)           # make window
    ball = Circle(Point(150,150),5)         # make ball
    ball.setFill('blue')
    ball.draw(win)
    dx,dy = 3,-5                            # initial direction
    while not win.checkMouse():             # repeat until mouse click
        ball.move(dx,dy)                    # move ball
        sleep(0.02)                         # sleep 0.02 seconds
        dx,dy = bounce(ball,dx,dy)          # call function to check
    txt = Text(Point(150,150),"All done")   # end - show message
    txt.draw(win)
    win.getMouse()
    win.close()                             # close windows

main()
