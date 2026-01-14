import random

z=60
y=40
mp=[]
for i in range(y):
    mp.append([])
    for x in range(z):
        mp[i].append([''])

dne=False
while not dne:
    tle=[random.randint(0,(y-1)),random.randint(0,(z-1))]
    if mp[tle[0]][tle[1]][0]=='':
        ps=['~','#']
        for j in [[tle[0],tle[1]+1],[tle[0]-1,tle[1]],[tle[0]+1,tle[1]],[tle[0],tle[1]-1]]:
            if j[0]<(y-1) and j[0]>-1 and j[1]>-1 and j[1]<(z-1):
                if mp[j[0]][j[1]][0] != '':
                    for i in range(100):
                        ps.append(mp[j[0]][j[1]][0])
        while mp[tle[0]][tle[1]][0] == '':
            mp[tle[0]][tle[1]][0]=random.choice(ps)
    dne=True
    for i in mp:
        for x in i:
            if x[0] == '':
                dne=False

for i in range(100):
    dne=False
    while not dne:
        for i in range(y):
            for x in range(z):
                tle=[i,x]
                ps=[]
                for j in [[tle[0],tle[1]+1],[tle[0]-1,tle[1]],[tle[0]+1,tle[1]],[tle[0],tle[1]-1]]:
                    if not j[0]<y:
                        j[0]-=y
                    if not j[1]<z:
                        j[1]-=z
                    for a in range(10):
                        ps.append(mp[j[0]][j[1]][0])
                for b in range(100):
                    ps.append(mp[i][x][0])
                mp[tle[0]][tle[1]][0]=random.choice(ps)
        dne=True
        for i in mp:
            for x in i:
                if x[0] == '':
                    dne=False

for i in range(1):
    dne=False
    while not dne:
        for i in range(y):
            for x in range(z):
                if mp[i][x][0]!='~':
                    tle=[i,x]
                    mp[i][x].append(['-','^','+','&','%','!','*'])
                    ps=['-','^','+','&','%','!','*']
                    for j in [[tle[0],tle[1]+1],[tle[0]-1,tle[1]],[tle[0]+1,tle[1]],[tle[0],tle[1]-1]]:
                        if not j[0]<y:
                            j[0]-=y
                        if not j[1]<z:
                            j[1]-=z
                        for a in range(100):
                            if mp[j[0]][j[1]][0] not in ['~','#']:
                                ps.append(mp[j[0]][j[1]][0])
                    for b in range(100):
                        ps.append(mp[i][x][0])
                    mp[tle[0]][tle[1]][0]=random.choice(ps)
        dne=True
        for i in mp:
            for x in i:
                if x[0] == '#':
                    dne=False

for i in range(1500):
    dne=False
    while not dne:
        for i in range(y):
            for x in range(z):
                if mp[i][x][0]!='~':
                    tle=[i,x]
                    ps=mp[i][x][1]
                    for j in [[tle[0],tle[1]+1],[tle[0]-1,tle[1]],[tle[0]+1,tle[1]],[tle[0],tle[1]-1]]:
                        if not j[0]<y:
                            j[0]-=y
                        if not j[1]<z:
                            j[1]-=z
                        for a in range(100):
                            if mp[j[0]][j[1]][0]!='~':
                                ps.append(mp[j[0]][j[1]][0])
                    for b in range(100):
                        ps.append(mp[i][x][0])
                    mp[tle[0]][tle[1]][0]=random.choice(ps)
                    mp[i][x][1].append(mp[i][x][0])
        dne=True
        for i in mp:
            for x in i:
                if x[0] == '':
                    dne=False

    mappp=''
    mapp=''
    cds={'~':'\033[104m','-':'\033[43m','^':'\033[1m\033[47m','+':'\033[102m','&':'\33[45m','%':'\33[40m','!':'\33[41m','*':'\33[46m','#':''}
    for i in mp:
        for x in i:
            mapp+=(cds[x[0]]+' '+x[0]+' '+'\033[00m')
        mapp+='\n'
    print(mapp,end='\n')