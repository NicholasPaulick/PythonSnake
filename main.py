#imports stuff
import turtle as tr
import time
import random

#sets size and stuff
global score
global snakes
snakes = []
score = 0
tr.setworldcoordinates(0,0,100,100)
snakelen = 1
snakespeed = 5
snakeparts = []
crash = False
dot = tr.Turtle()
tr.pu()
tr.goto(50,50)
tr.shape("square")
tr.color("green")
print("To play select a Difficult out of E (easy), M (medium), H (hard). Use the wasd keys to control the direction that the snake goes. Make sure not to crash into the walls or yourself.")
difflet = input("Chose A Difficult (E,M,H)")
diffspeed = "f"
while diffspeed == "f":
  if difflet == "E":
    diffspeed = 0.5
  elif difflet == "M":
    diffspeed = 0.25
  elif difflet == "H":
    diffspeed = 0.105
  elif difflet == "I":
    diffspeed = 0.005

#walls
wall = tr.Turtle()
wall.speed(0)
wall.color("blue")
wall.width(10)
walls = False
while walls == False:
  wall.fd(100)
  wall.seth(90)
  wall.fd(100)
  wall.seth(180)
  wall.fd(100)
  wall.seth(270)
  wall.fd(100)
  walls = True

#movment
def dots():
  dot.clear()
  dot.color("red")
  dot.shape("circle")
  dx = random.randint(4,95)
  dy = random.randint(4,95)
  dot.pu()
  dot.goto(dx,dy)
def dotc():
  global score
  px = tr.xcor()
  py = tr.ycor()
  dox = dot.xcor()
  doy = dot.ycor()
  if px >= dox:
    rdx = px - dox
  elif px < dox:
    rdx = dox - px
  if py >= doy:
    rdy = py - doy
  elif py < doy:
    rdy = doy -py
  if rdx <= 4 and rdy <= 4:
    score += 1
    dots()
    grow()
def grow():
  global snakes
  global score
  bodys = tr.Turtle()
  bodys.pu()
  bodys.shape("square")
  bodys.color("orange")
  snakes.append(bodys)
def movement():
  tr.fd(5)
def up():
  tr.seth(90)
def down():
  tr.seth(270)
def left():
  tr.seth(180)
def right():
  tr.seth(0)
def checkcrash():
  x = tr.xcor()
  y = tr.ycor()
  if x >= 97.7 or x <= 2 or y <= 2 or y >= 97.7:
    tr.resetscreen()
    tr.ht()
    return(True)
    print(x)
  else:
    return(False)
def bodycrash():
  global snakes
  x = tr.xcor()
  y = tr.ycor()
  for each in range(len(snakes)-1, 0, -1):
    nx = snakes[each - 1].xcor()
    ny = snakes[each - 1].ycor()
    if abs(x-nx) <= 2:
      if abs(y-ny) <= 2:
        tr.resetscreen()
        tr.ht()
        return(True)
      else:
        return(False)
    else:
      return(False)
#bulk of work
dots()
while crash == False:
  tr.onkeypress(up,"w")
  tr.onkeypress(down,"s")
  tr.onkeypress(left,"a")
  tr.onkeypress(right,"d")
  tr.listen()
  time.sleep(diffspeed)
  x = tr.xcor()
  y = tr.ycor()
  movement()
  dotc()
  if len(snakes) != 0:
    snakes[0].goto(x, y)
  for each in range(len(snakes)-1, 0, -1):
    nx = snakes[each - 1].xcor()
    ny = snakes[each - 1].ycor()
    snakes[each].goto(nx,ny)
  crashwall = checkcrash()
  crashbody = bodycrash()
  if crashwall or crashbody == True:
    crash = True
    snakes.clear()
    tr.pu()
    tr.goto(50,50)
    tr.pd()
    tr.write("You lost", False, align="center", font=("Arial", 20, "normal"))
    tr.pu()
    tr.goto(50,40)
    tr.pd()
    tr.write("Your score: "+ str(score),False, align="center",font=("Arial", 20, "normal"))

tr.mainloop
