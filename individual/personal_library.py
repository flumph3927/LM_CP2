#LM 2nd Personal Library

#set LIBRARY to empty list

#define add, getting LIB
    #set TTL to user input for title
    #set ATHR to user input for author
    #add list first TTL, second ATHR to LIB
    #set LIB to a listed setted version of LIB(removes duplicates)
    #return LIB

#define srch, getting LIB
    #if user wants to search by title:
        #set TRM to user input title
        #loop through LIB as BOOK
            #if TRM in first item of BOOK, display first and second items in BOOK
    #Else if user wants to search by author:
        #set TRM to user input author
        #loop through LIB as BOOK
            #if TRM in second item of BOOK, display first and second items in BOOK

