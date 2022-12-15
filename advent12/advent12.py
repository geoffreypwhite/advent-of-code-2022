arr = []
with open('input.txt','r',encoding='utf-8') as r :
    for i in r:
        arr2 = []
        for j in i[:i.index('\n')]:
            arr2.append(j)
        arr.append(arr2)
coordinates = [20,55]
alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
markedArr = []
for i in arr :
    m=[]
    for j in i :
        m.append(False)
    markedArr.append(m)
def neighbors(coords:list[int]):
    ary:list[list[int]] = []
    if coords[0]!=0:
        ary.append([coords[0]-1,coords[1]])
    if coords[0]!=len(arr)-1:
        ary.append([coords[0]+1,coords[1]])
    if coords[1]!=0:
        ary.append([coords[0],coords[1]-1])
    if coords[1]!=len(arr[0])-1:
        ary.append([coords[0],coords[1]+1])
    return ary
min_list = []
curpath=0
for i in arr:
    mi = []
    for j in i:
        mi.append(-1)
    min_list.append(mi)
markQueue = [[20,55]]
while [20,0] != coordinates and arr[coordinates[0]][coordinates[1]] != 'a':
    markedArr[coordinates[0]][coordinates[1]] = True
    cur_level = arr[coordinates[0]][coordinates[1]]
    for i in neighbors(coordinates):
        if not markedArr[i[0]][i[1]] and (alphabet.index(cur_level) - alphabet.index(arr[i[0]][i[1]])<=1):
            markQueue.append(i)
            markedArr[i[0]][i[1]]=True
            min_list[i[0]][i[1]] = curpath + 1
    coordinate = markQueue.pop(0)
    coordinates = coordinate
    curpath=min_list[coordinates[0]][coordinates[1]]
print(min_list[coordinates[0]][coordinates[1]])
