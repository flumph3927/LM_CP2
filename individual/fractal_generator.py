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
def triangle(length):
    #create triangle side lengths length
    for i in range(3):
        turtle.forward(length)
        turtle.rt(120)

#create function generate, get midpoint coords if needed and depth and length
def generate(depth,length,total=6):
    turtle.speed(0)
    if total==6:
        for i in range(3):
            turtle.forward(length)
            turtle.lt(120)
    #if depth is one, create triangle and leave
    #create triangle with turtle
    else:
        triangle(length)
    if depth==1:
        return
    #call function generate on midpoint of triangles and depth-1 and length/2
    x,y=turtle.pos()
    if total==6:
        turtle.teleport(x+length/4,y+length*1.732/4)
        generate(depth-1,length/2,total-1)
    else:
        turtle.teleport(x+length/4,y+length*1.732/4)
        generate(depth-1,length/2,total-1)
        turtle.teleport(x-length/4,y-length*1.732/4)
        generate(depth-1,length/2,total-1)
        turtle.teleport(x+length*3/4,y-length*1.732/4)
        generate(depth-1,length/2,total-1)

def bckgrnd():
    choice=input('Choose background color:\n1.red\n2.blue\n3.green\n4.yellow\n5.purple\n6.orange\nAnything else for white\n')
    if choice==1: turtle.bgcolor('red')
    elif choice==2: turtle.bgcolor('blue')
    elif choice==3: turtle.bgcolor('green')
    elif choice==4: turtle.bgcolor('yellow')
    elif choice==5: turtle.bgcolor('purple')
    elif choice==6: turtle.bgcolor('orange')
    else: turtle.bgcolor('white')

#create function koch, get depth and length
    #
    #if depth is one, exit

#create function main
def main():
    #loop
    while True:
        #ask user to create fractal or exit
        choice=input('1. Create Sierpinski Triangle\n2. Exit\n')
        while choice not in ['1','2']:choice=input('1. Create Sierpinski Triangle\n2. Exit\n')
        #if create fractal: 
        if choice=='1':
            #set background to user input color
            bckgrnd()
            #run function generate on user input depth
            depth=input('File depth(1-6):')
        #if exit: break out of loop
        else: break

main()