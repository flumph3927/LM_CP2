'''#parent class
class Vehicle:
    def __init__(self, model, brand):
        self.brand=brand
        self.model=model
        
    def move(self):
        print('MOVE!')

#child class
class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print('Sail')
        
        
car=Boat('Mustang','Ford')
print(car.brand,car.model)
car.move()'''

class Library:
    def __init__(self,name,catalog=[]):
        self.name=name
        self.catalog=catalog
        
    def add(self,book):
        self.catalog.append(book)
    
    def remove(self,book):
        if book in self.catalog: self.catalog.pop(book)
    def view_cat(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f'{self.title} by {self.author}'
    
lib=Library('Provo Library')

lib.add(Book('The Lord of the Rings','J. R. R. Tolkien'))
lib.add(Book('The Silmarillion','J. R. R. Tolkien'))
lib.add(Book('The Sunlit Man','Brandon Sanderson'))

lib.view_cat()

