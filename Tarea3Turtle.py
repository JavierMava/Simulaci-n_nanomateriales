import turtle
import random


'Color'

def randomcolor():
    r=random.random()*0.75
    g=random.random()*0.75
    b=random.random()*0.75
    turtle.color(r,g,b)

'Particula'
def pa (s):
    total = 0
    for _ in range (s):
        a = int(random.random() * 360)
        d = (20)
        turtle.lt(a)
        turtle.fd(d)
        total = total=+d
    return total



def sim (p,s):
    for _ in range (p):
        turtle.up()
        turtle.home()
        turtle.down()
        randomcolor()
        print (pa(s))

def main():    
    turtle.setup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0)
    randomcolor()

    print (pa(2))

    sim(20,50)
    turtle.done()

main()
