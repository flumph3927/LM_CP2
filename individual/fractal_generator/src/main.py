#LM 1st Fractal Pattern Generator

import turtle

#create function midpoints, get end1,end2,end3
def midpoints(x,y,z):
    out=[]
    #get midpoint coords of trangle with corners ends
    for i in [x,y]:
        out.append([(i[0]+z[0])/2,(i[1]+z[1])/2])
        if i==x:out.append([(i[0]+y[0])/2,(i[1]+y[1])/2])
    #return midpoints
    return out

#create function triangle, get length
def triangle(t,length):
    #create triangle side lengths length
    for i in range(3):
        t.forward(length)
        t.rt(120)

#create function square, get length
def square(t,length):
    #create square side lengths length
    for i in range(4):
        t.forward(length)
        t.lt(90)

#create function generate, get midpoint coords if needed and depth and length
def generate(t,depth,length,edge=True):
    t.speed(0)
    #if depth is one, create triangle and leave, alse generate edge
    #create triangle with turtle
    triangle(t,length)
    if depth==1:
        t.teleport(-100,(-1.732/2))
        for i in range(3):
            t.forward(200)
            t.lt(120)
        return
    #call function generate on midpoint of triangles and depth-1 and length/2
    #Do this three times at appropriate positions, special case for start
    if edge:
        t.teleport(-100,(-1.732/2))
        x,y=t.pos()
        t.teleport(x+length/4,y+length*1.732/4)
        generate(t,depth-1,length/2,False)
    else:
        x,y=t.pos()
        t.teleport(x+length/4,y+length*1.732/4)
        generate(t,depth-1,length/2,False)
        t.teleport(x-length/4,y-length*1.732/4)
        generate(t,depth-1,length/2,False)
        t.teleport(x+length*3/4,y-length*1.732/4)
        generate(t,depth-1,length/2,False)

#create function background
def bckgrnd():
    #user select background color, change to user select
    choice=input('Choose background color:\n1.red\n2.blue\n3.green\n4.yellow\n5.purple\n6.orange\nAnything else for white\n')
    if choice=='1': return 'red'
    elif choice=='2': return 'blue'
    elif choice=='3': return 'green'
    elif choice=='4': return 'yellow'
    elif choice=='5': return 'purple'
    elif choice=='6': return 'orange'
    else: return 'white'

#create function save image
def save_image(scrn):
    #get valid filename, save as eps file
    while True:
        path=input('Filepath to save to(do not include filename extension): ')
        try:
            set=turtle.getscreen()
            set.bgcolor(scrn.bgcolor())
            set.getcanvas().postscript(file=path+'.eps')
            break
        except:
            print('Invalid path. Try again.')

#create function other fractal, get depth and length
def other_fractal(t,depth,length,edge=True):
    t.speed(0.0000000001)
    t.pendown()
    #if first recursion, move to center
    if edge:
        t.teleport(-100,-100)
        square(t,length)
    #if depth is one, exit
    if depth==1:
        return
    square(t,length)
    #move to other corenr locations, call 4 times with length/3 and depth-1
    x,y=t.pos()
    other_fractal(t,depth-1,length/3,False)
    t.teleport(x+length*2/3,y)
    other_fractal(t,depth-1,length/3,False)
    t.teleport(x+length*2/3,y+length*2/3)
    other_fractal(t,depth-1,length/3,False)
    t.teleport(x,y+length*2/3)
    other_fractal(t,depth-1,length/3,False)

#create function main
def main():
    #loop
    while True:
        #ask user to create fractal or exit
        choice=input('1. Create Sierpinski Triangle\n2. Create Unnamed Fractal\n3. Exit\n')
        while choice not in ['1','2','3']:choice=input('1. Create Sierpinski Triangle\n2. Create Unnamed Fractal\n3. Exit\n')
        #if create fractal 1: 
        if choice=='1':
            t=turtle.Turtle()
            scrn=turtle.Screen()
            scrn.clearscreen()
            scrn.setup(800,600)
            #set background to user input color
            scrn.bgcolor(bckgrnd())
            #run function generate on user input depth
            depth=input('File depth(1-6): ')
            while depth not in [str(x+1) for x in range(6)]:
                print('Invalid input. Try again.')
                depth=input('File depth(1-6):')
            generate(t,int(depth),200)
            if input('S to save as image: ').lower()=='s':
                save_image()
        #repeat creat fractal one but for fractal 2
        elif choice=='2':
            t=turtle.Turtle()
            scrn=turtle.Screen()
            scrn.clearscreen()
            scrn.setup(800,600)
            #set background to user input color
            scrn.bgcolor(bckgrnd())
            #run function generate on user input depth
            depth=input('File depth(1-6): ')
            while depth not in [str(x+1) for x in range(6)]:
                print('Invalid input. Try again.')
                depth=input('File depth(1-6):')
            other_fractal(t,int(depth),200)
            if input('S to save as image: ').lower()=='s':
                save_image()
        #if exit: break out of loop
        else: break

main()