# positions = [] 

# row = [] 
# for j in range(100):
#     for i in range(100) : 
#         row.append('o')
#     positions.append(row)


def touching(head_position,tail_position) -> bool :
    if head_position[0] - tail_position[0] <= 1 and head_position[0] - tail_position[0] >= -1 :
        if head_position[1] - tail_position[1] <= 1 and head_position[1] - tail_position[1] >= -1 :
            return True
    return False


def step(s:str,pos):
    if s == 'U' :
        pos[0] += 1
    if s == 'D' :
        pos[0] -= 1
    if s == 'R' :
        pos[1] += 1
    if s == 'L' :
        pos[1] -= 1
    return pos

#   12345
# 1 nnnnn
# 2 naaan
# 3 natan
# 4 naaan
# 5 nnnnn
def step_tail(head_position,tail_position):
    head_row = head_position[0]
    head_column = head_position[1]
    tail_row = tail_position[0]
    tail_column = tail_position[1]
    same_row = (head_row==tail_row)
    same_column = (head_column==tail_column)
    if same_row and not same_column :
        if head_column > tail_column :
            tail_position[1]+=1
        else :
            tail_position[1]-=1
    elif same_column and not same_row :
        if head_row > tail_row :
            tail_position[0]+=1
        else :
            tail_position[0]-=1
    elif not same_column and not same_row :

        if head_column > tail_column and head_row > tail_row :
            tail_position[0]+=1
            tail_position[1]+=1

        elif head_column > tail_column and head_row < tail_row:
            tail_position[0]-=1
            tail_position[1]+=1


        elif head_column < tail_column and head_row > tail_row:
            tail_position[0]+=1
            tail_position[1]-=1

        elif head_column < tail_column and head_row < tail_row:
            tail_position[0]-=1
            tail_position[1]-=1
    return tail_position



def parttwo():


    head_position = [0,0]
    two = [0,0]
    three = [0,0]
    four = [0,0]
    five = [0,0]
    six = [0,0]
    seven = [0,0]
    eight = [0,0]
    nine = [0,0]
    tail_position = [0,0]

    knots = [head_position,two,three,four,five,six,seven,eight,nine,tail_position]

    places2 = []
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r:
            distance: int = int(i[i.index(' ')+1:])
            # print(distance)
            if 'R' in str(i):
                for k in range(distance):
                    head_position = step('R',head_position)
                    for j in range(0,9):
                        if not touching(knots[j],knots[j+1]):
                            knots[j+1] = step_tail(knots[j],knots[j+1])
                    if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places2:
                        places2.append(str(tail_position[0]) + ' ' + str(tail_position[1]))
            if 'L' in str(i):
                for k in range(distance):
                    head_position = step('L',head_position)
                    for j in range(0,9):
                        if not touching(knots[j],knots[j+1]):
                            knots[j+1] = step_tail(knots[j],knots[j+1])
                    if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places2:
                        places2.append(str(tail_position[0]) + ' ' + str(tail_position[1]))
            if 'U' in str(i):
                for k in range(distance):
                    head_position = step('U',head_position)
                    for j in range(0,9):
                        # print(j)
                        if not touching(knots[j],knots[j+1]):
                            knots[j+1] = step_tail(knots[j],knots[j+1])
                    if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places2:
                        places2.append(str(tail_position[0]) + ' ' + str(tail_position[1]))
            if 'D' in str(i):
                for k in range(distance):
                    head_position = step('D',head_position)
                    for j in range(0,9):
                        if not touching(knots[j],knots[j+1]):
                            knots[j+1] = step_tail(knots[j],knots[j+1])
                    if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places2:
                        places2.append(str(tail_position[0]) + ' ' + str(tail_position[1]))

    print(len(places2))


# R = [0,0]->[0,1] == position[1]++
# L = [0,0]->[0,-1 == position[1]--
# U = [0,0]->[1,0] == position[0]++
# D = [0,0]->[-1,0]== position[0]--
def partone():
    places = ['0 0']
    head_position=[0,0]
    tail_position=[0,0]
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r:
            # print(head_position)
            # print(tail_position)
            # print (i)
            distance: int = int(i[i.index(' ')+1:])
            # print(distance)
            if 'R' in str(i):
                for i in range(distance):
                    head_position = step('R',head_position)
                    if not touching(head_position,tail_position):
                        # print('fffffffff')
                        tail_position = step_tail(head_position,tail_position)
                        # print(tail_position)
                        if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places:
                            places.append(str(tail_position[0]) + ' ' + str(tail_position[1]))

            if 'L' in str(i):
                for i in range(distance):
                    head_position = step('L',head_position)
                    if not touching(head_position,tail_position):
                        tail_position = step_tail(head_position,tail_position)
                        if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places:
                            places.append(str(tail_position[0]) + ' ' + str(tail_position[1]))

            if 'U' in str(i):
                for i in range(distance):
                    head_position = step('U',head_position)
                    if not touching(head_position,tail_position):
                        tail_position = step_tail(head_position,tail_position)
                        if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places:
                            places.append(str(tail_position[0]) + ' ' + str(tail_position[1]))

            if 'D' in str(i):
                for i in range(distance):
                    head_position = step('D',head_position)
                    if not touching(head_position,tail_position):
                        tail_position = step_tail(head_position,tail_position)
                        if str(tail_position[0]) + ' ' + str(tail_position[1]) not in places:
                            places.append(str(tail_position[0]) + ' ' + str(tail_position[1]))

                 
        print(len(places))

def main():
    partone()
    parttwo()

if __name__ == '__main__':
    main()


