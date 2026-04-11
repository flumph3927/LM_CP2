
import turtle

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
            set.getcanvas().postscript(file=path+'.eps', colormode='color')
            break
        except:
            print('Invalid path. Try again.')