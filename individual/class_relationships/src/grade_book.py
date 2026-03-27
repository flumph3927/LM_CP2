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
    def add_student(self,grades={}):
        #get student id until student id does not match any other student id
        id=input('Student ID:')
        while True:
            try:
                id=int(id)
                if id 
        name=input('Studnet name: ')
        #create student class from this, add to self students
        self.students[id]=student.Student(id,name,grades)

    def dictify(self):
        out={}
        for i in list(self.students.values()):
            out[i.id]=i.dictify()
        
    #create method add grade
    def add_grade(self):
        #get valid grade, percent, and student id user inputs
        while True:
            id=input('Student\'s ID: ')
            try: id=int(id)
            except: print('Invalid input. Try again.')
            if id in list(self.students.keys()):break
            else:
                print('Invalid input. Try again.')
        name=input('Assignment Name(if not unique will replace): ')
        grade=input('Grade: ')
        while True:
            try:
                grade=int(grade)
                if not grade>=0 or not grade<=100:
                    int('hi')
                break
            except:
                print('Invalid input. Try again.')
                grade=input('Grade: ')
        #add to correct student's grades dict
        self.students[id].grades[name]=grade

    #create method view records
    def view_records(self):
        #get valid user input for student id
        while True:
            id=input('Student\'s ID: ')
            try: id=int(id)
            except: print('Invalid input. Try again.')
            if id in list(self.students.keys()):
                break
            else:
                print('Invalid input. Try again.')
        #display that student's records and academic standing
        print(self.students[id])

    #create method show stats
    def show_stats(self):
        grades=[]
        for i in self.students:
            if i.grades=={}:
                grades.append('No grade')
            else:
                grades.append(sum(list(i.grades.values()))/len(i.grades))
        #get avg grade
        avg=sum(grades)/len(grades)
        # get best grade
        best=max(grades)
        # get worst grade
        worst=min(grades)
        #get number of students
        num=len(self.students)
        #display information
        print(f'Total students: {num}\nAverage grade: {avg}\nBest grade: {best}\nWorst grade: {worst}')
