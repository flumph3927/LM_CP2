#student class file


#create class Student
class Student:
    #create method init, get student ID
    def __init__(self,id,name,grades,age):
        #get user input for name 
        self.name=name
        #set these to self vars
        self.id=id
        #set empty grade dict
        self.grades=grades
        self.age=age

    #create method string
    def __str__(self):
        if self.grades=={}:
            grade='No grade'
            standing='Unknown standing'
        else:
            grade=sum(list(self.grades.values()))/len(self.grades)
            if grade>=90:
                standing='Honor Roll'
            elif grade>=80:
                standing='Good Standing'
            else:
                standing='Needs Improvement'
            grade=str(grade)+'%'
        #return student informations(no grade is possible)
        return f'{self.id}: {self.name} | {self.age}th Grade | {grade} - {standing}'

    #create method dictify
    def dictify(self):
        #turn student information into dict, return this
        return [self.name,self.grades,self.age]
    
    def full(self):
        if self.grades=={}:
            grade='No grade'
            standing='Unknown standing'
        else:
            grade=sum(list(self.grades.values()))/len(self.grades)
            if grade>=90:
                standing='Honor Roll'
            elif grade>=80:
                standing='Good Standing'
            else:
                standing='Needs Improvement'
            grade=str(grade)+'%'
        print(f'Name: {self.name}\nStudent ID: {self.id}\n{self.age}th Grade\nOverall Grade: {grade}\nAcademic Standing: {standing}\nAssignments:')
        for i in self.grades:
            print(f'{i}: {self.grades[i]}')