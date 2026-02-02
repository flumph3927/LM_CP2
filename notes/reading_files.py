#LM 2nd Reading Files Notes
import csv

'''
#how to open file without crashing: (notic erelative path)
try:
    with open("notes/files_read.txt","r") as file:
        content=file.read()
except:
    print('problem time. be angry.')
else:
    print(content)

#how to open file without crashing: (notice relative path)
try:
    with open("notes/files_read.txt","r") as file:
        for line in file:
            print(line.strip())
except:
    print('problem time. be angry.')
else: pass
'''

#csv time
try:
    with open("notes/sample_csv.csv", mode='r') as casava: #becaues why not
        content=csv.reader(casava)
        headers=next(content)
        rows=[]
        for i in content:
            print(f'{i[0]}: {i[1]}')
            rows.append({headers[0]:i[0],headers[1]:i:[1]})
except:
    print('problems')
else:
    pass