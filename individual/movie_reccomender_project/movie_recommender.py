#LM 2nd Movie Recommender
import csv

#create function display movie, get MOVIE
def display_movie(movies):
    while True:
    #ask user for title of movie to view
        title=input('What is the full title of the movie?').lower()
    #find movie with that title
    #display movie informtion cleaned up
    print(f'\nTitle: {movie[0]}. \nDirector: {movie[1]}. \nGenre: {movie[2]}. \nRating: {movie[3]}. \nLength: {movie[4]} minutes. \nNotable Actors: {movie[5]}.')

#create function show simple, get MOVIE
def show_simple(movie):
    #display simple movie information cleaned up
    print(f'Title: {movie[0]}. Genre: {movie[2]}. Rating: {movie[3]}.')

#create function setup, get PATH
def setup(path):
    try:
    #open file at PATH
        with open(path,"r") as fil:
    #read from file and set STUFF to file information in lists of lists
            content=csv.reader(fil)
            next(content)
            stuff=[]
            for i in content:
                stuff.append(i)
    except:
        print('Corrupt file. Program terminating.')
    #return STUFF
    return stuff

#create function show all, get ALL
def show_all(all):
    #loop through ALL as MOVIE
    for movie in all:
        #call function display movie on MOVIE
        show_simple(movie)

#create function all but length, get POSS and TYP
def all_but_length(poss,typ):
    #set RESULTS to empty list
    results=[]
    #set TERM to valid user input
    term=input(' ').lower()
    #loop through POSS as MOVIE
    for movie in poss:
        #if any of MOVIE accessed at TYP are TERM
        if term in movie[typ].lower():
            #add MOVIE to RESULTS
            results.append(movie)
    #return RESULTS
    return results

#create function movie length, get poss
def movie_length(poss):
    #set RESULTS to empty list
    results=[]
    #set LENT to list, two items, valid user inputs for min and max length
    lent=[]
    while True:
        try:
            lengt=input('What is the minimum movie length?(enter for none) ')
            if lengt=='':
                lengt=0
            lengt=int(lengt)
            break
        except:
            print('Invalid input. Try again.')
    lent.append(lengt)
    while True:
        try:
            lengt=input('What is the maximum movie length?(enter for none) ')
            if lengt=='':
                lengt=9999999999999999999999999999999999999999999
            lengt=int(lengt)
            if lengt<lent[0]:
                int('string') #causes intentional error
            break
        except:
            print('Invalid input. Try again.')
    lent.append(lengt)
    #loop through LENT, if item is empty string, set to 0 or arbitrarily large number (max or min)
    #loop through POSS as MOVIE
    for movie in poss:
        #if MOVIE length is between first and last of LENT
        if int(movie[4])<lent[1] and int(movie[4])>lent[0]:
            #add MOVIE to RESULTS
            results.append(movie)
    #return RESULTS
    return results

#create function get results, get OPTIONS and MOVIES
def get_results(options, movies):
    #set POSS to MOVIES
    poss=movies
    #if 1 in OPTIONS
    if '1' in options:
        print('Search genre:', end='')
        #set POSS to function all but length run on POSS and 2
        poss=all_but_length(poss,2)
    #if 2 in OPTIONS
    if '2' in options:
        print('Search director:', end='')
        #set POSS to function all but length run on POSS and 1
        poss=all_but_length(poss,1)
    #if 3 in OPTIONS
    if '3' in options:
        print('Search notable actors:', end='')
        #set POSS to function all but length run on POSS and 5
        poss=all_but_length(poss,5)
    #if 4 in OPTIONS
    if '4' in options:
        #set poss to function movie length run on POSS
        poss=movie_length(poss)
    #return POSS
    return poss

#create function main
def main():
    #set MOVIES to function setup run on file path
    movies=setup("individual/movie_reccomender_project/Movies list.csv")
    print('--------------Movie Recommender--------------')
    #loop
    while True:
        #ask user if they want to show all, exit, or search
        choice=input('\n\n\n\n\n\n\n1. Show all\n2. Search movies\n3. Exit\n')
        while choice not in ['1','2','3',]:
            print('Invalid input. Try again.')
            choice=input('1. Show all\n2. Search movies\n3. Exit\n')
        #if show all, run function show all on MOVIES
        if choice=='1': show_all(movies)
        #if search
        elif choice=='2':
            #set PAS to empty string
            pas=''
            #ask user if they want to do options, add corresonding number string to PAS (for all options)
            if input('Would you like to search by genre?(Y/anything else) ').lower()=='y': pas+='1'
            if input('Would you like to search by director?(Y/anything else) ').lower()=='y': pas+='2'
            if input('Would you like to search by notable actors?(Y/anything else) ').lower()=='y': pas+='3'
            if input('Would you like to search by length?(Y/anything else) ').lower()=='y': pas+='4'
            #display results (using display movie) of call function get results on PAS and MOVIES
            found=get_results(pas,movies)
            show_all(found)
            if input('Would you like to view specific movie?(Y/anything else) ').lower=='y':
                pass
        #if exit, break out of loop
        elif choice=='3':
            break

#call function main
main()