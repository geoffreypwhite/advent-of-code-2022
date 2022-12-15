def partone():
    with open('input2.txt','r',encoding='utf-8') as text:
        score:int = 0
        for i in text:
            if i[2:3:]=='X' :
                score+=1
                if i[0:1:]=='B':
                    score+=0
                elif i[0:1:]=='A':
                    score+=3
                else:
                    score+=6
            elif i[2:3:]=='Y' :
                score+=2
                if i[0:1:]=='B':
                    score+=3
                elif i[0:1:]=='A':
                    score+=6
                else:
                    score+=0
            elif i[2:3:]=='Z' :
                score+=3
                if i[0:1:]=='B':
                    score+=6
                elif i[0:1:]=='A':
                    score+=0
                else:
                    score+=3
        print(score)



def parttwo():
    with open('input2.txt','r',encoding='utf-8') as text:
        score:int = 0
        for i in text:
            if i[0:1]=='A': # they play rock
                if i[2:3]=='X' :
                    score+=3 # lose to rock with scissors
                elif i[2:3]=='Y':
                    score+=4 #draw to rock with rock
                elif i[2:3]=='Z':
                    score+=8 #win to rock with paper
            elif i[0:1]=='B': # they play scissors
                if i[2:3]=='X' :
                    score+=1 #lose to paper with rock
                elif i[2:3]=='Y':
                    score+=5 #draw to paper with paper
                elif i[2:3]=='Z':
                    score+=9 #win to paper with scissors
            elif i[0:1]=='C':
                if i[2:3]=='X' :
                    score+=2 # lose to scissors with paper
                elif i[2:3]=='Y':
                    score+=6 # draw to scissors with scissors
                elif i[2:3]=='Z':
                    score+=7 # win to scissors with rock
        print(score)


