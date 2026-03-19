#transformations functions

#create add rotation function, get rotation and class
def rotate(rotation,clas):
    #set class rotation to rotation
    clas.rotation=rotation
    return clas

#create add scale function, get scale and class
def scale(scale,clas):
    #set class scale to scale
    clas.stretch=scale
    return clas

#create add shifts function, get shifts([x,y]) and class
def shifter(shifts,clas):
    #set class shift x to shift x
    clas.shifts[0]=shifts[0]
    #set class shift y to shift y
    clas.shifts[1]=shifts[1]
    return clas