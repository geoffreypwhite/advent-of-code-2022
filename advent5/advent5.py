



stackList: list[list[str]] = [['H','B','V','W','N','M','L','P'],['M','H','Q'],['N','D','B','G','F','Q','M','L'],['Z','T','F','Q','M','W','G'],[ 'M','T','H','P' ],[ 'C', 'B', 'M', 'J', 'D', 'H', 'G', 'T' ],[ 'M', 'N', 'B', 'F', 'V', 'R' ],[ 'P', 'L', 'H', 'M', 'R', 'G', 'S' ],[ 'P', 'D', 'B', 'C', 'N' ]] 

def partone():
    with open('input.txt','r',encoding='utf-8') as r:
        for i in r:
            if 'move' in i :
                amt = i.replace('move ','')[:i.replace('move ','').index(' ')]
                print(amt)
                source = i[i.index('from ')+5:i.index(' to')] 
                source = int(source)-1
                print(source)
                dest = i[i.index('to')+3].replace(' ','')
                dest = int(dest)-1
                for i in range(int(amt)):
                    stackList[dest].append(stackList[source].pop())


    for i in stackList:
        print(i[len(i)-1])



def parttwo():
    with open('input.txt','r',encoding='utf-8') as r:
        for i in r:
            if 'move' in i:
                amt = i.replace('move ','')[:i.replace('move ','').index(' ')]
                print(amt)
                source = i[i.index('from ')+5:i.index(' to')] 
                source = int(source)-1
                print(source)
                dest = i[i.index('to')+3].replace(' ','')
                dest = int(dest)-1
                holdList = []
                for i in range(int(amt)):
                    holdList.append(stackList[source].pop())
                for i in range(int(amt)):
                    stackList[dest].append(holdList.pop())
    for i in stackList:
        print(i[len(i)-1])

if __name__ == '__main__':
    parttwo()
