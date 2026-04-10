import tkinter

def main_screen():
    #create four functions to replace area with text and show run button, depending on button clicked
    def first():
        pass

    def second():
        pass

    def third():
        pass

    def fourth():
        pass
    
    #create destroy window function for run button
    def killl():
        pass

    #create window
    root=tkinter.Tk()
    root.title('Levi Morris - Programming Portfolio')
    root.geometry("500x700+500+100")
    #create elements, buttons, labels
    intro=tkinter.Message(root,text='Click on any project below to see project information; once you do so, you may run said project.\n\n\n\n\nProjects:',bd=10,width=500)
    intro.pack()
    intro.place(x=0,y=20)
    p1=tkinter.Button(root,text='Project 1',height=3,width=14,command=first)
    p1.pack()
    p1.place(x=92,y=200)
    p2=tkinter.Button(root,text='Project 2',height=3,width=14,command=second)
    p2.pack()
    p2.place(x=300,y=200)
    p3=tkinter.Button(root,text='Project 3',height=3,width=14,command=third)
    p3.pack()
    p3.place(x=92,y=300)
    p4=tkinter.Button(root,text='Project 4',height=3,width=14,command=fourth)
    p4.pack()
    p4.place(x=300,y=300)
    #run mainloop
    root.mainloop()
    #return the button that has been clicked
    pass

main_screen()