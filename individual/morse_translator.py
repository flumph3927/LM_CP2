#LM 2nd Simple Morse Code Translator

#create function change, get IN, OUT and MESSAGE
def change(inn,out,message,sep=1):
    #set DONE to empty string
    done=''
    #for CHAR in MESSAGE
    for char in message:
        #if CHAR is in IN
        if char in inn:
            #add OUT at index of CHAR in IN to DONE
            done+=out[inn.index(char)]
        #else
        else:
            #add CHAR to DONE
            done+=char
        done+=' '*sep
    #return done
    return done

#create function prepare, get MESSAGE
def prepare(message):
    #set PT1 to MESSAGE split at 3 spaces
    pt1=message.split('   ')
    #set PT2 to first of PT1 split at spaces, plus space, plus next part of part 1 split at spaces, etc.
    pt2=[]
    for i in pt1:
        pt2+=i.split()
        pt2+=' '
    #return PT2
    return pt2

#create function main
def main():
    print('Welcome to the Morse Code Translator.')
    #set ALPHA and MORSE to lists of letters/codes in alphabetical order
    alpha=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
    morse=('.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','   ')
    #loop
    while True:
        #ask user if they want to go englih tomorse, morse to english, or exit
        choice=input('1. English to Morse\n2. Morse to English\n3. Exit\n')
        #if user chooses english to morse
        if choice=='1':
            #run function change on ALPHA, MORSE, and user input message
            print('Your translated message is:',change(alpha,morse,input('What is the message to be translated? ').lower()))
        #else if user chooses morse to english
        elif choice=='2':
            #run function change on MORSE, ALPHA, and user input message
            print('Your translated message is:',change(morse,alpha,prepare(input('What is the message to be translated? ').lower()),sep=0))
        #else if user chooses exit
        elif choice=='3':
            #break out of loop
            break
        else:
            print('Invalid input. Try again.')

#call function main
main()