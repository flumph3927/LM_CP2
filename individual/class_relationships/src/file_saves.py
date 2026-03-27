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
def amalgamate(dict):
    #assemble dict into classes correctly
    students={}
    for i in list(dict.values()):
        students[list(i.keys())[0]]=student.student(list(i.keys())[0],i[list(i.keys())[0]][0],i[list(i.keys())[0]][0])
    return grade_book.GradeBook(students)