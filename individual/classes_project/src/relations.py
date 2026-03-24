#comparison functions file

#create function view shapes, get shapes
def view(shapes):
    #loop through shapes
    for i,(k,v) in enumerate(shapes.items()):
    #display shapes with assosciated number
        print(f'{i+1}: {v}\n\n')

#create function choice, get opt and objedcts
def choice(objects):
    #if opt is one, return  object with larger area
    opt=input('1. Compare area/volume\n2. Compare perimiter/surface area\n')
    while opt not in ['1','2']:
        print('Invalid Input. Try Again.')
        opt=input('1. Compare area/volume\n2. Compare perimiter/surface area\n')
    opt=int(opt)
    try:
        if opt==1:
            if objects[0].area>objects[1].area:
                return objects[0]
            else:return objects[1]
    #else, return object with larger perimeter
        else:
            if objects[0].perimeter>objects[1].perimeter:
                return objects[0]
            else:return objects[1]
    except:
        #for 3d
        if opt==1:
            if objects[0].volume>objects[1].volume:
                return objects[0]
            else:return objects[1]
        else:
            if objects[0].surface>objects[1].surface:
                return objects[0]
            else:return objects[1]

#create function sort, get opt, objects
def sort(objects):
    opt=input('1. Sort by area/volume\n2. Sort by perimiter/surface area\n')
    while opt not in ['1','2']:
        print('Invalid Input. Try Again.')
        opt=input('1. Sort by area/volume\n2. Sort by perimiter/surface area\n')
    opt=int(opt)
    try:
    #if opt is one, return objects reordered by area
        if opt==1:
            return dict(sorted(objects.items(),key=lambda s: s[1].area,reverse=True))
    #else, return objects reordered by perimeter
        else:
            return dict(sorted(objects.items(),key=lambda s: s[1].perimeter,reverse=True))
    #for 3d:
    except:
        if opt==1:
            return dict(sorted(objects.items(),key=lambda s: s[1].volume,reverse=True))
        else:
            return dict(sorted(objects.items(),key=lambda s: s[1].surface,reverse=True))

#create function select, get objects
def select(objects):
    #loop through and show all objects
    view(objects)
    #return selected object
    while True:
        try:
            choice=int(input('Which shape would you like to select? '))
            if choice in [x+1 for x in range(len(objects))]:
                break
            else:
                int('hi')
        except:
            print('Invalid Input. Try again.')
    return objects[list(objects.keys())[choice-1]]