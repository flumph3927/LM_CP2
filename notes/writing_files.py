#LM CP2 Writing to Files Notes
'''
with open("notes\\files_write.txt", 'r+') as fil:
    content = fil.read()
    fil.write('\nHi')
    '''

import csv,string,random
'''
with open('notes/sample_csv.csv', 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow('')
'''
with open('notes/sample_csv.csv', 'r+', newline='') as casava:
    reade=csv.reader(casava)
    for lin in reade:
        print(lin)
    writer = csv.writer(casava)
    for i in range(16):
        writer.writerow([''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8)),''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8))])