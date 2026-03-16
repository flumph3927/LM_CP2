#LM 2nd Classes Notes

#A class is a blueprint for an object, where you have pre-setup the structure of the object, used to create multiple objects with unique and specific details, while the class/blueprint remains the same

#classes use PascalCase

#ex:
class Animal:
    def __init__(self,name,species,age): 
        #init is always here, all methods always take in 'self'
        self.name=name.capitalize()
        self.species=species.capitalize()
        self.age=age

    def __str__(self): 
        #returns (must return) a string with the object's information for when prin(object) or such is called
        return f'NAME: {self.name}\nSPECIES: {self.species}\nAGE: {self.age}'
        
    def aging(self):
        self.age+=1




dog=Animal('Dog','dog',5)

print(dog)
dog.aging()
print(dog)



#NEW EXAMPLE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ClassPeriod:
    def __init__(self, subject, teacher, room = None):
        self.subject=subject.capitalize()
        self.teacher=teacher
        self.room=room

    def __str__(self):
        return f'{self.subject} is being taught by {self.teacher} in room {self.room}'
    
p1=ClassPeriod("CP2", 'Ms. LaRose', 200)
p2=ClassPeriod('Geography', 'Dr. Christensen', 217)
p3=ClassPeriod('English 9H', 'Ms. Thornock', 215)
p4=ClassPeriod('Advisory', 'Ms. Jensen', 216)
p6=ClassPeriod('Study Hall', 'Dr. Christensen', 217)
p7=ClassPeriod('CHEM 1010 CE', 'Mr. Johanson', 214)
p8=ClassPeriod('MATH 1050 CE', 'Ms. Cannon', 203)
p7=ClassPeriod('CHEM 1015 CE', 'Mr. Johanson', 214)


#to use a class on another page, you import the class like 'from classes import ClassName' or 'import classes' and use classes.ClassName()