'''from turtle import Turtle
#x=int(input("Enter length of star:"))
x=100
t=Turtle()

t.setheading(-80)

t.up()
t.goto(100,100)
t.width(50)
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
for i in range(5):
    t.down()
    t.forward(x)
    t.right(144)

t.end_fill()
print(t.position())
t.isdown()
t.screen.bgcolor('orange')
t.home()
t.screen.exitonclick()
x=t.screen.window_height()
y=t.screen.window_width()
'''

'''
from images import Image
image = Image(300,300)
b=(0,0,255)
y=150//2
for x in range(150):
    image.setPixel(x,y-1,b)
    image.setPixel(x,y+1,b)
    image.setPixel(x,y,b)
    

image.draw()
 '''
'''
from images import Image
i=Image(150,150)
for x in range(i.getWidth()):
    for y in range(i.getWidth()):
        i.setPixel(x,y,(255,0,0))
i.draw() '''

from images import Image

i=Image('myth.gif')
j=Image(i.getWidth(),i.getHeight())
for x in range(i.getWidth()):
    for y in range(i.getHeight()):
            j.setPixel(x,y,i.getPixel(x,y))

def bw():
    for x in range(j.getWidth()):
         for y in range(j.getHeight()):
            r,g,b=j.getPixel(x,y)
            avg=(r+g+b)//3
            if avg<127:
                 j.setPixel(x,y,(0,0,0))
            else:
                 j.setPixel(x,y,(255,255,255))

def greyscale():
     for x in range(j.getWidth()):
        for y in range(j.getHeight()):
            r,g,b=j.getPixel(x,y)
            r=r*.299
            g*=.587
            b*=.114
            color=int(r+g+b)
            j.setPixel(x,y,(color,color,color))
def avg(triple):
    a,b,c=triple
    a=(a+b+c)//3
    return a
def blur():
     for x in range(1,j.getWidth()-1):
        for y in range(1,j.getHeight()-1):
            a=avg(j.getPixel(x+1,y))

            b=avg(j.getPixel(x-1,y))
            c=avg(j.getPixel(x,y-1))
            d=avg(j.getPixel(x,y+1))
            aver=(a+b+c+d)//4
            j.setPixel(x,y,(aver,aver,aver))
blur()
j.draw()