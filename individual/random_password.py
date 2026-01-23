#LM 1st random password generator

#create function uppercase, get AMOUNT
    #set OUT to empty list
    #loop AMOUNT times
        #add randomly chosen uppercase number to OUT

#create function lowercase, get AMOUNT
    #set OUT to empty list
    #loop AMOUNT times
        #add randomly chosen lowercase number to OUT

#create function number, get AMOUNT
    #set OUT to empty list
    #loop AMOUNT times
        #add randomly chosen number to OUT

#create function special, get AMOUNT
    #set OUT to empty list
    #loop amount times
        #add randomly chosen special character to OUT

#create function distribute, get LENGTH and CHOSEN
    #create dictionary, 4 items, keys upper, lower, number, special, values all 0
    #loop LENGTH minus length of CHOSEN times
        #randomly choose from CHOSEN list, add 1 to appropriate item in dictionary
    #add 1 to all items in dictionary that correspond with items in CHOSEN

#create function main
    #display welcome to the random password generator
    #loop
        #