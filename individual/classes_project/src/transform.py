#transformations functions

#create transform menu function, get shape
def transforms(shape):
    #check if shape is 2d
    #get transformation,transformation value, and and transform
    try:
        sfghsfijofbisiof=shape.area
        trans=input('1. Shift\n2. Rotate\n3. Scale\n')
        while trans not in ['1','2','3']:
            print('Invalid Input. Try Again.')
            trans=input('1. Shift\n2. Rotate\n3. Scale\n')
        if trans=='1':
            x=input('What horizontal shift would you like to add? ')
            y=input('What vertical shift would you like to add? ')
            while True:
                try:
                    x=int(x)
                    y=int(y)
                    break
                except:
                    print('Invalid inputs. Try again.')
                    x=input('What horizontal shift would you like to add? ')
                    y=input('What vertical shift would you like to add? ')
            shape=shifter([x,y],shape)
        elif trans=='2':
            degs=input('What rotation would you like to add? ')
            while True:
                try:
                    degs=int(degs)
                    break
                except:
                    print('Invalid input. Try again.')
                    degs=input('What rotation would you like to add? ')
            shape=rotate(degs,shape)
        else:
            scle=input('What scale factor would you like to add? ')
            while True:
                try:
                    scle=int(scle)
                    break
                except:
                    print('Invalid input. Try again.')
                    scle=input('What scale factor would you like to add? ')
            shape=scale(scle,shape)
    except:
        print('3d shapes cannot be transformed')
    return shape

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