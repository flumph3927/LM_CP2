#file saving functions
import json, grade_book, student

#create function save, get class and path
def save(clas,path):
    with open(path,'w') as fle:
    #call dictify method of class, save to path as JSON
        json.dump(clas.dictify(),fle)

#create function load, get path
def load(path):
    #load from json at path, return dictionary
    with open(path,'r') as fle:
        stuff=json.load(fle)
    return stuff

#create function amalgamate, get dict
def amalgamate(dikt):
    #assemble dict into classes correctly
    students={}
    for i in dikt:
        students[int(i)]=student.Student(i,dikt[i][0],dikt[i][1],dikt[i][2])
    return grade_book.GradeBook(students)