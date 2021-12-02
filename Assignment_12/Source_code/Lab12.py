###################################################################
##
## CS 101 Lab
## Program 12
## Name
## Email
##
## PROBLEM : 
##
## ALGORITHM : 
##      1. Import turtle module.
##      2.Defined point class. In the class it takes x, y, and color. It goes to x and y cordonates and then places dot.
##      3.Defined box class. Inherits the parameters of point class and adds parameters width and height. Draws a box starting at x and y location with the width and height entered.
##      4.Defined boxfilled class.  Inherits parameters of box class and adds fillcolor. Inherits box class box drawing but fills with color.
##      5.Defined circle class. Inherits the parameters of point class and adds parameter radius. Draws a circle starting at x,y cordonate and draws circle based on radius
##      6.Defined circlefilled class. Inherits parameters of circle class and adds fillcolor.  Draws a circle by inheriting from circle then fills with fillcolor.
##      7.Main code is an example of each class and its output.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import turtle

class point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        '''goes to loction and sets pen down as the color indicated'''
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        '''places a dot'''
        turtle.dot()
class box(point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)#inherits __init__ of point 
        self.width = width
        self.height = height
    def draw_action(self):
        '''draws a box'''
        for i in range(2):# run section twice to complete square
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
class boxfilled(box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)#inherits __init__ of box 
        self.fillcolor = fillcolor
    def draw_action(self):
        '''draws box and fills color'''
        turtle.color(self.color, self.fillcolor)
        turtle.begin_fill()
        box.draw_action(self)#draws box from box class
        turtle.end_fill()
class circle(point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)#inherits __init__ of point 
        self.radius = radius
    def draw_action(self):
        '''draws circle'''
        turtle.circle(self.radius)
class circlefilled(circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)#inherits __init__ of circle 
        self.fillcolor = fillcolor
    def draw_action(self):
        '''draws a filled circle'''
        turtle.color(self.color, self.fillcolor)
        turtle.begin_fill()
        circle.draw_action(self)#draws circle from circle class
        turtle.end_fill()


p = point(-100, 100, 'blue')#example of a point
p.draw()

b1= box(100,110, 50 ,40, 'red')#example of a box
b1.draw()

b= boxfilled( 1, 2, 100, 200, 'red', 'blue')#example of a filled box
b.draw()

c = circle( -20, -50, 10, 'yellow')#example of a circle
c.draw()

c1 = circlefilled(-40, -50, 5, 'green', 'blue')#example of a filled circle
c1.draw()


