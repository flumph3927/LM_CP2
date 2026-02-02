#LM 1st Personal Library

#define add, getting LIB
def add(lib):
    #set TTL to user input for title
    title=input('What is the title of the book you would like to add? ')
    #set ATHR to user input for author
    author=input('What is the author of the book you would like to add? ')
    #add list first TTL, second ATHR to LIB
    lib.append((title,author))
    #return LIB
    return lib

#define srch, getting LIB
def search(lib):
    none=True
    choice=input('1. Seach by title\n2. Search by author\n')
    while choice not in ('1','2'):
        print('Invalid input. Try again.')
        choice=input('1. Seach by title\n2. Search by author\n')
    #if user wants to search by title:
    if choice=='1':
        #set TRM to user input title
        term=input('Title: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if term in book[0].lower():
                print(f'{book[0]} by {book[1]}')
                none=False
    #Else if user wants to search by author:
    else:
        #set TRM to user input author
        term=input('Author: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in second item of BOOK, display first and second items in BOOK
            if term in book[1].lower():
                print(f'{book[0]} by {book[1]}')
                none=False
    if none: print('No results found.')


#define view, getting LIB
def view(lib):
    #loop through LIB as BOOK
    for book in lib:
        #display book item one(title) by book item two(author)
        print(f'{book[0]} by {book[1]}')
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
            if term in book[0].lower():
                print(f'{book[0]} by {book[1]}')
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
            if term in book[1].lower():
                print(f'{book[0]} by {book[1]}')
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

#def main
def main():
    #set LIBRARY to empty list
    library=[]
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