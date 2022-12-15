
s:str
# with open(input(),'r',encoding='utf-8') as r:
    # s = r.readline()

s = input()

print(s)

one:str = ''
two:str = ''
three:str = ''
four:str = ''

def unique() -> bool:
    if (one == two or one == three or one ==four or two == three or two == four or three == four) or (one == '' or two == '' or three == '' or four == ''):
        return False
    return True



for i in range(len(s)):
    
        four = three 
        three = two 
        two = one 
        one = s[i:i+1]
        print (i)
        if unique():
            print(one)
            print(two)
            print(three)
            print(four)
            break

def uniquefourteen(s:str):
    ar = []
    for i in range (len(s)):
        try:
            if ar.index(s[i:i+1]) > -1:
                return False
        except: 
            None
        ar.append(s[i:i+1])
    return True



for i in range(len(s)-14):
    string = s[i:i+14]
    if uniquefourteen(string):
        print(i+14)
        if uniquefourteen(string):
            break


