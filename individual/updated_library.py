#LM 1st update personal library
import csv

#define add, getting LIB
def add(lib):
    #set TTL to user input for title
    title=input('What is the title of the book you would like to add? ')
    #set ATHR to user input for author
    author=input('What is the author of the book you would like to add? ')
    while True:
        try:
            year=int(input('What year was the book you would like to add created? '))
            break
        except:
            print('Invalid input. Try again.')
    genre=input('What genre is the book you would like to add? ')
    #add list first TTL, second ATHR to LIB
    lib.append({'Title':title,'Author':author,'Year':year,'Genre':genre})
    #return LIB
    return lib

#define srch, getting LIB
def search(lib):
    choice=input('1. Search by title\n2. Search by author\n')
    while choice not in ('1','2'):
        print('Invalid input. Try again.')
        choice=input('1. Search by title\n2. Search by author\n')
    #if user wants to search by title:
    results=[]
    total=1
    if choice=='1':
        #set TRM to user input title
        term=input('Title: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if term in book['Title'].lower():
                print(f'{total}. {book['Title']} by {book['Author']}')
                results.append(book)
                total+=1
    #Else if user wants to search by author:
    else:
        #set TRM to user input author
        term=input('Author: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in second item of BOOK, display first and second items in BOOK
            if term in book['Author'].lower():
                print(f'{total}. {book['Title']} by {book['Author']}')
                results.append(book)
                total+=1
    if total==1:
        print('No results found.')
    else:
        choice=input('Enter the number corresponding to a book to see more details, anything else to return to menu. ')
        for i in range(len(results)):
            if choice==str(i+1):
                view_book(results[i])

#create function view book, get BOOK
def view_book(book):
    #display all BOOK information
    print(f'Title: {book['Title']}\nAuthor: {book['Author']}\nYear: {book['Year']}\nGenre: {book['Genre']}')

#define view, getting LIB
def view(lib):
    #loop through LIB as BOOK
    for book in lib:
        #display book item one(title) by book item two(author)
        print(f'{book['Title']} by {book['Author']}')
    if len(lib)==0:
        print('Your library is empty.')

#define rmv, getting LIB
def remove(lib):
    choice=input('1. Seach by title\n2. Search by author\n')
    while choice not in ('1','2'):
        print('Invalid input. Try again.')
        choice=input('1. Seach by title\n2. Search by author\n')
    #if user wants to search by title:
    if choice=='1':
        none=True
        #set TRM to user input title
        term=input('Title: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if term in book['Title'].lower():
                print(f'{book['Title']} by {book['Author']}')
                none=False
                choice=input('Do you want to remove this book? (y/n) ').lower()
                while choice not in ('y','n'):
                    print('Invalid input. Try again.')
                    choice=input('Do you want to remove this book? (y/n) ').lower()
                #if user wants to remove BOOK
                if choice=='y':
                    #remove BOOK from LIB
                    lib.remove(book)
        if none: print('Nothing found.')
    #Else if user wants to search by author:
    else:
        none=True     
        #set TRM to user input author
        term=input('Author: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if term in book['Author'].lower():
                print(f'{book['Title']} by {book['Author']}')
                none=False
                choice=input('Do you want to remove this book? (y/n) ').lower()
                while choice not in ('y','n'):
                    print('Invalid input. Try again.')
                    choice=input('Do you want to remove this book? (y/n) ').lower()
                #if user wants to remove BOOK
                if choice=='y':
                    #remove BOOK from LIB
                    lib.remove(book)
        if none: print('Nothing found.')

#create function get from, get PATH
def get_from(path):
    #open file at PATH
    stuff=[]
    with open(path,mode='r') as lib:
    #get information form file as list of dictionaries
        content=csv.DictReader(lib)
        for i in content:
            stuff.append(i)
    #return information
    return stuff

#create function save, get PATH and LIB
def save_to(path,lib):
    #open file at path
    with open(path, mode='w') as sav:
    #save LIB to file at path
        writer=csv.DictWriter(sav,fieldnames=['Title','Author','Year','Genre'])
        writer.writeheader()
        writer.writerows(lib)

#def main
def main():
    #set LIBRARY to empty list
    library=get_from('individual\\library_file.csv')
    #loop
    while True:
        #get user input on which option(view,search,add,remove,exit)
        option=input('1. View\n2. Search\n3. Add\n4. Remove\n5. Exit\n')
        while option not in ('1','2','3','4','5'):
            print('Invalid input. Try again')
            option=input('1. View\n2. Search\n3. Add\n4. Remove\n5. Exit\n')
        #if input is exit, break out of loop
        if option=='5':

            break
        #else, run appropriate function
        elif option=='1':
            view(library)
        elif option=='2':
            search(library)
        elif option=='3':
            add(library)
        elif option=='4':
            remove(library)

#run main function
main()