#importing modules
import turtle
import os
import math
import random

#setting up
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space INvaders")
wn.bgpic("Bg_invader.gif")

#register player and enemy shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")
wn.register_shape("laser.gif")

#set border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

#set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("green")
score_pen.penup()
score_pen.setposition(-290,270)
scorestring = "Score: %s" %score 
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()  

#PLAYER TURTLE
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-240)
player.setheading(90)
playerspeed = 5  #(default value variable to move)

#choose a number of enemies
number_of_enemies = 10
#empty list of enemies
enemies = []
#add enemies to the list
for i in range(number_of_enemies):
    #create enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:  
    enemy.shape("invader.gif")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(150,250)    
    enemy.setposition(x,y)
enemyspeed = 2

#create player"s bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("laser.gif")
bullet.penup()
bullet.speed(0)
bullet.setposition(0,-270)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 40


#DEFINE BULLET STATE
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x<-280:
        x =-280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x>280:
        x=280
    player.setx(x)

def fire_bullet():
    #declares bulletstate as global if it needs to be chaged
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision (t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+(math.pow(t1.ycor()-t2.ycor(),2)))
    if distance < 22:
        return True
    else:
        return False

#keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet,"space")

#MAIN GAME LOOP
while True:
    for enemy in enemies:
        #enemy move
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #move the enemy back and forth
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        #check for collision
        if isCollision(bullet,enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reset enemy
            x = random.randint(-200,200)
            y = random.randint(150,250)    
            enemy.setposition(x,y)
            #update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check if bullet reached top
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"
    


delay = input("click to exit")