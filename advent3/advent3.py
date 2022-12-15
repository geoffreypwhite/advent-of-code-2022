
def partone() -> None:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0 
    with open('input3.txt','r',encoding='utf-8') as text:
        for i in text:
            f = len(i)
            print(str(f))

            h  = f // 2
            print(i[:h])
            print(i[h:])
            solved = False
            for j in range(h):
                letter = i[j:j+1]
                for k in range(h,f):
                    if i[k:k+1] == letter:
                        print(letter)
                        print(str(alphabet.index(letter)+1))
                        sum+= alphabet.index(letter) + 1
                        solved = True 
                        break
                if solved:break
    print(sum)

def parttwo() -> None:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    checklist:list[bool] = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    threechecklist:list[int] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sum = 0 
    threeCheck = 0
    with open('input3.txt','r',encoding='utf-8') as text:
        for i in text:
            i = i.replace(' ','')
            i = i.replace('\n','')
            for j in range(len(i)):
                # print(i[j:j+1])
                ind = alphabet.index(i[j:j+1])
                if not checklist[ind] :
                    threechecklist[ind]+=1
                    checklist[ind] = True
            threeCheck+=1
            if 0 == threeCheck % 3 :
                for q in range(len(threechecklist)):
                    if threechecklist[q]==3:
                        sum+= q + 1
                        break
                threechecklist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            checklist= [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    print(sum)


if __name__ == '__main__':
    parttwo()
