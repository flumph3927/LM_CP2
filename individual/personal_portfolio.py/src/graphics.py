import tkinter

def main_screen():
    #create four functions to replace area with text and show run button, depending on button clicked
    #will show description of project, and create run button which runs said projett
    def first():
        root.exp.config(text='This project creates either a serpinski triangle fractal or an unnamed square fractal using the python module turtle.\nWhat I learned:\n - Recursive functions\nChallenges:\n - Understanding exactly what was happening so I could troubleshoot')
        run=tkinter.Button(root,text='Run',command=lambda: killl(1))
        run.pack()
        run.place(x=230,y=600)

    def second():
        root.exp.config(text='A program used to create select geometric shapes and find their information. It can draw some shapes and make comparisons between them.\nWhat I learned:\n - Classes\nChallenges:\n - Drawing a triangle accurately based on side length only (Heron\'s Formula)')
        run=tkinter.Button(root,text='Run',command=lambda: killl(2))
        run.pack()
        run.place(x=230,y=600)

    def third():
        root.exp.config(text='A class manager that allows you to manage student grades and see class summaries and statistics.\nWhat I learned:\n - Class Relationships\nChallenges:\n - Saving and loading classes indirectly while retaining all information.')
        run=tkinter.Button(root,text='Run',command=lambda: killl(3))
        run.pack()
        run.place(x=230,y=600)

    def fourth():
        root.exp.config(text='A project that allows you to view a list of movies and search through it. It allows searching by runtime, notable actors, director, and genre.\nWhat I learned:\n - Saving with CSV\nChallenges:\n - Integrating similar functions together for modularity.')
        run=tkinter.Button(root,text='Run',command=lambda: killl(4))
        run.pack()
        run.place(x=230,y=600)
    
    #create destroy window function for run button
    #destroys window so project runs
    def killl(button):
        root.destroy()
        root.button=button

    #create window
    root=tkinter.Tk()
    root.title('Levi Morris - Programming Portfolio')
    root.geometry("500x700+500+100")
    #create elements, buttons, labels
    #top introduction part
    intro=tkinter.Message(root,text='Click on any project below to see project information. Once you do so, you may run said project. Once you have run said project, you will return to this screen.\n\n\n\n\nProjects:',bd=10,width=500)
    intro.pack()
    intro.place(x=0,y=20)
    #four buttons for the project, uses commands above
    p1=tkinter.Button(root,text='Project 1:\nFractal Generator',height=3,width=16,command=first)
    p1.pack()
    p1.place(x=92,y=200)
    p2=tkinter.Button(root,text='Project 2:\nGeometry Calculator',height=3,width=16,command=second)
    p2.pack()
    p2.place(x=300,y=200)
    p3=tkinter.Button(root,text='Project 3:\nGrade Book',height=3,width=16,command=third)
    p3.pack()
    p3.place(x=92,y=300)
    p4=tkinter.Button(root,text='Project 4\nMovie Recommender',height=3,width=16,command=fourth)
    p4.pack()
    p4.place(x=300,y=300)
    #create basic nonshown description box.
    #will be used later to show project description
    #refrenced earlier
    root.exp=tkinter.Message(root,bd=10,width=480)
    root.exp.pack()
    root.exp.place(x=0,y=400)
    #run mainloop
    root.mainloop()
    #return the button that has been clicked
    return root.button
