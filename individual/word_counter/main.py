#LM 1st Word Counter
import times, files

#create function main
def main():
    #get file path, and pass to all functons later, as user input
    path=input('Enter the exact file path for your document: ')
    #loop
    while True:
        #ask user if they want to write to document, view, add timestamp/word count, or exit
        choice=input('\n1. Add content\n2. View content\n3. Add word count and timestamp\n4. Exit\n')
        while choice not in ['1','2','3','4']:
            print('Invalid input. Try again.')
            choice=input('\n1. Add content\n2. View content\n3. Add word count and timestamp\n4. Exit\n')
        #if user write to:
        if choice=='1':
            #call write line
            files.write_line(path)
            #while user wnats to continue writing
            while input('\nY to continue writing lines, anything else to exit.').lower()=='y':
                #call write line
                files.write_line(path)
        #if user view
        elif choice=='2':
            #call reading
            files.readin(path)
        #if user add timestamp, etc.
        elif choice=='3':
            words=files.get_words(path)
            #display word count using function call get words
            print(f'Word count: {words}')
            #call function add info on function call get time and word count
            files.add_info(path,times.get_time(),words)
        #if exit
        else:
            #break out of loop
            break

main()