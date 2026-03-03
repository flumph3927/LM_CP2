#LM 1st Fractal Pattern Generator

import turtle, fractals, screen_background

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
            scrn.bgcolor(screen_background.bckgrnd())
            #run function generate on user input depth
            depth=input('File depth(1-6): ')
            while depth not in [str(x+1) for x in range(6)]:
                print('Invalid input. Try again.')
                depth=input('File depth(1-6):')
            turtle.tracer(0,0)
            fractals.generate(t,int(depth),200)
            turtle.update()
            if input('S to save as image: ').lower()=='s':
                screen_background.save_image(scrn)
        #repeat creat fractal one but for fractal 2
        elif choice=='2':
            t=turtle.Turtle()
            scrn=turtle.Screen()
            scrn.clearscreen()
            scrn.setup(800,600)
            #set background to user input color
            scrn.bgcolor(screen_background.bckgrnd())
            #run function generate on user input depth
            depth=input('File depth(1-5): ')
            while depth not in [str(x+1) for x in range(5)]:
                print('Invalid input. Try again.')
                depth=input('File depth(1-6):')
            turtle.tracer(0,0)
            fractals.other_fractal(t,int(depth)+1,200)
            turtle.update()
            if input('S to save as image: ').lower()=='s':
                screen_background.save_image(scrn)
        #if exit: break out of loop
        else: break

main()