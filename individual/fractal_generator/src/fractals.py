
import turtle, helpers

#create function generate, get midpoint coords if needed and depth and length
def generate(t,depth,length,edge=True):
    t.speed(0)
    #if depth is one, create triangle and leave, alse generate edge
    #create triangle with turtle
    helpers.triangle(t,length)
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

#create function other fractal, get depth and length
def other_fractal(t,depth,length,edge=True):
    t.speed(0)
    t.pendown()
    #if first recursion, move to center
    if edge:
        t.teleport(-100,-100)
    #if depth is one, exit
    if depth==1:
        return
    helpers.square(t,length)
    #move to other corenr locations, call 4 times with length/3 and depth-1
    x,y=t.pos()
    if depth==2:
        t.teleport(-100,100)
        for i in range(4):
            t.forward(200)
            t.rt(90)
    t.teleport(x,y)
    other_fractal(t,depth-1,length/3,False)
    t.teleport(x+length*2/3,y)
    other_fractal(t,depth-1,length/3,False)
    t.teleport(x+length*2/3,y+length*2/3)
    other_fractal(t,depth-1,length/3,False)
    t.teleport(x,y+length*2/3)
    other_fractal(t,depth-1,length/3,False)