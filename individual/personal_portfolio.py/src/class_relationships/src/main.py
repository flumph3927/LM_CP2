#main function file
import class_relationships.src.file_saves

#create function main
def main():
    #set BOOK to function amalgamate on function load on file path
    book=class_relationships.src.file_saves.amalgamate(class_relationships.src.file_saves.load('individual/class_relationships/docs/students.json'))
    #loop
    while True:
        #menu: add new student, add student grade, view student record, view all students, class statistics, exit
        choice=input('1. Add new student\n2. Add student grade\n3. View student record\n4. View all students\n5. Class statistics\n6. Class summary\n7. Exit\n')
        while choice not in [str(x+1) for x in range(7)]:
            print('Invalid input. Try again.')
            choice=input('1. Add new student\n2. Add student grade\n3. View student record\n4. View all students\n5. Class statistics\n6. Exit\n')
        #if add new student
        if choice=='1':
            #use BOOK add student method
            book.add_student()
        #else if add student grade
        elif choice=='2':
            #use BOOK add grade method
            book.add_grade()
        #else if view student record
        elif choice=='3':
            #use BOOK view records method
            book.view_records()
        #else if view all students
        elif choice=='4':
            #use BOOK string method
            print(book)
        #else if class statistics
        elif choice=='5':
            #use BOOK show stats method
            book.show_stats()
        elif choice=='6':
            book.summarize()
        #else
        else:
            #save
            class_relationships.src.file_saves.save(book,'individual/class_relationships/docs/students.json')
            #break ou of loop
            break