#3d shape classes
import math

#create class cube
class cube:
    #initialize, get side
    def __init__(self,name):
        #set volume, surface area, side, stretch, rotation, shifts, name
        while True:
            try:
                self.x=int(input('Side length of the cube: '))
                if self.x>0:
                    break
            except:
                print('Invalid input. Try again.')
        self.volume=self.x^3
        self.surface=6*self.x^2
        self.name=name

    #string method
    def __str__(self):
        #display cube attributes
        return f'''Name: {self.name}
Type: {self.__class__.__name__}
Side Length: {self.x}
Volume: {self.volume}
Surface Area: {self.surface}
'''

    #draw method
    def draw():
        #say 3d shapes cannot be drawn
        print('3d shapes cannot be drawn.')

    #info method
    def info():
        #show formulas and explanation
        print('The formula for the volume of a cube is a^3, with a being the side length. The formula for the surface area of a cube is 6a^2, with a being the side length.')


#create class cylinder
class cyl:
    #initialize, get h, radius
    def __init__(self,name):
        #set volume, surface area, top radius, height, stretch, rotation, shifts, name
        while True:
            try:
                self.top=int(input('Radius of the top circle: '))
                if self.top>0:
                    break
            except:
                print('Invalid input. Try again.')
        while True:
            try:
                self.height=int(input('Height of the cylinder: '))
                if self.height>0:
                    break
            except:
                print('Invalid input. Try again.')
        self.volume=self.height*self.top^2*3.14159
        self.surface=self.radius*2*3.14159*self.height+2*self.radius^2*3.14159
        self.name=name

    #string method
    def __str__(self):
        #display cylinder attributes
        return f'''Name: {self.name}
Type: {self.__class__.__name__}
Top Radius: {self.top}
Height: {self.height}
Volume: {self.volume}
Surface Area: {self.surface}
'''

    #draw method
    def draw():
        #say 3d shapes cannot be drawn
        print('3d shapes cannot be drawn.')


    #info method
    def info():
        #show formulas and explanation
        print('The formula for the volume of a cylinder is πhr^2, with r being the top radius and h being the height.\nThe formula for the surface area of a cylinder is 2πrh+2πr^2, where r is the top radius and h is the height.')


#create class tetrahedron
class tetra:
    #initialize, get side
    def __init__(self,name):
        #set volume, surface area, side, stretch, rotation, shifts, name
        while True:
            try:
                self.side=int(input('Side length of the tetrahedron: '))
                if self.side>0:
                    break
            except:
                print('Invalid input. Try again.')
        self.volume=self.side^3/(6*math.sqrt(2))
        self.surface=math.sqrt(3)*self.side^2
        self.name=name

    #string method
    def __str__(self):
        #display d4 attributes
        return f'''Name: {self.name}
Type: {self.__class__.__name__}
Side Length: {self.side}
Volume: {self.volume}
Surface Area: {self.surface}
'''

    #draw method
    def draw():
        #say 3d shapes cannot be drawn
        print('3d shapes cannot be drawn.')

    #info method
    def info():
        #show formulas and explanation
        print('The formula for the volume of a tetrahedron is a^3/(6*2^(1/2)), with a being the side length.\nThe formula for the surface area of a tetrahedron is a^2*3^(1/2), with a being the side length.')