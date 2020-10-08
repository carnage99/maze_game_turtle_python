#import
import turtle
import math
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CAUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("DONT EVEN GO NEAR THE RED TRIANGLES , DONT WORRY THEY KILL YOU ONLY IF YOU TOUCH THEM ")
print("                           MAKE YOUR WAY OUT OF THE MAZE")
print("COLLECT AS MANY GOLD CUBES AS POSSIBLE ON THE WAY , PRETTY SURE YOU WON'T COLLECT ALL ")
print("KEEP COUNT , IF YOU COLLECT ALL OF THEM , YOU'VE GOT ONE REASON TO BRAG ABOUT YOURSELF")



#screen setup
turtle.setup(700,700)
wnd=turtle.Screen()
wnd.title("MAZE ADVENTURE")
wnd.bgcolor("white")

#draw lines func
def draw(s):
    myp=turtle.Turtle()
    myp.penup()
    myp.setposition(s[0],s[1])
    myp.speed(0)
    myp.pendown()
    myp.pensize(15)
    myp.goto(s[2],s[3])
    myp.hideturtle()

#dog positions
d2={0:(-280,-265,280,-265,-150,-265),1:(-280,-265,280,-265,50,-265),2:(20,-145,280,-145,20,-145),3:(20,-145,280,-145,230,-145),4:(175,205,275,205,175,205),5:(-280,265,-20,265,-270,265),6:(-280,265,-20,265,-220,265),7:(-280,265,-20,265,-160,265)}

d3={0:(25,-100,25,40,25,30),1:(25,-100,25,40,25,-30),2:(170,-100,170,100,170,60),3:(170,-100,170,100,170,0),4:(250,-100,250,160,250,120),5:(250,-100,250,160,250,0),6:(30,140,30,280,30,180),7:(-30,80,-30,280,-30,240),8:(-250,-220,-250,-180,-250,-220),9:(-130,-160,-130,160,-130,60),10:(-130,-160,-130,160,-130,-20),11:(100,-100,100,40,100,30),12:(100,-100,100,40,100,-30)}

#dogs setup(horizontal)
dog=[]
for i in range(8):
    dog.append(turtle.Turtle())
    dog[i].penup()
    dog[i].color("red")
    dog[i].shape("triangle")
    dog[i].setposition(d2[i][4],d2[i][5])
    dog[i].speed(0)

#dogs setup 2(verticle)
dog2=[]
for i in range(13):
    dog2.append(turtle.Turtle())
    dog2[i].penup()
    dog2[i].color("red")
    dog2[i].shape("triangle")
    dog2[i].setposition(d3[i][4],d3[i][5])
    dog2[i].speed(0)

#gold positions
goldp={0:(75,-215),1:(125,-215),2:(-250,-210),3:(-270,-265),4:(-220,-150),5:(-20,-150),6:(-20,-30),7:(-20,-90),8:(-270,150),9:(-170,150),10:(-70,180),11:(-70,120),12:(-70,30),13:(-10,30),14:(-40,30),15:(240,0),16:(70,210),17:(100,210),18:(130,210),19:(220,280),20:(250,280),21:(280,280)}


#gold setup
gold=[]
for i in range(22):
    gold.append(turtle.Turtle())
    gold[i].penup()
    gold[i].color("gold")
    gold[i].shape("square")
    gold[i].setposition(goldp[i][0],goldp[i][1])
    gold[i].speed(0)

    

    
    
#draw lines
d=((-300,-300,200,-300),(250,-300,300,-300),(300,-300,300,300),(-200,300,300,300),(-300,300,-250,300),(-300,-300,-300,300),(-250,240,-150,240),(-100,0,-100,240),(-250,180,-100,180),(-250,-180,-250,120),(-250,-180,0,-180),(0,-180,0,0),(-100,0,0,0),(-100,60,150,60),(-50,60,-50,180),(0,120,0,300),(-100,-60,0,-60),(-100,-120,0,-120),(-200,-120,-200,180),(-150,-180,-150,120),(-300,-240,-150,-240),(-100,-240,200,-240),(50,-240,50,-180),(50,-180,300,-180),(0,-120,50,-120),(125,-120,125,60),(100,-120,150,-120),(200,-120,250,-120),(225,-120,225,120),(0,120,225,120),(200,240,200,300),(200,240,250,240),(50,240,150,240),(150,180,150,240),(50,180,250,180))
for i in d:
    draw(i)

    
#player
player=turtle.Turtle()
player.penup()
player.color("orange")
player.shape("circle")
player.speed(0)
player.setposition(230,-320)

#keyboard input function with wall rejection
def up():
    for i in d:
        if player.xcor() in range(int(i[0])-15,int(i[2])+15) and player.ycor() in range(int(i[1])-20,int(i[3])):
            return None
        elif player.xcor()in range(-250,-200) and player.ycor() > 300:
            print("YOU MADE IT!!")
            exit()
    return player.sety(player.ycor()+10)

def down():
    for i in d:
        global point
        if player.xcor() in range(int(i[0])-15,int(i[2])+15) and player.ycor() in range(int(i[1])-15,int(i[3])+23):
            return None
        elif player.xcor()in range(-250,-200) and player.ycor() > 300:
            print("YOU MADE IT!!")
            exit()
    return player.sety(player.ycor()-10)

def left():
    for i in d:
        global point
        if player.xcor() in range(int(i[0]),int(i[2])+23) and player.ycor() in range(int(i[1])-15,int(i[3])+15):
            return None
        elif player.xcor()in range(-250,-200) and player.ycor() > 300:
            print("YOU MADE IT!!")
            exit()
    return player.backward(10)

def right():
    for i in d:
        global point
        if player.xcor() in range(int(i[0])-25,int(i[2])) and player.ycor() in range(int(i[1])-15,int(i[3])+15):
            return None       
        elif player.xcor()in range(-250,-200) and player.ycor() > 300:
            print("YOU MADE IT!!")
            exit()
    return player.forward(10)



#keyboard input
wnd.onkey(up,"Up")
wnd.onkey(down,"Down")
wnd.onkey(left,"Left")
wnd.onkey(right,"Right")
wnd.listen()



#dogs input and gold input


while True:
    for j in range(8):
        dist = math.sqrt(math.pow(player.xcor()-dog[j].xcor(),2)+math.pow(player.ycor()-dog[j].ycor(),2))
        if(dist < 20):
            print("GAME OVER . YOU LOST ")
            exit()
        dog[j].forward(6)
        if (dog[j].xcor()< d2[j][0] or dog[j].xcor()> d2[j][2] or dog[j].ycor()< d2[j][1] or dog[j].ycor()> d2[j][3]):
            dog[j].right(180)

    for q in range(13):
        dist2 = math.sqrt(math.pow(player.xcor()-dog2[q].xcor(),2)+math.pow(player.ycor()-dog2[q].ycor(),2))
        if(dist2 < 20):
            print("GAME OVER . YOU LOST ")
            exit()
        dog2[q].sety(dog2[q].ycor()+5)
        if (dog2[q].xcor()< d3[q][0] or dog2[q].xcor()> d3[q][2] or dog2[q].ycor()< d3[q][1] or dog2[q].ycor()> d3[q][3]):
            dog2[q].sety(dog2[q].ycor()-(d3[q][3]-d3[q][1]))

    for g in range(22):
        dist3 = math.sqrt(math.pow(player.xcor()-gold[g].xcor(),2)+math.pow(player.ycor()-gold[g].ycor(),2))
        if(dist3 < 20):
            gold[g].hideturtle()
        




delay=raw_input("Press enter to finish")
