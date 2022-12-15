ary = []
for i in range(1000) : 
    row = []
    for j in range(600):
        row.append('.')
    ary.append(row)


def drop_sand():
    x = 500 
    y = 0 
    try:
        while ary[x][y+1] not in  'o#' or ary[x+1][y+1] not in 'o#' or ary[x-1][y+1] not in 'o#':
            if ary[x][y]=='.':ary[x][y]='~'
            if ary[x][y+1] not in 'o#' :
                y+=1
            elif ary[x-1][y+1] not in 'o#': 
                y+=1
                x-=1
            elif ary[x+1][y+1] not in 'o#':
                x+=1
                y+=1
             


        ary[x][y]='o'
        return True
    except:
        return False




def line(coord_1,coord_2):
    if coord_1[0] == coord_2[0]:
        if coord_1[1] < coord_2[1]:
            for i in range(coord_1[1],coord_2[1]+1): 
                ary[coord_1[0]][i] = '#'
        else:
            for i in range(coord_2[1],coord_1[1]+1): 
                ary[coord_1[0]][i] = '#'
            
    elif coord_1[1] == coord_2[1]:
        if coord_1[0]<coord_2[0]:
            for i in range(coord_1[0],coord_2[0] + 1 ):
                ary[i][coord_1[1]] = '#'
        else:
            for i in range(coord_2[0],coord_1[0] + 1):
                ary[i][coord_1[1]] = '#'


paths = []

with open('input.txt','r',encoding='utf-8') as r :
    for i in r :
        path = i 
        pathary = []
        while '->' in path :
            c_1 = path[:path.index(' ')]
            c_1_x = int(c_1[:c_1.index(',')])
            c_1_y = int(c_1[c_1.index(',')+1:])
            path = path[path.index('> ')+2:]
            pathary.append([c_1_x,c_1_y])
            # print(c_1)
        
        c_1 = path
        c_1_x = int(c_1[:c_1.index(',')])
        c_1_y = int(c_1[c_1.index(',')+1:])
        pathary.append([c_1_x,c_1_y])
        paths.append(pathary)
            
        # print(pathary)
        


for i in paths:
    for j in range(1,len(i)):
        coord_1 = i[j-1]
        coord_2 = i[j]
        line(coord_1,coord_2)


start = [500,0]
s=0
while drop_sand() :
    s+=1
    # print(s)
# print(ary)

number = 0
for i in range(len(ary)):
    for j in range(len(ary[i])):
        if ary[i][j] == 'o':
            number+=1
            # print(str(i) + ',' + str(j))
            # print (number)
print(s)


max = 0
for i in ary :
    for j in range(len(i)):
        if i[j]=='#' and j > max :
            max=j

for i in ary :
    i[max+2] = '#'


while ary[500][0]!='o':
    drop_sand()

s=0
for i in ary :
    for j in i[:max+2] :
        if j == 'o':
            s+=1
            # print(s)
print(s)
