import turtle
turtlePen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("light yellow")
def polygon(n, size=80):
    if n > 2:                          
        angle = 360/n                  
        for n in range(0, n):         
            turtlePen.left(angle)
            turtlePen.forward(size)
def polygon2(n, size=80):
    if n > 2:                          
        angle = 360/n                  
        for n in range(0, n):         
            turtlePen.right(angle)
            turtlePen.forward(size)
turtlePen.color("purple")
polygon(3)
polygon(4)
polygon(5)
polygon(6)
turtlePen.color("light yellow")
polygon(4)
polygon(3)
turtlePen.color("purple")
polygon(3)
polygon(4)
turtlePen.color("light yellow")
polygon(3)
polygon(4)
polygon(5)
polygon(6)
window.mainloop() 
