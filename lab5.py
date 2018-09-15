###CS - 177
###Sarah Hermanek, Nicholas Koontz, HeeJoon Rnoh
###lab5.py
##
###This program completes a demographic survey of some students, including a count of the number of students
###in each demographic region, and a horizontal bar graph depicting this distribution
##
##print("This program completes a demographic survey of some students, including a count of the number of students in each demographic region, and a horizontal bar graph depicting this distribution")
##
##
##print("Type what file you would like to open:", end = ' ')
##file = str(input())
##f= open(file,'r')
##h = open("output.txt",'w')
##IN=0
##OH=0
##TX=0
##NY=0
###close the file
##
##
###accumulate the count of students belonging to each demographic region
##for i in f.readlines():
##    k = i.split(",")
##    if k[2] =='0':
##        IN= IN+1
##    elif k[2]=='1':
##        OH=OH+1
##    elif k[2]=='2':
##        TX=TX+1
##    elif k[2]=='3':
##        NY=NY+1
##h.write('Region' + '\t' + 'Number of Students' + '\n' + 'IN' + '\t' + str(IN) +'\n' 'OH' + '\t' + str(OH) +'\n' + 'TX' + '\t' + str(TX) + '\n' + 'NY' + '\t' + str(NY) + '\n')
##print("IN", IN)
##print("OH", OH)
##print("TX", TX)
##print("NY", NY)
###close files
##h.close()
##f.close()
##y = IN + OH + TX + NY
##INP = IN/y
##OHP = OH/y
##TXP = TX/y
##NYP = NY/y
####Part 2

from graphics import *

def main():
    Demo = GraphWin("Demographic Plot",360,360)
    #Draw lines
    aLine = Line(Point(50,310), Point(50, 60))
    bLine = Line(Point(50, 310), Point(310, 310))
    aLine.setArrow("last")
    bLine.setArrow("last")
    aLine.draw(Demo)
    bLine.draw(Demo)
    #Draw Bar Graph
    aRect= Rectangle(Point(50, 280), Point(50+(260*INP),250))
    aRect.setFill('red')
    aRect.draw(Demo)
    Line1 = Line(Point(50, 265), Point(40,265))
    Line1.draw(Demo)
    bRect= Rectangle(Point(50, 230), Point(50+(260*OHP), 200))
    bRect.setFill('green')
    bRect.draw(Demo)
    Line2 = Line(Point(50,215), Point(40,215))
    Line2.draw(Demo)
    cRect = Rectangle(Point(50, 180), Point(50+(260*TXP), 150))
    cRect.setFill('blue')
    cRect.draw(Demo)
    Line3 = Line(Point(50,165), Point(40,165))
    Line3.draw(Demo)
    dRect = Rectangle(Point(50, 130), Point(50+(260*NYP), 100))
    dRect.setFill('yellow')
    dRect.draw(Demo)
    Line4 = Line(Point(50, 115), Point(40,115))
    Line4.draw(Demo)
    #Legend for Graph
    INRECT = Rectangle(Point(310,20), Point(320,30))
    INRECT.setFill('red')
    INRECT.draw(Demo)
    INTEXT = Text(Point(290,25), 'IN')
    INTEXT.draw(Demo)
    
    OHRECT = Rectangle(Point(310,50), Point(320,60))
    OHRECT.setFill('green')
    OHRECT.draw(Demo)
    OHTEXT = Text(Point(290,55), 'OH')
    OHTEXT.draw(Demo)

    TXRECT = Rectangle(Point(310,80), Point(320,90))
    TXRECT.setFill('blue')
    TXRECT.draw(Demo)
    TXTEXT = Text(Point(290,85), 'TX')
    TXTEXT.draw(Demo)

    TXRECT = Rectangle(Point(310,110), Point(320,120))
    TXRECT.setFill('yellow')
    TXRECT.draw(Demo)
    TXTEXT = Text(Point(290,115), 'NY')
    TXTEXT.draw(Demo)
    #Text for Graph
    zero = Text(Point(50, 320),'0')
    zero.draw(Demo)
    Region = Text(Point(50,40), 'Demo. region')
    Region.draw(Demo)
    percent = Text(Point(310, 340), '% of students')
    percent.draw(Demo)
    hund = Text(Point(300,320), '100')
    hund.draw(Demo)
    
    ten = Text(Point(75,320), '10')
    ten.draw(Demo)
    tenline = Line(Point(75,310), Point(75,315))
    tenline.draw(Demo)
    
    two = Text(Point(100,320), '20')
    two.draw(Demo)
    tline = Line(Point(100,310), Point(100,315))
    tline.draw(Demo)
    
    three = Text(Point(125,320), '30')
    three.draw(Demo)
    threeline = Line(Point(125,310), Point(125,315))
    threeline.draw(Demo)
    
    four = Text(Point(150,320), '40')
    four.draw(Demo)
    fourline = Line(Point(150,310), Point(150,315))
    fourline.draw(Demo)
    
    five = Text(Point(175,320), '50')
    five.draw(Demo)
    fline = Line(Point(175,310), Point(175,315))
    fline.draw(Demo)
    
    six = Text(Point(200,320), '60')
    six.draw(Demo)
    sixline = Line(Point(200,310), Point(200,315))
    sixline.draw(Demo)
    
    seven = Text(Point(225,320), '70')
    seven.draw(Demo)
    sline = Line(Point(225,310), Point(225,315))
    sline.draw(Demo)
    
    eight = Text(Point(250,320), '80')
    eight.draw(Demo)
    eline = Line(Point(250,310), Point(250,315))
    eline.draw(Demo)
    
    nine = Text(Point(275,320), '90')
    nine.draw(Demo)
    nline = Line(Point(275,310), Point(275,315))
    nline.draw(Demo)
    #Get mouse
    mouseKey = Demo.getMouse()
    while mouseKey == None:
        mouseKey = Demo.getMouse()
    if mouseKey != None :
        Demo.close()
main()

    
    
