import pgzrun
from sympy import Point, Circle, Line, Ray
import random
import time

WIDTH = 800
HEIGHT = 800

background = (255,255,255)
distance = 25
ear1 = ((WIDTH/2) - (distance/2), HEIGHT/2)
ear2 = ((WIDTH/2) + (distance/2), HEIGHT/2)


point1 = (int(random.randrange(WIDTH)),int(random.randrange(HEIGHT)))
points = []
pos1 = (0,0)

mousedown = 0

def on_mouse_down(pos):
    global mousedown
    mousedown = 1
    
def on_mouse_up(pos):
    global mousedown
    mousedown = 0
    
def on_mouse_move(pos):
    global pos1
    pos1 = pos
    
def update():
    global pos1
    global mousedown
    global points
    if mousedown == 1:
        move_point(pos1)
        d1 = ((ear1[0] - point1[0])**2 + (ear1[1] - point1[1])**2)**0.5
        d2 = ((ear2[0] - point1[0])**2 + (ear2[1] - point1[1])**2)**0.5
        points = []
        step = 4
        pointAmount = 100
  
        for i in range(pointAmount):
            checkPoint(i*step, d1, d2)  




        
        
    

def move_point(pos):
    global point1
    point1 = pos
    
def checkPoint(radius, d1, d2):
    global points
    global ear1
    global ear2
    dr = abs(d1 - d2)
    start = time.time()
    if d1 < d2:
        cSmol = Circle(ear1, radius)
        cBig = Circle(ear2, radius + dr)
    else:
        cSmol = Circle(ear2, radius)
        cBig = Circle(ear1, radius + dr)
    intersections = cSmol.intersection(cBig)
    dt = time.time() - start
    print("time:", dt)
    for i in range(len(intersections)):
        points.append(intersections[i].coordinates)
        print(abs(d2 - d1))
    
    
def draw():
    screen.fill(background)
    screen.draw.filled_circle(ear1, 5, (0,0,0))
    screen.draw.filled_circle(ear2, 5, (0,0,0))
    screen.draw.filled_circle(point1, 5, (0,0,255))
    screen.draw.line(ear1, point1, (255,0,0))
    screen.draw.line(ear2, point1, (255,0,0))
    distance1 = ((ear1[0] - point1[0])**2 + (ear1[1] - point1[1])**2)**0.5
    distance2 = ((ear2[0] - point1[0])**2 + (ear2[1] - point1[1])**2)**0.5
    if distance1 < distance2:
        screen.draw.circle(point1, int(distance1), (0,0,0))
    else:
        screen.draw.circle(point1, int(distance2), (0,0,0))
    screen.draw.text("d1 :" + str(int(distance1)), (0,0), color = (0,0,0), fontsize=32)
    screen.draw.text("d2 :" + str(int(distance2)), (0,32), color = (0,0,0), fontsize=32)
    screen.draw.text("dr :" + str(abs(distance1 - distance2)), (0,64), color = (0,0,0), fontsize=32)
    for i in range(len(points)):
        screen.draw.filled_circle(points[i], 1, (0,255,0))



    
pgzrun.go()
