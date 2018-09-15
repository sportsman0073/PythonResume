#CS - 177 project2.py
#Nicholas Koontz
# Skeet Shooting game
import math
from graphics import *
from time import sleep
import random

names = []
hscore = []

def sort_score(player_name, score):
    file = open('top_scores.txt','w')
    s = str(score)
    names.append(player_name)
    hscore.append(s)
    print(hscore)

    limit = 0
    if len(hscore) >= 10:
        limit = 10
    else:
        limit = len(hscore)

    for i in range(limit):
        for j in range(i+1, limit):
            if hscore[j] > hscore[i]:
                stmp = hscore[i]
                hscore[i] = hscore[j]
                hscore[j] = stmp
                ntmp = names[j]
                names[j] = names[i]
                names[i] = ntmp
                print(hscore)
    file.seek(0)
    file.truncate()
    file.write('Top 10 Scores\n')
    file.write('=============\n')
    for i in range(limit):
        file.write(str(i+1)+". "+names[i]+'    '+hscore[i]+'\n')
    file.close()

def pull(win,x,y):
    pull_b = Rectangle(Point(140,320),Point(250,360))
    pull_b.setFill('yellow')
    pull_b.draw(win)
    pull_text = Text(Point(195, 340), "PULL")
    pull_text.draw(win)
    sleep(.1)
    pull_b.setFill('pink')
    
def high_scores(player_entry, score):
    scores = GraphWin('High Scores',200,400)
    file = open('top_scores.txt','r')
    f = file.readlines()
    print(f)
    txt = ''
    for i in range(len(f)):
        txt += f[i]
    top_10 = Text(Point(100, 100), txt)
    top_10.draw(scores)
    mouseclick = scores.getMouse()
    while mouseclick == None:
        mouseclick = scores.getMouse()
    if mouseclick != None:
        scores.close()
    
def game(demo,n,p,g):
    s = 0
    r = random.randint(350,450)
    l = random.randint(350,450)
    targetright = Circle(Point(0,r),8)
    targetright.setFill('dark grey')
    targetright.draw(demo)
    targetleft = Circle(Point(600,l),8)
    targetleft.setFill('dark grey')
    targetleft.draw(demo)
    sleep(2)
    r_y = targetright.getCenter().getY()
    l_y = targetleft.getCenter().getY()
    r_x = targetright.getCenter().getX()
    l_x = targetright.getCenter().getX()
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
        l_x = targetright.getCenter().getX()
        targetright.move(dxr,dyr)
        targetleft.move(dxl,dyl)
        sleep(.1)
        if r_x <= 0:
            targetright.undraw()
            dyr = 0
            dxr = 0
        if l_x >= 600:
            targetleft.undraw()
            dyl = 0
            dxl = 0
        if r_y >= 450:
            targetright.undraw()
            dyr = 0
            dxr = 0
        if l_y >= 450:
            targetleft.undraw()
            dyl = 0
            dxl = 0
        if dxr == 0 and dxl == 0:
            demo.close()
            break
        if mousekey != None:
            x = mousekey.getX()
            y = mousekey.getY()
            click_x_r = x - r_x
            click_x_l = x - l_x
            click_y_r = y - r_y
            click_y_l = y - l_y
            if click_x_r <= 4:
                targetright.undraw()
                dyr = 0
                dxr = 0
                s += (g+p)/10
                round(s,3)
            elif click_x_l <= 4:
                targetleft.undraw()
                s += (g+p)/10
                dyl = 0
                dxl = 0
                round(s,3)
            elif click_y_r <= 4:
                targetright.undraw()
                dyr = 0
                dxr = 0
                s += (g+p)/10
                round(s,3)
            elif click_y_l <= 4:
                targetleft.undraw()
                dyl = 0
                dxl = 0
                s += (g+p)/10
                round(s,3)
            if dxr == 0 and dxl == 0:
                demo.close()
                break
    return s
    
    
def angle_up(win,n):
    ang_up = Circle(Point(110,270),10)
    ang_up.setFill('red')
    ang_up.draw(win)
    up_arrow_ang = Line(Point(110,280),Point(110,260))
    up_arrow_ang.setArrow("last")
    up_arrow_ang.draw(win)
    sleep(.1)
    ang_up.setFill('Light Grey')
    if n >= 30 and n <= 60:
        n = n+1
        angle_entry = Entry(Point(70,285),2)
        angle_entry.setText(n)
        angle_entry.draw(win)
    return n
    
def angle_down(win,n):
    ang_down = Circle(Point(110,300),10)
    ang_down.setFill('red')
    ang_down.draw(win)
    down_arrow_ang = Line(Point(110,290),Point(110,310))
    down_arrow_ang.setArrow("last")
    down_arrow_ang.draw(win)
    sleep(.1)
    ang_down.setFill('Light Grey')
    if n >= 30 and n <= 60:
        n = n-1
        angle_entry = Entry(Point(70,285),2)
        angle_entry.setText(n)
        angle_entry.draw(win)
    return n
    
def power_up(win,p):
    p_up = Circle(Point(240,270),10)
    p_up.setFill('red')
    p_up.draw(win)
    up_arrow_p = Line(Point(240,280),Point(240,260))
    up_arrow_p.setArrow("last")
    up_arrow_p.draw(win)
    sleep(.1)
    p_up.setFill('Light Grey')
    if p >= 5 and p <=50:
        p = p+1
        power_entry = Entry(Point(190,285),2)
        power_entry.setText(p)
        power_entry.draw(win)
    return p

def power_down(win,p):
    p_down = Circle(Point(240,300),10)
    p_down.setFill('red')
    p_down.draw(win)
    down_arrow_p = Line(Point(240,290),Point(240,310))
    down_arrow_p.setArrow("last")
    down_arrow_p.draw(win)
    sleep(.1)
    p_down.setFill('Light Grey')
    if p >= 5 and p <=50:
        p = p-1
        power_entry = Entry(Point(190,285),2)
        power_entry.setText(p)
        power_entry.draw(win)
    return p
    
def gravity_up(win,g):
    g_up = Circle(Point(360,270),10)
    g_up.setFill('red')
    g_up.draw(win)
    up_arrow_g = Line(Point(360,280),Point(360,260))
    up_arrow_g.setArrow("last")
    up_arrow_g.draw(win)
    sleep(.1)
    g_up.setFill('Light Grey')
    if g >= 3 and g <= 25:
        g += 1
        gravity_entry = Entry(Point(320,285),2)
        gravity_entry.setText(g)
        gravity_entry.draw(win)
    return g
    
def gravity_down(win,g):
    g_down = Circle(Point(360,300),10)
    g_down.setFill('red')
    g_down.draw(win)
    down_arrow_g = Line(Point(360,290),Point(360,310))
    down_arrow_g.setArrow("last")
    down_arrow_g.draw(win)
    sleep(.1)
    g_down.setFill('Light Grey')
    if g >= 3 and g <= 25:
        g = g-1
        gravity_entry = Entry(Point(320,285),2)
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
    
def gamewin():
    demo = GraphWin("Game Window",600,600)
    sky = Rectangle(Point(0,0),Point(600,450))
    sky.setFill('sky blue')
    sky.draw(demo)
    ground = Rectangle(Point(600,450),Point(0,600))
    ground.setFill('green')
    ground.draw(demo)
    return demo

def main():
    #Game Panel
    win = GraphWin("Control Panel", 400,400)
    Game_Panel = Rectangle(Point(20,30),Point(380, 180))
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
    Target_Panel = Rectangle(Point(20,220),Point(380, 370))
    Target_Panel.setFill('white')
    Target_Panel.draw(win)
    target_text = Text(Point(200,210), "Target Panel")
    target_text.draw(win)

    #Buttons Game Panel
    ngame = Rectangle(Point(30,50),Point(120,90))
    ngame.setFill('grey')
    ngame.draw(win)
    ngame_text = Text(Point(75,70),"NEW GAME")
    ngame_text.draw(win)
    
    #High Score Button
    high = Rectangle(Point(140,50),Point(250,90))
    high.setFill('blue')
    high.draw(win)
    high_text = Text(Point(195,70),"HIGH SCORES")
    high_text.draw(win)
    
    file = open('top_scores.txt','w')

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
    
    
    #Round Entry Box and Text
    round_text = Text(Point(195,110),"Round")
    round_text.draw(win)
    round_box = Rectangle(Point(170,120), Point(220,160))
    round_box.draw(win)
    
    #Score Entry Box and Text
    score_text = Text(Point(320,110), "Score")
    score_text.draw(win)
    score_box = Rectangle(Point(300,120),Point(340,160))
    score_box.draw(win)
    #Target Pannel Buttons
    
    #Angle Up and Entry Box
    n = 45
    angle_text = Text(Point(75,240), "Angle")
    angle_text.draw(win)
    ang_up = Circle(Point(110,270),10)
    ang_up.setFill('Light Grey')
    ang_up.draw(win)
    ang_box = Rectangle(Point(50,260),Point(90,310))
    ang_box.draw(win)
    up_arrow_ang = Line(Point(110,280),Point(110,260))
    up_arrow_ang.setArrow("last")
    up_arrow_ang.draw(win)
    angle_entry = Entry(Point(70,285),2)
    angle_entry.setText(n)
    angle_entry.draw(win)
    
    #Angle Down
    ang_down = Circle(Point(110,300),10)
    ang_down.setFill('Light Grey')
    ang_down.draw(win)
    down_arrow_ang = Line(Point(110,290),Point(110,310))
    down_arrow_ang.setArrow("last")
    down_arrow_ang.draw(win)
    
    #Power Up and Entry Box
    p = 25
    power_text = Text(Point(195, 240), "Power")
    power_text.draw(win)
    p_up = Circle(Point(240,270),10)
    p_up.setFill('Light Grey')
    p_up.draw(win)
    power_box = Rectangle(Point(170,260),Point(220,310))
    power_box.draw(win)
    up_arrow_p = Line(Point(240,280),Point(240,260))
    up_arrow_p.setArrow("last")
    up_arrow_p.draw(win)
    power_entry = Entry(Point(190,285),2)
    power_entry.setText(p)
    power_entry.draw(win)
    
    #Power Down
    p_down = Circle(Point(240,300),10)
    p_down.setFill('Light Grey')
    p_down.draw(win)
    down_arrow_p = Line(Point(240,290),Point(240,310))
    down_arrow_p.setArrow("last")
    down_arrow_p.draw(win)
    
    #Gravity Up and Entry Box
    g = 5
    gravity_text = Text(Point(320,240), "Gravity")
    gravity_text.draw(win)
    g_up = Circle(Point(360,270),10)
    g_up.setFill('Light Grey')
    g_up.draw(win)
    up_arrow_g = Line(Point(360,280),Point(360,260))
    up_arrow_g.setArrow("last")
    up_arrow_g.draw(win)
    gravity_box = Rectangle(Point(300,260),Point(340,310))
    gravity_box.draw(win)
    gravity_entry = Entry(Point(320,285),2)
    gravity_entry.setText(g)
    gravity_entry.draw(win)
    
    #Gravity Down
    g_down = Circle(Point(360,300),10)
    g_down.setFill('Light Grey')
    g_down.draw(win)
    down_arrow_g = Line(Point(360,290),Point(360,310))
    down_arrow_g.setArrow("last")
    down_arrow_g.draw(win)
    
    #Pull Button
    pull_b = Rectangle(Point(140,320),Point(250,360))
    pull_b.setFill('pink')
    pull_b.draw(win)
    pull_text = Text(Point(195, 340), "PULL")
    pull_text.draw(win)
    
    while True:
        mousekey = win.getMouse()
        x = mousekey.getX()
        y = mousekey.getY()
        if player_entry.getText() != "":
            
            if x >= 140 and x <= 250 and y >= 320 and y <= 360:
                r_text.undraw()
                pull(win,x,y)
                rounds += 1
                r_text = Text(Point(195, 140), rounds)
                r_text.draw(win)
                
                if rounds <= 5:
                    score += game(gamewin(),n,p,g)
                    r_text.undraw()
                    p_score.undraw()
                    p_score = Text(Point(320,140), score)
                    p_score.draw(win)
                    
                else:
                    sort_score(player_entry.getText(),score)
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
            
        if x >= 140 and x <= 250 and y >= 50 and y <= 90:
            high_scores(player_name, score)
        
        if x >= 100 and x <= 120 and y >= 260 and y <= 280:
            n = angle_up(win,n)
            
        if x >= 100 and x <= 120 and y >= 290 and y <= 310:
            n = angle_down(win,n)
            
        if x >= 230 and x <= 250 and y >= 260 and y <= 280:
            p = power_up(win,p)
            
        if x >= 230 and x <= 250 and y >= 290 and y <= 310:
            p = power_down(win,p)
            
        if x >= 350 and x <= 370 and y >= 260 and y <= 280:
            g = gravity_up(win,g)
            
        if x >= 350 and x <= 370 and y >= 290 and y <= 310:
            g = gravity_down(win,g)
            
        if x >= 270 and x <= 370 and y >= 50 and y <= 90:
            win.close()
            file.close()
            
    
main()
