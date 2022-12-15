import math


def partone():

    sensors = [] 
    beacons = []
    with open('input.txt','r',encoding='utf=8') as r :
        for i in r :
            sensor_string = i[:i.index(':')]
            x = sensor_string[sensor_string.index('x'):sensor_string.index(',')]
            y = sensor_string[sensor_string.index(',')+2:]
            print (x)
            print (y)
            x = x[x.index('=')+1:]
            y = y[y.index('=')+1:]
            print (x)
            print (y)
            sensor = [int(x),int(y)]
            beacon_string = i[i.index('is at')+6:]
            print(beacon_string)
            x_b= beacon_string[beacon_string.index('x'):beacon_string.index(',')]
            y_b = beacon_string[beacon_string.index(',')+2:]
            x_b = x_b[x_b.index('=')+1:]
            y_b = y_b[y_b.index('=')+1:]
            print (x_b)
            print (y_b)
            beacon = [int(x_b),int(y_b)]
            sensors.append(sensor)
            beacons.append(beacon)

    sum = 0 
    xcoords = []
    for i in sensors :
        xcoords.append(i[0])
    for i in beacons :
        xcoords.append(i[0])
    ycoords = []
    for i in sensors :
        ycoords.append(i[1])
    for i in beacons :
        ycoords.append(i[1])

    minx = min(xcoords)
    maxx = max(xcoords)
    print( minx , maxx )
    ans = []
    for j in range(minx,maxx+1):
        for i in range(len(sensors)) : 
            x_check_length = abs(j-sensors[i][0])
            y_check_length = abs(2000000-sensors[i][1])
            check_distance = x_check_length + y_check_length
            x_length = abs(sensors[i][0] - beacons[i][0])
            y_length = abs(sensors[i][1]-beacons[i][1])
            distance = x_length + y_length

            # print(square)
            # print(check_square)
            f=True
            if [j,2000000] in beacons:
                    f=False
                    break
            if [j,2000000] in sensors or not f:
                f=False
                break
            if not f : break
            if (check_distance <= distance):
                sum+=1
                ans.append([j,2000000])
                break

    print(len(ans))
    print(sum)
    print(minx,maxx)



def mergetwoRanges(range1:list,range2):
    # print(range1,range2)
    if len(range1)==0 and len(range2)==0:
        return []
    if len(range1) == 0:
        # print('range 2 ' + str(range2))
        return range2
    elif len(range2) == 0:
        # print('range 1 ' + str(range1))
        return range1
    else:
        # print( [min([range1[0],range2[0]]),max([range1[1],range2[1]])])
        return [min([range1[0],range2[0]]),max([range1[1],range2[1]])]
def taxi_distance(c1,c2):
    x_length = abs(c1[0] - c2[0])
    y_length = abs(c1[1]-c2[1])
    distance = x_length + y_length
    return distance
    

def get_range(row:int,sensor:list,beacon:list)->list[int]:
    x_distance = abs(sensor[0]-row)
    range_radius = taxi_distance(sensor,beacon) - x_distance
    if range_radius < 0 :
        return []
    return [sensor[1]-range_radius,sensor[1]+range_radius]




def parttwo():
    d:dict  = {'[0,0]':False}
    sensors = [] 
    beacons = []
    with open('input.txt','r',encoding='utf=8') as r :
        for i in r :
            sensor_string = i[:i.index(':')]
            x = sensor_string[sensor_string.index('x'):sensor_string.index(',')]
            y = sensor_string[sensor_string.index(',')+2:]
            print (x)
            print (y)
            x = x[x.index('=')+1:]
            y = y[y.index('=')+1:]
            print (x)
            print (y)
            sensor = [int(x),int(y)]
            beacon_string = i[i.index('is at')+6:]
            print(beacon_string)
            x_b= beacon_string[beacon_string.index('x'):beacon_string.index(',')]
            y_b = beacon_string[beacon_string.index(',')+2:]
            x_b = x_b[x_b.index('=')+1:]
            y_b = y_b[y_b.index('=')+1:]
            print (x_b)
            print (y_b)
            beacon = [int(x_b),int(y_b)]
            sensors.append(sensor)
            beacons.append(beacon)

    sum = 0 
    xcoords = []
    for i in sensors :
        xcoords.append(i[0])
    for i in beacons :
        xcoords.append(i[0])
    ycoords = []
    for i in sensors :
        ycoords.append(i[1])
    for i in beacons :
        ycoords.append(i[1])

    xcoords.sort()
    while min(xcoords)<0 : xcoords.pop(0)
    print(min(xcoords))
    minx = min(xcoords)
    while max(xcoords)>4000000: xcoords.pop(len(xcoords)-1)
    maxx = max(xcoords)
    ycoords.sort()
    while min(ycoords)<0 : ycoords.pop(0)
    print(min(ycoords))
    miny = min(ycoords)
    while max(ycoords)>4000000: ycoords.pop(len(ycoords)-1)
    maxy = max(ycoords)
    print( miny , maxy )
    ans = []
    for i in range(0,4000001):
        ranges = []
        print(i)
        for j in range(len(sensors)):
            
            range_ = get_range(i,sensors[j],beacons[j])
            # print(range_)
            # print(ranges)
            f = False
            if len(ranges)==2 and can_merge(ranges[0],ranges[1]):
                ranges = [mergetwoRanges(ranges[0],ranges[1])]
            elif len(ranges)>=2:

                for k in range(len(ranges)):
                    if can_merge(ranges[k],range_):
                        ranges[k] = mergetwoRanges(ranges[k],range_)
                        f = True
                        break
            if not f: ranges.append(range_)
            if len(ranges) > 2:
                 
                while len(ranges) >=2 :
                    if can_merge(ranges[0],ranges[1]):
                        ranges[1] = mergetwoRanges(ranges[0],ranges[1])
                        ranges.pop(0)

                    else:
                        if can_merge(ranges[0],ranges[len(ranges)-1]):
                            ranges[len(ranges)-1] = mergetwoRanges(ranges[0],ranges[len(ranges)-1])
                            ranges.pop(0)
                        else:break
            
        
        if len(ranges)==2 and can_merge(ranges[0],ranges[1]):
            ranges = [mergetwoRanges(ranges[0],ranges[1]) ]
             
        if len(ranges)!=1 : return [i,ranges]

# [2,7][8,10]
def can_merge(range1:list[int],range2:list[int])->bool:
    if len(range1)==0 or len(range2)==0 : return True
    if range1[0] < range2[1] and range1[0] < range2[0] and range1[1] < range2[1] and range1[1] < range2[0] : return False
    if range2[0] < range1[1] and range2[0] < range1[0] and range2[1] < range1[1] and range2[1] < range1[0] : return False
    return True


def main ():
    # partone()
    print(parttwo())


if __name__ == '__main__':
    main()
