import tkinter

root=tkinter.Tk()

root.title('TEXT TITLE')
root.configure(background='blue')
root.minsize(500,500)
root.maxsize(1000,1000)
root.geometry('300x300+100+100')
label=tkinter.Label(root,text='COOL TEXT',font=('Times New Roman',14,'bold'))
label.config(fg='green',background='cyan')
label.pack()
#image=tkinter.PhotoImage(file='individual/classes_project/docs/running.png')
#tkinter.Label(root,image=image).pack()

#button time
root.count=0
def add():
    root.count+=1
    tkinter.Label(root,text=root.count).pack()

btn=tkinter.Button(root,text='MORE NUMBER',command=add)
btn.pack()

root.mainloop()