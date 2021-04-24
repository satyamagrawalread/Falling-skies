import turtle
import random
import time
import winsound #Sound

#HIGH SCORE
with open("highscore.txt","r") as f:
    highscore=f.read()  #value will be stored as a string
    

obj_sc=0
obj_live=5
a=0
b=0
high_sc=int(highscore)

is_right=True
is_right1=True
is_left=True
is_left1=True
is_start=False

level=1
max_speed=2
special_list=[10,15,31,60,90]
level_list=[30,55] # denotes level 2 and 3
corona_list=[36,45,46,49,60,70,72,73,74,80,81,82,85,86]
pc=turtle.Screen()
pc.title("Falling skies by code-geeks")
pc.setup(width=800, height=600)
#pc.bgcolor('black')
pc.bgpic("fallingskiesbg.gif")
pc.tracer(0,0)

#level1 name
wrlevel=turtle.Turtle()
wrlevel.speed(0)  
wrlevel.color("blue")
wrlevel.shape("turtle")
wrlevel.penup()
wrlevel.hideturtle()
wrlevel.goto(0,0)

wrlevel.write("WELCOME TO",align="center",font=("decorative",40,"bold"))
wrlevel.goto(0,-50)
wrlevel.write("FALLING SKIES",align="center",font=("formal",40,"bold"))
time.sleep(4)
wrlevel.clear()


pc.register_shape("camel1.gif")
pc.register_shape("camel3.gif")
pc.register_shape("ammo.gif")
pc.register_shape("bullet.gif")
pc.register_shape("mango.gif")
pc.register_shape("apple.gif")
pc.register_shape("apple1.gif")
pc.register_shape("pear.gif")
pc.register_shape("virus.gif")
pc.register_shape("dir_right.gif")
pc.register_shape("dir_left.gif")

obj=turtle.Turtle()
obj.speed(0)
obj.shape("camel1.gif")
obj.color("red")
obj.penup()
obj.goto(0,-450)
obj.direction="stop"



#create a list of good guys
bullets=[]
for _ in range(10):
    bullet=turtle.Turtle()
    bullet.speed(0)
    bullet.shape("ammo.gif")
    bullet.color("yellow")
    bullet.penup()
    x=random.randint(-350,350)
    y=random.randint(330,1000)
    bullet.goto(x,y)
    bullet.speed=random.randint(3, 6)
    bullets.append(bullet)

apple=turtle.Turtle()
apple.speed(0)
apple.shape("apple.gif")
apple.color("yellow")
apple.penup()
x=random.randint(-350,350)
y=random.randint(340,1000)
apple.goto(x,y)
apple.speed=random.randint(5, 7)
#apple.speed(6)


apple_right=turtle.Turtle()
apple_right.speed(6)
apple_right.shape("apple1.gif")
apple_right.color("yellow")
apple_right.penup()
apple_right.goto(360,340)

dir_right=turtle.Turtle()
dir_right.speed(6)
dir_right.shape("dir_right.gif")
dir_right.color("yellow")
dir_right.penup()
dir_right.goto(360,500)
dir_right.speed=random.randint(4, 6)
#dir_right.speed=6

dir_left=turtle.Turtle()
dir_left.speed(6)
dir_left.shape("dir_left.gif")
dir_left.color("yellow")
dir_left.penup()
dir_left.goto(360,500)
dir_left.speed=random.randint(4, 6)
#dir_left.speed=6


food_mangoes=[]
for _ in range(20):
    food_mango=turtle.Turtle()
    food_mango.speed(0)
    food_mango.shape("mango.gif")
    food_mango.color("yellow")
    food_mango.penup()
    x=random.randint(-350,350)
    y=random.randint(330,1000)
    food_mango.goto(x,y)
    food_mango.speed=random.randint(4, 6)
    food_mangoes.append(food_mango)


corona=turtle.Turtle()
corona.speed(1)
corona.shape("virus.gif")
corona.penup()
x=random.randint(-350,350)
y=random.randint(350,1000)
corona.goto(x,y)

#writing
wr=turtle.Turtle()
wr.speed(0)  
wr.color("yellow")
wr.shape("turtle")
wr.penup()
wr.hideturtle()
wr.goto(0,270)
wr.write("SCORE: {}  LIVES: {}".format(obj_sc,obj_live),align="center",font=("arial",20,"normal"))




def obj_left():
    global is_left
    obj.direction="left"
    obj.shape("camel1.gif")
    is_left=False
    #x=obj.xcor()
    #x-=7
    #obj.setx(x)

def obj_right():
    global is_right
    obj.direction="right"
    obj.shape("camel3.gif")
    is_right=False
    #x=obj.xcor()
    #x+=7
    #obj.setx(x)

def obj_stop():
    obj.direction="stop"


is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused=False
    else:
        is_paused=True 

def start():
    global is_start
    is_start=True   


pc.listen()
pc.onkeypress(obj_left,"Left")
pc.onkeypress(obj_right,"Right")
pc.onkeypress(obj_stop,"space")
pc.onkeypress(toggle_pause,"p")
pc.onkeypress(start,"s")


while not is_start:
    wrlevel.goto(0,50)
    wrlevel.write("Rules",align="center",font=("decorative",40,"bold"))
    wrlevel.goto(0,0)
    wrlevel.write("1.Initially the player has 5 lives.",align="center",font=("formal",14,"bold"))
    wrlevel.goto(0,-50)
    wrlevel.write("2.Player Has to collect Fruits to increase the score and the score increases by 1. ",align="center",font=("formal",14,"bold"))
    wrlevel.goto(0,-100)
    wrlevel.write("3.When the bullet hits the player , the lives decreases. ",align="center",font=("formal",14,"bold"))
    wrlevel.goto(0,-150)
    wrlevel.write("Press P key to pause the game.",align="center",font=("formal",14,"bold"))
    wrlevel.goto(0,-230)
    wrlevel.write("Press S key to start the game.",align="center",font=("formal",14,"bold"))

wrlevel.clear()
obj.goto(0,-250)


wr2=turtle.Turtle()
wr2.speed(0)  
wr2.color("blue")
wr2.shape("turtle")
wr2.penup()
wr2.hideturtle()
wr2.goto(0,0)
wr2.write("TUTORIAL",align="center",font=("arial",20,"bold"))

while is_right:
    if is_right1 is True:
        pc.update()
        y=apple_right.ycor()
        y-=0.3
        apple_right.sety(y)
        if(apple_right.ycor()<=200):
            is_right1=False
    else:
        pc.update()
        dir_right.goto(obj.xcor()+60,obj.ycor())
        wrlevel.goto(0,-50)
        wrlevel.write("PRESS RIGHT KEY",align="center",font=("formal",40,"bold"))


dir_right.goto(450,500)
wrlevel.clear()
is_right=True
while is_right:
    y=apple_right.ycor()
    y-=0.3
    apple_right.sety(y)
    
    if(obj.xcor()>360):
        obj.setx(360)
    elif(obj.xcor()<-360):
        obj.setx(-360)
        
    if(obj.direction=="left"):
        x=obj.xcor()
        x-=0.5
        obj.setx(x)
    elif(obj.direction=="right"):
        x=obj.xcor()
        x+=0.5
        obj.setx(x)
    if(obj.distance(apple_right)<40):
        apple_right.goto(-360,340)
        is_right=False
    pc.update()




while is_left:
    if is_left1 is True:
        pc.update()
        y=apple_right.ycor()
        y-=0.3
        apple_right.sety(y)
        if(apple_right.ycor()<=200):
            is_left1=False
    else:
        pc.update()
        dir_left.goto(obj.xcor()-100,obj.ycor())
        wrlevel.goto(0,-50)
        wrlevel.write("PRESS LEFT KEY",align="center",font=("formal",40,"bold"))


dir_left.goto(450,500)
wrlevel.clear()
is_left=True
while is_left:
    y=apple_right.ycor()
    y-=0.3
    apple_right.sety(y)
    
    if(obj.xcor()>360):
        obj.setx(360)
    elif(obj.xcor()<-360):
        obj.setx(-360)
        
    if(obj.direction=="left"):
        x=obj.xcor()
        x-=0.5
        obj.setx(x)
    elif(obj.direction=="right"):
        x=obj.xcor()
        x+=0.5
        obj.setx(x)
    if(obj.distance(apple_right)<40):
        apple_right.goto(500,500)
        is_left=False
    pc.update()




        

wr2.clear()
wrlevel.goto(0,0)
wrlevel.write("LEVEL: {}".format(level),align="center",font=("formal",20,"bold"))
winsound.PlaySound("level-complete.wav",winsound.SND_ASYNC)
time.sleep(2)

def game_level(level):
    if(level==2):
        for i in food_mangoes:
            i.shape("apple1.gif")
        for i in bullets:
            i.shape("bullet.gif")
        pc.bgpic("fallingskiesbg1.gif")
    elif(level==3):
        for i in food_mangoes:
            i.shape("pear.gif")
        for i in bullets:
            i.shape("virus.gif")
        pc.bgpic("fallingskiesbg2.gif")



    



while True:
    if not is_paused:

        pc.update()

        wrlevel.clear()
        if(obj.xcor()>360):
            obj.setx(360)
        elif(obj.xcor()<-360):
            obj.setx(-360)
        
        if(obj.direction=="left"):
            x=obj.xcor()
            x-=1.5
            obj.setx(x)
        elif(obj.direction=="right"):
            x=obj.xcor()
            x+=1.5
            obj.setx(x)

        if(level!=3):
            for i in bullets:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
            
        else:
            for i in bullets:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
                if(y<=random.randint(-50,50)):
                    x=i.xcor()
                    x=random.randint(x-5,x+5)   
                    i.setx(x) 

             
        
        for i in bullets:
            if(i.distance(obj)<40):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))
                obj_live-=1
                winsound.PlaySound("hurt.wav",winsound.SND_ASYNC)
                wr.clear()
                if obj_sc>int(highscore):
                    highscore=obj_sc
                    print(highscore)
                wr.write("SCORE: {}  LIVES: {}  HIGH SCORE: {}".format(obj_sc,obj_live,highscore),align="center",font=("arial",20,"normal"))
                
                
        


        for i in bullets:
            if(i.ycor()<-300):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))

        if(level!=3):
            for i in food_mangoes:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
            
        else:    
            for i in food_mangoes:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
                if (y<= random.randint(-50,50)):
                    x=i.xcor()
                    x=random.randint(x-5,x+5)   
                    i.setx(x)

        
        for i in food_mangoes:
            if(i.distance(obj)<40):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))
                obj_sc+=1
                winsound.PlaySound("2_bounce.wav",winsound.SND_ASYNC)
                wr.clear()
                if obj_sc>int(highscore):
                    highscore=obj_sc
                    print(highscore)
                wr.write("SCORE: {}  LIVES: {}  HIGH SCORE: {}".format(obj_sc,obj_live,highscore),align="center",font=("arial",20,"normal"))
                

        for i in food_mangoes:
            if(i.ycor()<-300):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))

        if obj_sc in special_list:
            a=1
        
        if(a==1):
            y=apple.ycor()
            y-=random.randint(2,3)
            apple.sety(y)


        if(apple.distance(obj)<40):
            apple.sety(random.randint(340,400))
            apple.setx(random.randint(-350,350))
            a=0
            obj_sc+=5
            winsound.PlaySound("powerup.wav",winsound.SND_ASYNC)
            wr.clear()
            if obj_sc>int(highscore):
                    highscore=obj_sc
                    print(highscore)
            wr.write("SCORE: {}  LIVES: {}  HIGH SCORE: {}".format(obj_sc,obj_live,highscore),align="center",font=("arial",20,"normal"))
                

        if(apple.ycor()<-300):
            apple.sety(random.randint(340,400))
            apple.setx(random.randint(-350,350))
            a=0


        if obj_sc in corona_list:
            b=1
        
        if(b==1):
            y=corona.ycor()
            y-=random.randint(2,3)
            corona.sety(y)


        if(corona.distance(obj)<40):
            corona.sety(random.randint(340,400))
            corona.setx(random.randint(-350,350))
            b=0
            obj_live-=2
            winsound.PlaySound("powerup.wav",winsound.SND_ASYNC)
            wr.clear()
            wr.write("SCORE: {}  LIVES: {}".format(obj_sc,obj_live),align="center",font=("arial",20,"normal"))

        if(corona.ycor()<-300):
            corona.sety(random.randint(340,400))
            corona.setx(random.randint(-350,350))
            b=0

        

        


        if obj_sc in level_list:
            level+=1
            winsound.PlaySound("level-complete.wav",winsound.SND_ASYNC)
            game_level(level)
            wrlevel.write("LEVEL: {}".format(level),align="center",font=("normal",20,"bold"))
            time.sleep(2)
            wrlevel.clear()
            obj_sc+=1
            max_speed+=1
            obj_live+=1
            

            


        if(obj_live<=0):
            wr1=turtle.Turtle()
            wr1.speed(0)  
            wr1.color("blue")
            wr1.shape("turtle")
            wr1.penup()
            wr1.hideturtle()
            wr1.goto(0,0)
            wr1.write("GAME OVER",align="center",font=("arial",60,"normal"))
            winsound.PlaySound("gameover.wav",winsound.SND_ASYNC)
            with open("highscore.txt","w") as f:
                f.write(str(highscore))  #value will be stored as a string
            if(obj_sc>high_sc):
                time.sleep(3)
                wr1.clear()
                wr1.write("Congratulation!",align="center",font=("arial",40,"normal"))
                wr1.goto(0,-60)
                wr1.write("Highest Scorer of the Game",align="center",font=("arial",40,"normal"))
                
            break
    else:
        pc.update()
        wrlevel.write("Press P again to Resume",align="center",font=("arial",40,"normal"))
                    

turtle.done()