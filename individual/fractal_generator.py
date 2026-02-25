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
    #create triangle side lengths length

#create function generate, get midpoint coords if needed and depth and length
def generate(depth,length,mids=[]):
    #if depth is one, create triangle and leave
    #create triangle with turtle
    pass
    #call function generate on midpoint of triangles and depth-1 and length/2

#create function koch, get depth and length
    #
    #if depth is one, exit

#create function main
    #loop
        #ask user to create fractal or exit
        #if create fractal: 
            #set background to user input color
            #run function generate on user input depth
        #if exit: break out of loop