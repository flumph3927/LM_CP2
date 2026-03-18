#2d shape classes file
import turtle, math

#create class circ
class circ:
    #initialize, get radius and name
    def __init__(self,name):
        #set diameter, perimiter, radius, area, stretch, rotation, shifts and name
        while True:
            try:
                self.radius=int(input('Radius of the circle: '))
                if self.radius>0:
                    break
            except:
                print('Invalid input. Try again.')
        self.diameter=self.radius*2
        self.perimiter=self.radius*3.14159*2
        self.area=self.radius^2*3.14159
        self.stretch=1
        self.rotation=0
        self.shifts=[0,0]
        self.name=name

    #string method
    def __str__(self):
        #display all circle attributes
        return f'''Name: {self.name}
Type: {self.__class__.__name__}
Radius: {self.radius}
Area: {self.area}
Circumference: {self.perimiter}
Diameter: {self.diameter}
'''

    #draw method
    def draw(self):
        #imprt turtle
        #move to implement rotation and shifts
        turtle.teleport(self.shifts[0]*50, self.shifts[1]*50)
        turtle.lt(self.rotation)
        #draw circle with radius self radius and stretch
        turtle.circle(self.radius*50*self.stretch)
        #hold turtle screen
        turtle.done()

    #info method
    def info():
        #show formulas and explanation
        print('The formula for a circle\'s area is πr^2, with r being the radius.\n The formula for a circle\'s perimiter, or circumference, is 2πr, with r being the radius.\nThe formula for the diameter of a circle is 2r, with r being the radius.')


#create class rect
class rect:
    #initialize, get x, y and name
    def __init__(self,name):
        #set perimiter, x, y, area, stretch, rotation, shifts and name
        while True:
            try:
                self.x=int(input('Width of the rectangle: '))
                if self.x>0:
                    break
            except:
                print('Invalid input. Try again.')
        while True:
            try:
                self.y=int(input('Height of the rectangle: '))
                if self.y>0:
                    break
            except:
                print('Invalid input. Try again.')
        self.perimiter=self.x*2+self.y*2
        self.area=self.x*self.y
        self.stretch=1
        self.rotation=0
        self.shifts=[0,0]
        self.name=name

    #string method
    def __str__(self):
        #display all rect attributes
        return f'''Name: {self.name}
Type: {self.__class__.__name__}
Width: {self.x}
Height: {self.y}
Area: {self.area}
Perimeter: {self.perimiter}
'''

    #draw method
    def draw(self):
        #imprt turtle
        #move to implement rotation and shifts
        turtle.teleport(self.shifts[0]*50, self.shifts[1]*50)
        turtle.lt(self.rotation)
        #draw rect with side lengths x and y and stretch
        for i in range(2):
            turtle.forward(self.x*50)
            turtle.lt(90)
            turtle.forward(self.y*50)
            turtle.lt(90)
        #hold turtle screen
        turtle.done()

    #info method
    def info():
        #show formulas and explanation
        print('The formula for the area of a rectangle is lw, with l being lenth and w being width.\nThe formula for the perimiter of a rectangle is 2(l+w), with l being length and w  being width.')


#create class tri
class tri:
    #initialize, get b, h and name
    def __init__(self,name):
        #set perimiter, base, height, area, stretch, rotation, shifts and namewhile True:
        while True:
            try:
                self.a=int(input('Side A of the triangle: '))
                if self.a>0:
                    break
            except:
                print('Invalid input. Try again.')
        while True:
            try:
                self.b=int(input('Side B of the triangle: '))
                if self.b>0:
                    break
            except:
                print('Invalid input. Try again.')
        while True:
            try:
                self.c=int(input('Side C of the triangle: '))
                if self.c>0:
                    break
            except:
                print('Invalid input. Try again.')
        self.perimiter=self.a+self.b+self.c
        semi=self.perimiter/2
        self.area=math.sqrt(semi(semi-self.a)(semi-self.b)(semi-self.c))
        self.stretch=1
        self.rotation=0
        self.shifts=[0,0]
        self.name=name

    #string method
    def __str__(self):
        #display all triangle attributes
        return f'''Name: {self.name}
Type: {self.__class__.__name__}
Side A: {self.a}
Side B: {self.b}
Side C: {self.c}
Area: {self.area}
Perimeter: {self.perimiter}
'''

    #draw method
    def draw(self):
        #imprt turtle
        #move to implement rotation and shifts
        turtle.teleport(self.shifts[0]*50, self.shifts[1]*50)
        turtle.lt(self.rotation)
        #draw triangle with base base and height height and stretch
        turtle.forward(self.a*50)
        turtle.lt(math.acos((self.a^2+self.b^2-self.c^2)/2*self.a*self.b))
        turtle.forward(self.b*50)
        turtle.lt(math.acos((self.c^2+self.b^2-self.a^2)/2*self.c*self.b))
        turtle.forward(self.c*50)
        turtle.lt(math.acos((self.a^2+self.c^2-self.b^2)/2*self.a*self.c))
        #hold turtle screen
        turtle.done()

    #info method
        #show formulas and explanation


#create class square, subclass of rectangle
    #intialize, get sides
        #initialize class rect with same side lengths