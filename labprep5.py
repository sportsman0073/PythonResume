from graphics import *
from msvcrt import getch
#CS 177 – labprep5.py
# Nicholas Koontz
# This is a demonstration of basic Graphics module functions
# Full documentation of the Graphics module can be found in
# the Zelle Python textbook Ch 4 (2nd and 3rd editions) and at:
# http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
#
# This program creates a Graphics window and draws several shapes
# and interactive elements, then waits for a mouse click in
# the Graphics window before changing the properties of the
# shapes. After 5 clicks it prompts the user for one more
# then closes the Graphics window.

def main():
    circColor = 'red'
    rectColor = 'green'
    triColor = 'blue'

    field = GraphWin("Window",300,400)
    
    #Generate the text field under each color
    label = Entry(Point(50,375), 10)
    label.draw(field)
    label2 = Entry(Point(150,375), 10)
    label2.draw(field)
    label3 = Entry(Point(250,375), 10)
    label3.draw(field)
    for i in range(6):
        
        #Generates the shapes in the field
        circle = Circle(Point(120,150),30)
        circle.setFill(circColor)
        circle.draw(field)
        rect = Rectangle(Point(200,200), Point(240,260))
        rect.setFill(rectColor)
        rect.draw(field)
        tri = Polygon(Point(120,20),Point(180,60),Point(60,60))
        tri.setFill(triColor)
        tri.draw(field)

        exText = Text(Point(150, 300), "Enter new shape color(s) and click anywhere")
        done = Text(Point(150, 320),"All done! Click to exit...")
        exText.draw(field)
        if(i == 5):
            done.draw(field);
        #Generates the text field colors and names
        cirText = Text(Point(50,340),"Circle")
        cirText.draw(field)
        x = Rectangle(Point(0,400), Point(100,350))
        x.setFill(circColor)
        x.draw(field)
        rectText = Text(Point(150,340),"Rectangle")
        rectText.draw(field)
        y = Rectangle(Point(100,400), Point(200,350))
        y.setFill(rectColor)
        y.draw(field)
        triText = Text(Point(250,340),"Triangle")
        triText.draw(field)
        z = Rectangle(Point(200,400), Point(300,350))
        z.setFill(triColor)
        z.draw(field)
        mouseKey = field.getMouse()
        
        #key = field.getKey()
        while mouseKey == None:
            mouseKey = field.getMouse()
        if mouseKey != None :
            if(label.getText() != ""):
                circColor = label.getText()
                label.setText("")
            if(label2.getText() != ""):
                rectColor = label2.getText()
                label2.setText("")
            if(label3.getText() != ""):
                triColor = label3.getText()
                label3.setText("")
#PYTHON WORKS WITH SO MANY COLORS!!!! :)
           
    field.close()
main()
