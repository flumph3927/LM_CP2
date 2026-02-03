#LM 2nd Movie Recommender

#create function display movie, get MOVIE
    #display movie informtion cleaned up

#create function setup, get PATH
    #open file at PATH
    #read from file and set STUFF to file information in lists of lists
    #return STUFF

#create function show all, get ALL
    #loop through ALL as MOVIE
        #call function display movie on MOVIE

#create function genre, get POSS and TYP
    #set RESULTS to empty list
    #set TERM to valid user input
    #loop through POSS as MOVIE
        #if any of MOVIE accessed at TYP are TERM
            #add MOVIE to RESULTS
    #return RESULTS

#create function movie length
    #set RESULTS to empty list
    #set LENT to list, two items, valid user inputs for min and max length
    #loop through LENT, if item is empty string, set to 0 or arbitrarily large number (max or min)
    #loop through POSS as MOVIE
        #if MOVIE length is between first and last of LENT
            #add MOVIE to RESULTS
    #return RESULTS

#crea