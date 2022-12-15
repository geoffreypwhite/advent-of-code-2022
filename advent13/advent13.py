def compareLeftListToRightInteger(list:list,integer:int):
    right_list = [integer]
    if compareTwoLists(list,right_list) == None: return None
    if compareTwoLists(list,right_list) == True : return True
    if compareTwoLists(list,right_list) == False : return False
def compareRightListToLeftInteger(list:list,integer:int):
    left_list = [integer]
    if compareTwoLists(left_list,list) == True : return True
    elif compareTwoLists(left_list,list) == False: return False
    elif compareTwoLists(left_list,list) == None : return None

def compareTwoLists(left_list,right_list):
    # if len(left_list)>len(right_list) : return False
    # if len(left_list) < len(right_list) : return True
    # if len(left_list)==0 and len(right_list)>0: return True 
    for i in range(min(len(left_list),len(right_list))):
        left = left_list[i]
        right = right_list[i]
        if '[' in str(left) and '[' in str(right):
            twolist = compareTwoLists(left,right)
            if twolist == True : return True 
            elif twolist == False : return False
        elif '[' in str(right) :
            twolist = compareRightListToLeftInteger(right,left)
            if twolist==False : return False
            elif twolist == True : return True
        elif  '[' in str(left):
            twolist = compareLeftListToRightInteger(left,right)
            if twolist==False : return False
            elif twolist == True : return True
        elif left<right :
           return True
        elif left>right : 
            return False
    if len(right_list) < len(left_list): return False
    if len(right_list) > len(left_list): return True
    return None





def main() :
    ary = []

    with open('input.txt','r',encoding='utf-8') as r :
        for i in r :
            lists = []
            one = []
            two = []
            bracket_count = 0
            cur_list = one
            prev_list = one
            cur_value = ''
            if len(i)>1:
                for j in i[:i.index('\n')]:
                    if '[' in j :
                        new_list = []
                        cur_list.append(new_list)
                        lists.append(prev_list)
                        prev_list = cur_list
                        cur_list = new_list
                        cur_value=''
                        bracket_count+=1
                    elif ']' in j :
                        if cur_value != '' : cur_list.append(int(cur_value))
                        cur_list = prev_list
                        prev_list = lists.pop()
                        cur_value=''
                    elif ',' in j :
                        if cur_value!='': cur_list.append(int(cur_value))
                        cur_value = ''
                    else:
                        cur_value+=j
                ary.append(one)
    sum = 0 
    for i in range (0,len(ary)-1,2):
        one = ary[i][0]
        two = ary[i+1][0]
        if compareTwoLists(one,two): 
            sum+=i // 2 + 1
    print(sum)
    ary.append([[2]])
    ary.append([[6]])
    for i in range(len(ary)):
        j = i
        while j!=0 and not compareTwoLists(ary[j-1],ary[j]):
            hold = ary[j-1]
            ary[j-1] = ary [j]
            ary[j] = hold 
            j-=1
    print((ary.index([[2]])+1) * (1+ary.index([[6]])))

if __name__ == '__main__':
    main()


