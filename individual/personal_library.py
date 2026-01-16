#LM 2nd Personal Library

#define add, getting LIB
def add(lib):
    #set TTL to user input for title
    ttl=input('What is the title of the book you would like to add? ')
    #set ATHR to user input for author
    athr=input('What is the author of the book you would like to add? ')
    #add list first TTL, second ATHR to LIB
    lib.append([ttl,athr])
    #return LIB
    return lib

#define srch, getting LIB
def srch(lib):
    nne=True
    chce=input('1. Seach by title\n2. Search by author\n')
    while chce not in ('1','2'):
        print('Invalid input. Try again.')
        chce=input('1. Seach by title\n2. Search by author\n')
    #if user wants to search by title:
    if chce=='1':
        #set TRM to user input title
        trm=input('Title: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if trm in book[0].lower():
                print(f'{book[0]} by {book[1]}')
                nne=False
    #Else if user wants to search by author:
    else:
        #set TRM to user input author
        trm=input('Author: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in second item of BOOK, display first and second items in BOOK
            if trm in book[1].lower():
                print(f'{book[0]} by {book[1]}')
                nne=False
    if nne: print('No results found.')


#define view, getting LIB
def view(lib):
    #loop through LIB as BOOK
    for book in lib:
        #display book item one(title) by book item two(author)
        print(f'{book[0]} by {book[1]}')
    if len(lib)==0:
        print('Your library is empty.')

#define rmv, getting LIB
def rmv(lib):
    chce=input('1. Seach by title\n2. Search by author\n')
    while chce not in ('1','2'):
        print('Invalid input. Try again.')
        chce=input('1. Seach by title\n2. Search by author\n')
    #if user wants to search by title:
    if chce=='1':
        none=True
        #set TRM to user input title
        trm=input('Title: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if trm in book[0].lower():
                print(f'{book[0]} by {book[1]}')
                none=False
                chce=input('Do you want to remove this book? (y/n) ').lower()
                while chce not in ('y','n'):
                    print('Invalid input. Try again.')
                    chce=input('Do you want to remove this book? (y/n) ').lower()
                #if user wants to remove BOOK
                if chce=='y':
                    #remove BOOK from LIB
                    lib.remove(book)
        if none: print('Nothing found.')
    #Else if user wants to search by author:
    else:
        none=True     
        #set TRM to user input author
        trm=input('Author: ').lower()
        #loop through LIB as BOOK
        for book in lib:
            #if TRM in first item of BOOK, display first and second items in BOOK
            if trm in book[1].lower():
                print(f'{book[0]} by {book[1]}')
                none=False
                chce=input('Do you want to remove this book? (y/n) ').lower()
                while chce not in ('y','n'):
                    print('Invalid input. Try again.')
                    chce=input('Do you want to remove this book? (y/n) ').lower()
                #if user wants to remove BOOK
                if chce=='y':
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
        opt=input('1. View\n2. Search\n3. Add\n4. Remove\n5. Exit\n')
        while opt not in ('1','2','3','4','5'):
            print('Invalid input. Try again')
            opt=input('1. View\n2. Search\n3. Add\n4. Remove\n5. Exit\n')
        #if input is exit, break out of loop
        if opt=='5':
            break
        #else, run appropriate function
        elif opt=='1':
            view(library)
        elif opt=='2':
            srch(library)
        elif opt=='3':
            add(library)
        elif opt=='4':
            rmv(library)

#run main function
main()