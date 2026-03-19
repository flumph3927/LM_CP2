#comparison functions file

#create function choice, get opt and objedcts
def choice(opt,objects):
    #if opt is one, return  object with larger area
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
def sort(opt,objects):
    try:
    #if opt is one, return objects reordered by area
        if opt==1:
            return dict(sorted(objects,key=lambda s: s[1].area,reverse=True))
    #else, return objects reordered by perimeter
        else:
            return dict(sorted(objects,key=lambda s: s[1].perimeter,reverse=True))
    #for 3d:
    except:
        if opt==1:
            return dict(sorted(objects,key=lambda s: s[1].volume,reverse=True))
        else:
            return dict(sorted(objects,key=lambda s: s[1].surface,reverse=True))

#create function select, get objects
def select(objects):
    #loop through and show all objects
    for i,v in enumerate(objects):
        print(f'{i+1}: {v[1]}\n\n')
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
    return objects.values(choice-1)