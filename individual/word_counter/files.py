#LM 1st Word Counter

#create function get words, get file path
def get_words(path):
    #open file to read
    with open(path, 'r') as file:
        content=file.read()
    #get information from file
    #split into list of words
    words=content.split()
    #return length of list of words
    return len(words)

#create function add info, get time and file path, word count
def add_info(path,time,count):
    #open file to write
    with open(path, 'a') as file:
        file.write(f'\nWord Count: {count}\nTime: {time}\n\n')
    #write word count and time to file

#create function write line, get file path
def write_line(path):
    #get user input for line
    line=input('Line to write: ')
    #open file to write
    with open(path, 'a') as file:
    #write line to file
        file.write(line+'\n')

#create function reading, get file path
def readin(path):
    #open file to read
    with open(path,'r') as file:
        #display lines in order
        content=file.read()
    print(content)

#try to open, if fail, create.
def tests(path):
    with open(path, 'a'):
        pass
