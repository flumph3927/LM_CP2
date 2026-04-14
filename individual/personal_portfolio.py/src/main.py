import graphics,runs

#create main function
def main():
    #loop
    while True:
            #use run on main_screen function
        try:
            runs.run(graphics.main_screen())
        except:
            #if window closed, break loop
            break

#call main
main()