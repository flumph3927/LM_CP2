#LM 1st random password generator
import string, random

#create function get_chars, get AMOUNT and choices list
def get_chars(amount,sett):
    #set OUT to empty list
    out=[]
    #loop AMOUNT times
    for i in range(amount):
        #add randomly chosen character to OUT
        out.append(random.choice(sett))
    #return OUT
    return out

#create function assemble, get CHARS
def assemble(chars):
    #set OUT to empty string
    out=''
    #until CHARS is empty, randomly choose from CHARS, add to OUT, remove from CHARS
    while chars != []:
        char=random.choice(chars)
        out+=char
        chars.remove(char)
    #return OUT
    return out

#create function distribute, get LENGTH and CHOSEN
def distribute(length, chosen):
    #create dictionary, 4 items, keys upper, lower, number, special, values all 0
    options={'up':0,'low':0,'num':0,'punc':0}
    #loop LENGTH minus length of CHOSEN times
    for i in range(length-len(chosen)):
        #randomly choose from CHOSEN list, add 1 to appropriate item in dictionary
        options[random.choice(chosen)]+=1
    #add 1 to all items in dictionary that correspond with items in CHOSEN
    for x in chosen:
        options[x]+=1
    #run functions on number in corresponding dictionary value
    out=[]
    out+=get_chars(options['up'],string.ascii_uppercase)
    out+=get_chars(options['low'],string.ascii_lowercase)
    out+=get_chars(options['num'],string.digits)
    out+=get_chars(options['punc'],string.punctuation)
    return out

#create function main
def main():
    #display welcome to the random password generator
    print('Welcome to the random password generator.')
    #loop
    while True:
        #ask user if they would like to exit, if they do, break loop
        if input('Q to exit, anything else to continue. ').lower()=='q': break
        #ask user for length of password
        long=input('How long would you like your password to be? ')
        while True:
            try:
                long=int(long)
                break
            except:
                print('Invalid. Try again')
                long=input('How long would you like your password to be? ')
        #ask user which types they would like to include
        types=[]
        if input('I to include uppercase letters, anything else to exclude. ').lower()=='i': types.append('up')
        if input('I to include lowercase letters, anything else to exclude. ').lower()=='i': types.append('low')
        if input('I to include numbers, anything else to exclude. ').lower()=='i': types.append('num')
        if input('I to include special characters, anything else to exclude. ').lower()=='i': types.append('punc')
        #run function assemble on function distribute on length of password and list of types four times
        passwords=[]
        for i in range(4):
            passwords.append(assemble(distribute(long,types)))
        #display the 4 generated passwords
        print(f'Passwords:\n\n1. {passwords[0]}\n\n2. {passwords[1]}\n\n3. {passwords[2]}\n\n4. {passwords[3]}\n\n')

#call main
main()