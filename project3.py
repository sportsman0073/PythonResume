#CS - 177 project3.py
#Nicholas Koontz, Racheal HeeJoon Rnoh, Sarah Hermanek
# Skeet Shooting game improvements
import math
from graphics import *
from time import sleep
import random

names = []
hscore = []
rounds_played = []
store = []
start = 0

#Descibes in a new window who the work in this project
#Waits for a users click on the window before it closes the window
def credit():
    win = GraphWin('Credits', 300,200)
    bye = Text(Point(150,20), 'Thank You For Playing')
    bye.draw(win)
    created = Text(Point(150,60), 'Created By: Nicholas Koontz')
    created.draw(win)
    designed = Text(Point(150,100), 'Designed By: Nicholas Koontz')
    designed.draw(win)
    creative = Text(Point(150,140), 'Creative Ideas: Racheal and Sarah')
    creative.draw(win)
    close = Text(Point(150,180), 'Click to close window')
    mouseclick = win.getMouse()
    while mouseclick == None:
        mouseclick = win.getMouse()
    if mouseclick != None:
        win.close()


def sort_score(player_name, score, rounds):
    file = open('top_scores.txt','w')
    r = str(rounds)
    s = str(score)
    names.append(player_name)
    hscore.append(s)
    rounds_played.append(r)
    limit = 0
    if len(hscore) >= 10:
        limit = 10
    else:
        limit = len(hscore)
    
    for i in range(limit):
        for j in range(i+1, limit):
            
            if names[i] == names[j]:
                hscore[i] =  float(hscore[i]) + float(hscore[j])
                rounds_played[i] = int(rounds_played[i]) + int(rounds_played[j])
                hscore[i] = str(hscore[i])
                rounds_played[i] = str(rounds_played[i])
                names.remove(names[j])
                hscore.remove(hscore[j])
                rounds_played.remove(rounds_played[j])
                if len(hscore) < 10:
                    limit = len(hscore)
                
            elif hscore[j] > hscore[i]:
                stmp = hscore[i]
                hscore[i] = hscore[j]
                hscore[j] = stmp
                ntmp = names[j]
                names[j] = names[i]
                names[i] = ntmp
                rtemp = rounds_played[j]
                rounds_played[i] = rounds_played[j]
                rounds_played[j] = rtemp
                    
    file.seek(0)
    file.truncate()
    file.write('\n')
    file.write('\n')
    for i in range(limit):
        file.write(str(i+1)+".   "+names[i]+'\t'+hscore[i]+'\t'+rounds_played[i]+'\n')
    file.close()

def pull_s(win,x,y):
    pull_bs = Rectangle(Point(80,290),Point(190,330))
    pull_bs.setFill('yellow')
    pull_bs.draw(win)
    pull_text_s = Text(Point(135, 310), "PULL SINGLE")
    pull_text_s.draw(win)
    sleep(.1)
    pull_bs.setFill('pink')
    
def pull_d(win,x,y):
    pull_bd = Rectangle(Point(205,290),Point(320,330))
    pull_bd.setFill('yellow')
    pull_bd.draw(win)
    pull_text_d = Text(Point(263, 310), "PULL DOUBLE")
    pull_text_d.draw(win)
    sleep(.1)
    pull_bd.setFill('pink')
        
def game_s(demo,n,p,g, custom):
    r_or_p = random.randint(1,2)
    s = 0
    r = random.randint(350,450)
    l = random.randint(350,450)
    
    if r_or_p == 2:
        targetright = Circle(Point(0,r),8)
        targetright.setFill(custom[2])
        targetright.draw(demo)
        targetleft = Circle(Point(600,l),8)
        sleep(2)
        r_y = targetright.getCenter().getY()
        r_x = targetright.getCenter().getX()
        l_y = targetleft.getCenter().getY()
        l_x = targetleft.getCenter().getX()
        dxr = -(p * math.cos(math.degrees(n)))
        dyr = (p * -math.sin(math.degrees(n)))
        targetright.move(dxr,dyr)
        count = 0
        
        while r_y <= 450:
            count += 1
            mousekey = demo.checkMouse()
            dxr = -(p * math.cos(math.degrees(n)))
            dyr = ((p * -math.sin(math.degrees(n)))+g*count)
            dxl = (p * math.cos(math.degrees(n)))
            dyl = ((p * -math.sin(math.degrees(n)))+g*count)
            r_y = targetright.getCenter().getY()
            r_x = targetright.getCenter().getX()
            targetright.move(dxr,dyr)
            sleep(.1)
            if r_x <= 0 or r_y >= 450:
                targetright.undraw()
                dyr = 0
                dxr = 0
                targetleft.setFill(custom[2])
                targetleft.draw(demo)
                dyl = (p * -math.sin(math.degrees(n)))
                dxl = (p * math.cos(math.degrees(n)))
                targetleft.move(dxl,dyl)
                sleep(.2)
                count = 0
                while l_y <= 450 or l_x >= 600:
                    count += 1
                    l_x = targetleft.getCenter().getX()
                    l_y = targetleft.getCenter().getY()
                    dxl = (p * math.cos(math.degrees(n)))
                    dyl = ((p * -math.sin(math.degrees(n)))+g*count)
                    targetleft.move(dxl,dyl)
                    mousekey = demo.checkMouse()
                    sleep(.1)
                    if l_x >= 600 or l_y >= 450:
                        targetleft.undraw()
                        dyl = 0
                        dxl = 0
                    if mousekey != None:
                        x = mousekey.getX()
                        y = mousekey.getY()
                        click_x_r = abs(x - r_x)
                        click_x_l = abs(x - l_x)
                        click_y_r = abs(y - r_y)
                        click_y_l = abs(y - l_y)
                        if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                            missed = Text(Point(300,100),'MISSED')
                            missed.draw(demo)
                            sleep(.1)
                            missed.undraw()
                        if click_x_l <= 4 and click_y_l <= 4:
                            targetleft.undraw()
                            s += .5
                            dyl = 0
                            dxl = 0
                            #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                            #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                            right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                            right_triangle.setFill(custom[2])
                            right_triangle.draw(demo)

                            left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                            left_triangle.setFill(custom[2])
                            left_triangle.draw(demo)

                            center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                            center_triangle.setFill(custom[2])
                            center_triangle.draw(demo)
                            sleep(.2)
                            #Undraws the triangles so it looks like they fell to the ground 
                            center_triangle.undraw()
                            left_triangle.undraw()
                            right_triangle.undraw()
                    if dxr == 0 and dxl == 0:
                        demo.close()
                        break

            if dxr == 0 and dxl == 0:
                demo.close()
                break
            if mousekey != None:
                x = mousekey.getX()
                y = mousekey.getY()
                click_x_r = abs(x - r_x)
                click_x_l = abs(x - l_x)
                click_y_r = abs(y - r_y)
                click_y_l = abs(y - l_y)
                #Puts the word MISSED on the screen if the click is not on either target 
                if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.draw(demo)
                    sleep(.1)
                    missed.undraw()
                if click_x_r <= 4 and click_y_r <= 4:
                    targetright.undraw()
                    dyr = 0
                    dxr = 0
                    s += .5
                    #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                    #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                    right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                    right_triangle.setFill(custom[2])
                    right_triangle.draw(demo)

                    left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                    left_triangle.setFill(custom[2])
                    left_triangle.draw(demo)

                    center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                    center_triangle.setFill(custom[2])
                    center_triangle.draw(demo)
                    sleep(.2)
                    #Undraws the triangles so it looks like they fell to the ground 
                    center_triangle.undraw()
                    left_triangle.undraw()
                    right_triangle.undraw()
                    
                    targetleft.setFill(custom[2])
                    targetleft.draw(demo)
                    dyl = (p * -math.sin(math.degrees(n)))
                    dxl = (p * math.cos(math.degrees(n)))
                    targetleft.move(dxl,dyl)
                    sleep(.2)
                    count = 0
                    while l_y <= 450 or l_x >= 600:
                        count += 1
                        l_x = targetleft.getCenter().getX()
                        l_y = targetleft.getCenter().getY()
                        dxl = (p * math.cos(math.degrees(n)))
                        dyl = ((p * -math.sin(math.degrees(n)))+g*count)
                        targetleft.move(dxl,dyl)
                        mousekey = demo.checkMouse()
                        sleep(.1)
                        if l_x >= 600 or l_y >= 450:
                            targetleft.undraw()
                            dyl = 0
                            dxl = 0
                        if mousekey != None:
                            x = mousekey.getX()
                            y = mousekey.getY()
                            click_x_r = abs(x - r_x)
                            click_x_l = abs(x - l_x)
                            click_y_r = abs(y - r_y)
                            click_y_l = abs(y - l_y)
                            #Puts the word MISSED on the screen if the click is not on either target 
                            if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                                missed = Text(Point(300,100),'MISSED')
                                missed.draw(demo)
                                sleep(.1)
                                missed.undraw()
                            if click_x_l <= 4 and click_y_l <= 4:
                                targetleft.undraw()
                                #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                                #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                                right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                                right_triangle.setFill(custom[2])
                                right_triangle.draw(demo)
                                
                                left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                                left_triangle.setFill(custom[2])
                                left_triangle.draw(demo)
                                
                                center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                                center_triangle.setFill(custom[2])
                                center_triangle.draw(demo)
                                sleep(.2)
                                #Undraws the triangles so it looks like they fell to the ground 
                                left_triangle.undraw()
                                center_triangle.undraw()
                                right_triangle.undraw()
                                s += .5
                                dyl = 0
                                dxl = 0
                        if dxr == 0 and dxl == 0:
                            demo.close()
                            break
                if dxr == 0 and dxl == 0:
                    demo.close()
                    break
    else:
        targetright = Circle(Point(600,442),8)
        targetright.setFill(custom[2])
        targetright.draw(demo)
        targetleft = Circle(Point(0,442),8)
        sleep(2)
        r_y = targetright.getCenter().getY()
        r_x = targetright.getCenter().getX()
        l_y = targetleft.getCenter().getY()
        l_x = targetleft.getCenter().getX()
        dxr = (p * math.cos(math.degrees(n)))
        dyr = (p * -math.sin(math.degrees(n)))
        targetright.move(dxr,0)
        count = 0
        while r_x >= 0:
            count += 1
            mousekey = demo.checkMouse()
            dxr = (p * math.cos(math.degrees(n)))
            dxl = (p * math.cos(math.degrees(n)))
            r_y = targetright.getCenter().getY()
            r_x = targetright.getCenter().getX()
            targetright.move(dxr,0)
            sleep(.1)
            if r_x <= 0:
                targetright.undraw()
                dyr = 0
                dxr = 0
                targetleft.setFill(custom[2])
                targetleft.draw(demo)
                dxl = -(p * math.cos(math.degrees(n)))
                targetleft.move(dxl,0)
                sleep(.2)
                count = 0
                while l_x <= 600:
                    count += 1
                    l_x = targetleft.getCenter().getX()
                    l_y = targetleft.getCenter().getY()
                    dxl = -(p * math.cos(math.degrees(n)))
                    targetleft.move(dxl,0)
                    mousekey = demo.checkMouse()
                    sleep(.1)
                    if l_x >= 600:
                        targetleft.undraw()
                        dyl = 0
                        dxl = 0
                    if mousekey != None:
                        x = mousekey.getX()
                        y = mousekey.getY()
                        click_x_r = abs(x - r_x)
                        click_x_l = abs(x - l_x)
                        click_y_r = abs(y - r_y)
                        click_y_l = abs(y - l_y)
                        #Puts the word MISSED on the screen if the click is not on either target 
                        if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                            missed = Text(Point(300,100),'MISSED')
                            missed.draw(demo)
                            sleep(.1)
                            missed.undraw()
                        if click_x_l <= 4 and click_y_l <= 4:
                            targetleft.undraw()
                            s += .5
                            dyl = 0
                            dxl = 0
                            #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                            #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                            right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                            right_triangle.setFill(custom[2])
                            right_triangle.draw(demo)
                            
                            left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                            left_triangle.setFill(custom[2])
                            left_triangle.draw(demo)
                            
                            center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                            center_triangle.setFill(custom[2])
                            center_triangle.draw(demo)
                            sleep(.2)
                            #Undraws the triangles so it looks like they fell to the ground 
                            right_triangle.undraw()
                            left_triangle.undraw()
                            center_triangle.undraw()
                    if dxr == 0 and dxl == 0:
                        demo.close()
                        break
            if dxr == 0 and dxl == 0:
                demo.close()
                break

            if mousekey != None:
                x = mousekey.getX()
                y = mousekey.getY()
                click_x_r = abs(x - r_x)
                click_x_l = abs(x - l_x)
                click_y_r = abs(y - r_y)
                click_y_l = abs(y - l_y)
                #Puts the word MISSED on the screen if the click is not on either target 
                if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.draw(demo)
                    sleep(.1)
                    missed.undraw()
                if click_x_r <= 4 and click_y_r <= 4:
                    targetright.undraw()
                    #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                    #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                    right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                    right_triangle.setFill(custom[2])
                    right_triangle.draw(demo)
                    
                    left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                    left_triangle.setFill(custom[2])
                    left_triangle.draw(demo)
                
                    center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                    center_triangle.setFill(custom[2])
                    center_triangle.draw(demo)
                    sleep(.2)
                    #Undraws the triangles so it looks like they fell to the ground 
                    right_triangle.undraw()
                    left_triangle.undraw()
                    center_triangle.undraw()
                    dyr = 0
                    dxr = 0
                    s += .5
                    targetleft.setFill(custom[2])
                    targetleft.draw(demo)
                    dyl = -(p * -math.sin(math.degrees(n)))
                    dxl = (p * math.cos(math.degrees(n)))
                    targetleft.move(dxl,0)
                    sleep(.2)
                    while l_y <= 450 or l_x >= 600:
                        l_x = targetleft.getCenter().getX()
                        l_y = targetleft.getCenter().getY()
                        dxl = -(p * math.cos(math.degrees(n)))
                        dyl = ((p * -math.sin(math.degrees(n)))+g*count)
                        targetleft.move(dxl,0)
                        mousekey = demo.checkMouse()
                        sleep(.1)
                        if l_x >= 600 or l_y >= 450:
                            targetleft.undraw()
                            dyl = 0
                            dxl = 0
                        if mousekey != None:
                            x = mousekey.getX()
                            y = mousekey.getY()
                            click_x_r = abs(x - r_x)
                            click_x_l = abs(x - l_x)
                            click_y_r = abs(y - r_y)
                            click_y_l = abs(y - l_y)
                            #Puts the word MISSED on the screen if the click is not on either target 
                            if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                                missed = Text(Point(300,100),'MISSED')
                                missed.draw(demo)
                                sleep(.1)
                                missed.undraw()
                            if click_x_l <= 4 and click_y_l <= 4:
                                targetleft.undraw()
                                #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                                #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                                right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                                right_triangle.setFill(custom[2])
                                right_triangle.draw(demo)

                                left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                                left_triangle.setFill(custom[2])
                                left_triangle.draw(demo)

                                center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                                center_triangle.setFill(custom[2])
                                center_triangle.draw(demo)
                                sleep(.2)
                                #Undraws the triangles so it looks like they fell to the ground 
                                right_triangle.undraw()
                                left_triangle.undraw()
                                center_triangle.undraw()
                                s += .5
                                dyl = 0
                                dxl = 0
                        if dxr == 0 and dxl == 0:
                            demo.close()
                            break
                if dxr == 0 and dxl == 0:
                    demo.close()
                    break
    return s

def game_d(demo,n,p,g, custom):
    r_or_p = random.randint(1,2)
    s = 0
    r = random.randint(350,450)
    l = random.randint(350,450)
    if r_or_p == 2:
        targetright = Circle(Point(0,r),8)
        targetright.setFill(custom[2])
        targetright.draw(demo)
        targetleft = Circle(Point(600,l),8)
        targetleft.setFill(custom[2])
        targetleft.draw(demo)
        sleep(2)
        r_y = targetright.getCenter().getY()
        l_y = targetleft.getCenter().getY()
        r_x = targetright.getCenter().getX()
        l_x = targetleft.getCenter().getX()
        dxr = -(p * math.cos(math.degrees(n)))
        dyr = (p * -math.sin(math.degrees(n)))
        dxl = (p * math.cos(math.degrees(n)))
        dyl = (p * -math.sin(math.degrees(n)))
        targetright.move(dxr,dyr)
        targetleft.move(dxl,dyl)
        count = 0
        
        while r_y <= 450 or l_y <= 450:
            count += 1
            mousekey = demo.checkMouse()
            dxr = -(p * math.cos(math.degrees(n)))
            dyr = ((p * -math.sin(math.degrees(n)))+g*count)
            dxl = (p * math.cos(math.degrees(n)))
            dyl = ((p * -math.sin(math.degrees(n)))+g*count)
            r_y = targetright.getCenter().getY()
            l_y = targetleft.getCenter().getY()
            r_x = targetright.getCenter().getX()
            l_x = targetleft.getCenter().getX()
            targetright.move(dxr,dyr)
            targetleft.move(dxl,dyl)
            sleep(.1)
            if r_x <= 0 or r_y >= 450:
                targetright.undraw()
                dyr = 0
                dxr = 0
            if l_x >= 600 or l_y >= 450:
                targetleft.undraw()
                dyl = 0
                dxl = 0
            if dxr == 0 and dxl == 0:
                demo.close()
                break
            if mousekey != None:
                x = mousekey.getX()
                y = mousekey.getY()
                click_x_r = abs(x - r_x)
                click_x_l = abs(x - l_x)
                click_y_r = abs(y - r_y)
                click_y_l = abs(y - l_y)
                #Puts the word MISSED on the screen if the click is not on either target 
                if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.draw(demo)
                    sleep(.1)
                    missed.undraw()
                if click_x_r <= 4 and click_y_r <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.undraw()
                    targetright.undraw()
                    dyr = 0
                    dxr = 0
                    s += .5
                    #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                    #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                    right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                    right_triangle.setFill(custom[2])
                    right_triangle.draw(demo)
                    
                    left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                    left_triangle.setFill(custom[2])
                    left_triangle.draw(demo)

                    center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                    center_triangle.setFill(custom[2])
                    center_triangle.draw(demo)
                    sleep(.2)
                    #Undraws the triangles so it looks like they fell to the ground 
                    right_triangle.undraw()
                    left_triangle.undraw()
                    center_triangle.undraw()
                elif click_x_l <= 4 and click_y_l <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.undraw()
                    targetleft.undraw()
                    s += .5
                    dyl = 0
                    dxl = 0
                    #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                    #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                    right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                    right_triangle.setFill(custom[2])
                    right_triangle.draw(demo)
                    
                    left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                    left_triangle.setFill(custom[2])
                    left_triangle.draw(demo)
                    
                    center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                    center_triangle.setFill(custom[2])
                    center_triangle.draw(demo)
                    sleep(.2)
                    #Undraws the triangles so it looks like they fell to the ground 
                    right_triangle.undraw()
                    left_triangle.undraw()
                    center_triangle.undraw()
                
                if dxr == 0 and dxl == 0:
                    demo.close()
                    break
    else:
        targetright = Circle(Point(600,442),8)
        targetright.setFill(custom[2])
        targetright.draw(demo)
        targetleft = Circle(Point(0,442),8)
        targetleft.setFill(custom[2])
        targetleft.draw(demo)
        sleep(2)
        r_x = targetright.getCenter().getX()
        l_x = targetleft.getCenter().getX()
        dxl = -(p * math.cos(math.degrees(n)))
        dxr = (p * math.cos(math.degrees(n)))
        targetright.move(dxr,0)
        targetleft.move(dxl,0)
        while r_x <= 600 and l_x >= 0:
            mousekey = demo.checkMouse()
            r_y = targetright.getCenter().getY()
            l_y = targetleft.getCenter().getY()
            r_x = targetright.getCenter().getX()
            l_x = targetleft.getCenter().getX()
            dxl = -(p * math.cos(math.degrees(n)))
            dxr = (p * math.cos(math.degrees(n)))
            targetright.move(dxr,0)
            targetleft.move(dxl,0)
            sleep(.1)
            if r_x <= 0 and l_x >= 600:
                targetright.undraw()
                targetleft.undraw()
                dxr = 0
                dxl = 0
            if dxr == 0 and dxl == 0:
                demo.close()
                break
            if mousekey != None:
                x = mousekey.getX()
                y = mousekey.getY()
                click_x_r = abs(x - r_x)
                click_x_l = abs(x - l_x)
                click_y_r = abs(y - r_y)
                click_y_l = abs(y - l_y)
                #Puts the word MISSED on the screen if the click is not on either target 
                if not click_x_r <= 4 and not click_y_r <= 4 and not click_x_l <= 4 and not click_y_l <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.draw(demo)
                    sleep(.1)
                    missed.undraw()
                if click_x_r <= 4 and click_y_r <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.undraw()
                    targetright.undraw()
                    dxr = 0
                    s += .5
                    #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                    #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                    right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                    right_triangle.setFill(custom[2])
                    right_triangle.draw(demo)

                    left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                    left_triangle.setFill(custom[2])
                    left_triangle.draw(demo)

                    center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                    center_triangle.setFill(custom[2])
                    center_triangle.draw(demo)
                    sleep(.2)
                    #Undraws the triangles so it looks like they fell to the ground 
                    right_triangle.undraw()
                    center_triangle.undraw()
                    left_triangle.undraw()
                if click_x_l <= 4 and click_y_l <= 4:
                    missed = Text(Point(300,100),'MISSED')
                    missed.undraw()
                    targetleft.undraw()
                    s += .5
                    dxl = 0
                    #Makes it look like the target explodes like it has been shot by breaking it into multiple small triangles
                    #Takes the location of the mouse where it hit the target and draws triangles around the area of the skeet
                    right_triangle = Polygon(Point(x+3,y+7),Point(x+9,y+7),Point(x+6,y+17))
                    right_triangle.setFill(custom[2])
                    right_triangle.draw(demo)
                
                    left_triangle = Polygon(Point(x-3,y+9),Point(x-9,y+9),Point(x-6,y-1))
                    left_triangle.setFill(custom[2])
                    left_triangle.draw(demo)
                    
                    center_triangle = Polygon(Point(x,y-3),Point(x-6,y-3),Point(x-3,y-13))
                    center_triangle.setFill(custom[2])
                    center_triangle.draw(demo)
                    sleep(.2)
                    #Undraws the triangles so it looks like they fell to the ground 
                    right_triangle.undraw()
                    left_triangle.undraw()
                    center_triangle.undraw()
                if dxr == 0 and dxl == 0:
                    demo.close()
                    break
    return s
#You can customize the colors of the sky, ground and skeet

def custom():
    sky_color = 'sky blue'
    ground_color = 'green'
    skeet_color = 'dark grey'
    window = GraphWin('Custom Window',300,300)
    
    sky_box = Rectangle(Point(0,0),Point(100,300))
    sky_box.setFill(sky_color)
    sky_box.draw(window)
    
    ground_box = Rectangle(Point(100,0),Point(200,300))
    ground_box.setFill(ground_color)
    ground_box.draw(window)
    
    skeet_box = Rectangle(Point(200,0),Point(300,300))
    skeet_box.setFill(skeet_color)
    skeet_box.draw(window)
    
    sky_entry = Entry(Point(50,150),10)
    sky_entry.setText(sky_color)
    sky_entry.draw(window)
    
    ground_entry = Entry(Point(150,150),10)
    ground_entry.setText(ground_color)
    ground_entry.draw(window)
    
    skeet_entry = Entry(Point(250,150),10)
    skeet_entry.setText(skeet_color)
    skeet_entry.draw(window)
    #Type in the color and have the background and skeet change to that color
    sky_color = sky_entry.getText()
    sky_entry.setText(sky_color)
    sky_box.setFill(sky_color)
    ground_color = ground_entry.getText()
    ground_entry.setText(ground_color)
    ground_box.setFill(ground_color)
    skeet_color = skeet_entry.getText()
    skeet_entry.setText(skeet_color)
    skeet_box.setFill(skeet_color)
    return [sky_color, ground_color, skeet_color]
    
    
def angle_up(win,n):
    ang_up = Circle(Point(110,240),10)
    ang_up.setFill('red')
    ang_up.draw(win)
    up_arrow_ang = Line(Point(110,230),Point(110,250))
    up_arrow_ang.setArrow("first")
    up_arrow_ang.draw(win)
    sleep(.1)
    ang_up.setFill('Light Grey')
    if n >= 30 and n <= 60:
        n = n+1
        angle_entry = Entry(Point(70,255),2)
        angle_entry.setText(n)
        angle_entry.draw(win)
    return n
    
def angle_down(win,n):
    ang_down = Circle(Point(110,270),10)
    ang_down.setFill('red')
    ang_down.draw(win)
    down_arrow_ang = Line(Point(110,260),Point(110,280))
    down_arrow_ang.setArrow("last")
    down_arrow_ang.draw(win)
    sleep(.1)
    ang_down.setFill('Light Grey')
    if n >= 30 and n <= 60:
        n = n-1
        angle_entry = Entry(Point(70,255),2)
        angle_entry.setText(n)
        angle_entry.draw(win)
    return n
    
def power_up(win,p):
    p_up = Circle(Point(240,240),10)
    p_up.setFill('red')
    p_up.draw(win)
    up_arrow_p = Line(Point(240,230),Point(240,250))
    up_arrow_p.setArrow("first")
    up_arrow_p.draw(win)
    sleep(.1)
    p_up.setFill('Light Grey')
    if p >= 5 and p <=50:
        p = p+1
        power_entry = Entry(Point(190,255),2)
        power_entry.setText(p)
        power_entry.draw(win)
    return p

def power_down(win,p):
    p_down = Circle(Point(240,270),10)
    p_down.setFill('red')
    p_down.draw(win)
    down_arrow_p = Line(Point(240,260),Point(240,280))
    down_arrow_p.setArrow("last")
    down_arrow_p.draw(win)
    sleep(.1)
    p_down.setFill('Light Grey')
    if p >= 5 and p <=50:
        p = p-1
        power_entry = Entry(Point(190,255),2)
        power_entry.setText(p)
        power_entry.draw(win)
    return p
    
def gravity_up(win,g):
    g_up = Circle(Point(360,240),10)
    g_up.setFill('red')
    g_up.draw(win)
    up_arrow_g = Line(Point(360,230),Point(360,250))
    up_arrow_g.setArrow("first")
    up_arrow_g.draw(win)
    sleep(.1)
    g_up.setFill('Light Grey')
    if g >= 3 and g <= 25:
        g += 1
        gravity_entry = Entry(Point(320,255),2)
        gravity_entry.setText(g)
        gravity_entry.draw(win)
    return g
    
def gravity_down(win,g):
    g_down = Circle(Point(360,270),10)
    g_down.setFill('red')
    g_down.draw(win)
    down_arrow_g = Line(Point(360,260),Point(360,280))
    down_arrow_g.setArrow("last")
    down_arrow_g.draw(win)
    sleep(.1)
    g_down.setFill('Light Grey')
    if g >= 3 and g <= 25:
        g = g-1
        gravity_entry = Entry(Point(320,255),2)
        gravity_entry.setText(g)
        gravity_entry.draw(win)
    return g

def newgame(win):
    score = 0
    ngame = Rectangle(Point(30,50),Point(120,90))
    ngame.setFill('green')
    ngame.draw(win)
    ngame_text = Text(Point(75,70),"NEW GAME")
    ngame_text.draw(win)
    sleep(.1)
    ngame.setFill('gray')
    return ngame

def update(win):
    global start
    file = open('top_scores.txt','r')
    f = file.readlines()
    for t in store:
        t.undraw()
    store.clear()
    t = 360
    if start < 0:
        
        start = 0
    elif start > len(f):
        start = len(f)
    for i in range(start, len(f)):
        if start >= len(f)-1:
            break
        else:
            text = Text(Point(190,t),f[i])
            text.draw(win)
            t += 20
            store.append(text)
    
    
def gamewin(custom):
    
    demo = GraphWin("Game Window",600,600)
    sky = Rectangle(Point(0,0),Point(600,450))
    sky.setFill(custom[0])
    sky.draw(demo)
    ground = Rectangle(Point(600,450),Point(0,600))
    ground.setFill(custom[1])
    ground.draw(demo)
    return demo

def main():
    global start
    #Game Panel
    win = GraphWin("Control Panel", 400,400)
    Game_Panel = Rectangle(Point(20,30),Point(380, 170))
    Game_Panel.setFill('white')
    Game_Panel.draw(win)
    game_text = Text(Point(200,20),"Game Panel")
    game_text.draw(win)
    
    score = 0
    rounds = 0
    
    r_text = Text(Point(195, 140), rounds)
    r_text.draw(win)
    p_score = Text(Point(320,140), score)
    p_score.draw(win)
    
    
    
    #Target Panel
    Target_Panel = Rectangle(Point(20,190),Point(380, 340))
    Target_Panel.setFill('white')
    Target_Panel.draw(win)
    target_text = Text(Point(200,180), "Target Panel")
    target_text.draw(win)

    #Buttons Game Panel
    ngame = Rectangle(Point(30,50),Point(120,90))
    ngame.setFill('grey')
    ngame.draw(win)
    ngame_text = Text(Point(75,70),"NEW GAME")
    ngame_text.draw(win)
    
    #Custom Button
    button = Rectangle(Point(150,50),Point(240,90))
    button.setFill('Purple')
    button.draw(win)
    button_text = Text(Point(195,70),"CUSTOM")
    button_text.draw(win)
    
    #High Score Box
    score_box = Rectangle(Point(20,340),Point(360,400))
    score_box.setFill('white')
    score_box.draw(win)
    
    
    #Score Up Button
    score_up = Rectangle(Point(360,340),Point(380,370))
    score_up.setFill('blue')
    score_up.draw(win)
    
    #Score Up Arrow
    score_up_arrow = Line(Point(370,340),Point(370,370))
    score_up_arrow.setArrow('first')
    score_up_arrow.draw(win)
    
    #Score Down Button
    score_down = Rectangle(Point(360,370),Point(380,400))
    score_down.setFill('blue')
    score_down.draw(win)
    
    #Score Down Arrow
    score_down_arrow = Line(Point(370,370),Point(370,400))
    score_down_arrow.setArrow('last')
    score_down_arrow.draw(win)

    update(win)

    #Quit Button
    quit_b = Rectangle(Point(270,50),Point(370,90))
    quit_b.setFill('red')
    quit_b.draw(win)
    quit_text = Text(Point(320,70),"QUIT")
    quit_text.draw(win)
    
    #Player Entry Box and Text
    player_text = Text(Point(75,110),"Player")
    player_text.draw(win)
    player_box = Rectangle(Point(30,120), Point(120, 160))
    player_box.draw(win)
    player_entry = Entry(Point(75,140),7)
    player_entry.draw(win)
    player_name = player_entry.getText()
    
    
    #Round Text
    round_text = Text(Point(195,110),"Round")
    round_text.draw(win)
    round_box = Rectangle(Point(170,120), Point(220,160))
    round_box.draw(win)
    
    #Score Entry Box and Text
    score_text = Text(Point(320,110), "Score")
    score_text.draw(win)
    score_box = Rectangle(Point(295,120),Point(345,160))
    score_box.draw(win)
    #Target Pannel Buttons
    
    #Angle Up and Entry Box
    n = 45
    angle_text = Text(Point(75,210), "Angle")
    angle_text.draw(win)
    ang_up = Circle(Point(110,240),10)
    ang_up.setFill('Light Grey')
    ang_up.draw(win)
    ang_box = Rectangle(Point(50,230),Point(90,280))
    ang_box.draw(win)
    up_arrow_ang = Line(Point(110,230),Point(110,250))
    up_arrow_ang.setArrow("first")
    up_arrow_ang.draw(win)
    angle_entry = Entry(Point(70,255),2)
    angle_entry.setText(n)
    angle_entry.draw(win)
    
    #Angle Down
    ang_down = Circle(Point(110,270),10)
    ang_down.setFill('Light Grey')
    ang_down.draw(win)
    down_arrow_ang = Line(Point(110,260),Point(110,280))
    down_arrow_ang.setArrow("last")
    down_arrow_ang.draw(win)
    
    #Power Up and Entry Box
    p = 25
    power_text = Text(Point(195, 210), "Power")
    power_text.draw(win)
    p_up = Circle(Point(240,240),10)
    p_up.setFill('Light Grey')
    p_up.draw(win)
    power_box = Rectangle(Point(170,230),Point(220,280))
    power_box.draw(win)
    up_arrow_p = Line(Point(240,230),Point(240,250))
    up_arrow_p.setArrow("first")
    up_arrow_p.draw(win)
    power_entry = Entry(Point(190,255),2)
    power_entry.setText(p)
    power_entry.draw(win)
    
    #Power Down
    p_down = Circle(Point(240,270),10)
    p_down.setFill('Light Grey')
    p_down.draw(win)
    down_arrow_p = Line(Point(240,260),Point(240,280))
    down_arrow_p.setArrow("last")
    down_arrow_p.draw(win)
    
    #Gravity Up and Entry Box
    g = 5
    gravity_text = Text(Point(320,210), "Gravity")
    gravity_text.draw(win)
    g_up = Circle(Point(360,240),10)
    g_up.setFill('Light Grey')
    g_up.draw(win)
    up_arrow_g = Line(Point(360,230),Point(360,250))
    up_arrow_g.setArrow("first")
    up_arrow_g.draw(win)
    gravity_box = Rectangle(Point(300,230),Point(340,280))
    gravity_box.draw(win)
    gravity_entry = Entry(Point(320,255),2)
    gravity_entry.setText(g)
    gravity_entry.draw(win)
    
    #Gravity Down
    g_down = Circle(Point(360,270),10)
    g_down.setFill('Light Grey')
    g_down.draw(win)
    down_arrow_g = Line(Point(360,260),Point(360,280))
    down_arrow_g.setArrow("last")
    down_arrow_g.draw(win)
    
    #Pull Single
    pull_bs = Rectangle(Point(80,290),Point(190,330))
    pull_bs.setFill('pink')
    pull_bs.draw(win)
    pull_text_s = Text(Point(135, 310), "PULL SINGLE")
    pull_text_s.draw(win)
    
    #Pull Double
    pull_bd = Rectangle(Point(205,290),Point(320,330))
    pull_bd.setFill('Pink')
    pull_bd.draw(win)
    pull_text_d = Text(Point(263, 310), "PULL DOUBLE")
    pull_text_d.draw(win)
    
    while True:
        mousekey = win.getMouse()
        x = mousekey.getX()
        y = mousekey.getY()
        #Button to bring up color control pannel
        if x >= 150 and x <= 240 and y >= 50 and y <= 90:
            colors = []
            colors = custom()
        if player_entry.getText() != "":
            
            if x >= 80 and x <= 190 and y >= 290 and y <= 330:
                r_text.undraw()
                pull_s(win,x,y)
                rounds += 1
                r_text = Text(Point(195, 140), rounds)
                r_text.draw(win)
                temp = 0
                s = game_s(gamewin(colors),n,p,g, colors)
                temp += s
                score += (temp/rounds)*100
                g = round(score, 2)
                p_score.undraw()
                p_score = Text(Point(320,140), g)
                p_score.draw(win)   
                if s == 0.0:
                    sort_score(player_entry.getText(),g,rounds)
                    rounds = 0
                    score = 0
                    r_text.undraw()
                    r_text = Text(Point(195, 140), rounds)
                    r_text.draw(win)
                    p_score.undraw()
                    p_score = Text(Point(320,140), score)
                    p_score.draw(win)
                    newgame(win)
                    
        if player_entry.getText() != "":
            
            if x >= 205 and x <= 320 and y >= 290 and y <= 330:
                r_text.undraw()
                pull_d(win,x,y)
                rounds += 1
                r_text = Text(Point(195, 140), rounds)
                r_text.draw(win)
                temp = 0
                s = game_d(gamewin(colors),n,p,g, colors)
                temp += s
                score += (temp/rounds)*100
                g = round(score, 2)
                p_score.undraw()
                p_score = Text(Point(320,140), g)
                p_score.draw(win)    
                if s == 0.0:
                    sort_score(player_entry.getText(),g,rounds)
                    rounds = 0
                    score = 0
                    r_text.undraw()
                    r_text = Text(Point(195, 140), rounds)
                    r_text.draw(win)
                    p_score.undraw()
                    p_score = Text(Point(320,140), score)
                    p_score.draw(win)
                    newgame(win)
                    
        if x >= 30 and x <= 120 and y >= 50 and y <= 90:
            newgame(win)
            rounds = 0
            scores = 0
        
        
        if x >= 100 and x <= 120 and y >= 230 and y <= 250:
            n = angle_up(win,n)
            
        if x >= 100 and x <= 120 and y >= 260 and y <= 280:
            n = angle_down(win,n)
            
        if x >= 230 and x <= 250 and y >= 230 and y <= 250:
            p = power_up(win,p)
            
        if x >= 230 and x <= 250 and y >= 260 and y <= 280:
            p = power_down(win,p)
            
        if x >= 350 and x <= 370 and y >= 230 and y <= 250:
            g = gravity_up(win,g)
            
        if x >= 350 and x <= 370 and y >= 260 and y <= 280:
            g = gravity_down(win,g)
            
        if x >= 360 and x <= 380 and y >= 340 and y < 370:
            start -= 1
            update(win)
        if x >= 360 and x <= 380 and y > 370 and y <= 400:
            start += 1
            update(win)
        if x >= 270 and x <= 370 and y >= 50 and y <= 90:
            win.close()
            credit()
    
main()
