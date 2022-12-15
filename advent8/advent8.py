
def visible(x:int,y:int,trees) -> bool:
    up:bool = True
    down:bool = True
    left:bool = True
    right:bool = True
    value:int = trees[x][y]
    print(value)
    # if x == 0 or y == 0 or x ==len(trees) or y == len(trees[0]):
    #     return True
    for i in range(x)[::-1]:
        valuecheck = int(trees[i][y]) 
        print(valuecheck)
        if valuecheck >=value:
            up = False
            print( 'up is false' )
            break
    for i in range(x+1,len(trees[0])):
        valuecheck = int(trees[i][y])
        if valuecheck >=value:
            down = False
            print( 'down is false' )
            break
    for i in range(y)[::-1]:
        valuecheck = int(trees[x][i])
        if valuecheck >=value :
            left = False
            print( 'left is false' )
            break
    for i in range(y+1,len(trees)):
        valuecheck = int(trees[x][i])
        if valuecheck >=value :
            right = False
            print( 'right is false' )
            break

    print('f')
    return (up or down or left or right)

def scenicscore(x,y,trees):
    left = 0 
    right = 0 
    up = 0 
    down = 0 
    if x == 0 or y == 0 or x == len(trees)-1 or y ==len(trees[0]) -1 :
        return 0
    for i in range(x)[::-1]:
        left += 1
        if trees[i][y] >=trees[x][y]:
            break
    for i in range(x+1,len(trees[0])):
        right+= 1
        if trees[i][y] >=trees[x][y]:
            break
    for i in range(y)[::-1]:
        down += 1
        if trees[x][i] >=trees[x][y]:
            break
    for i in range(y+1,len(trees)):
        up += 1
        if trees[x][i]  >= trees[x][y]:
            break
    return up * down * left * right

def main():
    trees = [[]]

    with open('input.txt','r',encoding='utf-8') as r :
        index = 0
        for i in r:
            string = []
            for j in range(len(i)):
                if '\n' not in i[j:j+1]:
                    string.append(int(i[j:j+1]))
            trees.append(string)

            index+=1

    trees.pop(0)
    print(trees[0])
    sum = 0 
    for i in range (len(trees)):
        for j in range(len(trees[0])):
            print ( str(i) + ' ' + str(j) )
            vis = visible(i,j,trees)
            print(vis)
            if vis:
                sum+=1
    
    print(trees)
    print(sum)
    scores = [] 
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            scores.append(scenicscore(i,j,trees))
    highest = scores[0]
    for i in scores :
        if i > highest :
            highest = i
    print(highest)


if __name__ == '__main__':
    main()
