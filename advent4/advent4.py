def partone():
    sum = 0 
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r:
            rangeOneX = int(i[:i.index('-')])
            rangeOneY = int(i[i.index('-')+1:i.index(',')])
            i=i[i.index(',')+1:]
            rangeTwoX = int(i[:i.index('-')])
            rangeTwoY = int(i[i.index('-')+1:i.index('\n')])
            if (rangeOneX <= rangeTwoX and rangeOneY >= rangeTwoY) or ( rangeTwoX <= rangeOneX and rangeTwoY >= rangeOneY ):
                sum+=1
    print(sum)

def parttwo():
    sum = 0 
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r:
            rangeOneX = int(i[:i.index('-')])
            rangeOneY = int(i[i.index('-')+1:i.index(',')])
            i=i[i.index(',')+1:]
            rangeTwoX = int(i[:i.index('-')])
            rangeTwoY = int(i[i.index('-')+1:i.index('\n')])
            if (rangeOneX <= rangeTwoX and rangeOneY >= rangeTwoY) or ( rangeTwoX <= rangeOneX and rangeTwoY >= rangeOneY ) or ( rangeOneX <= rangeTwoX and rangeOneY >= rangeTwoX  ) or ( rangeOneX <=rangeTwoY and rangeOneY >= rangeTwoY ):
                sum+=1
    print(sum)

if __name__ == '__main__' :
    parttwo()

