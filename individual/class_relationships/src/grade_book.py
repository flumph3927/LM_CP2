#grade book class file
import student

#create class GradeBook
class GradeBook:
    #create method init, get students
    def __init__(self,students):
        #set self students to students
        self.students=students

    #create method string
    def __str__(self):
        out='ID    | Name     | Grade | Standing'
        #loop thourhg students
        for i in self.students:
            #call student method string
            out+='\n'+i
        return out

    #create method add student
    def add_student(self):
        #get student id until student id does not match any other student id
        id=input('Student ID:')
        while id in list(self.students.keys()) or len(id)!=5:
            print('Invalid ID. Try Again. (tip: ID must be 5 digits and cannot already exist)')
            id=input('Student ID:')
        #create student class from this, add to self students
        self.students[id]=student.Student(id)

    #create method add grade
        #get valid grade, percent, and student id user inputs
        #add to correct student's grades dict

    #create method view records
        #get valid user input for student id
        #display that student's records and academic standing

    #create method show stats
        #loop through students
            #use this to get avg grade, best grade, and worst grade
        #get number of students
        #display information
