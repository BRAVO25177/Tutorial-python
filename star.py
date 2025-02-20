from turtle import Turtle

num = int(input("Enter the number of stars: "))
length = int(input("Enter the length of the sides of the star: "))
radius = 2 * length
t = Turtle()
t.speed(1)

angle = 360 / num
for i in range(num):
    t.up()
    current_angle = i * angle
    t.right(current_angle)
    t.forward(radius)
    t.left(current_angle)
    t.down()
    
    t.down()
    t.right(72)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(72)
    
    t.up()
    t.home()