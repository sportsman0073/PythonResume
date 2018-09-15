from graphics import *
win = GraphWin('Win',300,300)
p = Point(50,50)
c = Circle(p, 10)
c.draw(win)
c.setFill('blue')

for x in range(10,15):
    for color in ['red','blue','green']:
        c.move(x,x+2)
        c.setFill(color)
        middle = c.getCenter()
        win.getMouse()
win.close()
