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


def parttwo():
    
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
    for j in range(0,4000001):
        for k in range(0,4000001):
            for i in range(len(sensors)) : 
                x_check_length = abs(j-sensors[i][0])
                y_check_length = abs(k-sensors[i][1])
                check_distance = x_check_length + y_check_length
                x_length = abs(sensors[i][0] - beacons[i][0])
                y_length = abs(sensors[i][1]-beacons[i][1])
                distance = x_length + y_length

                # print(square)
                # print(check_square)
                f=True
                if [j,k] in beacons:
                    f=False
                    ans.append([j,k])
                    break
                if [j,k] in sensors or not f:
                    f=False
                    ans.append([j,k])
                    break
                if not f : break
                if (check_distance <= distance):
                    ans.append([j,k])
                    break

    print(len(ans))
    print(sum)
    print(minx,maxx)
    for i in range(0,4000001):
        for j in range(0,4000001):
            if [i,j] not in ans :
                tune = (4000000*i)+j
                print(i,j)
                print(tune)

def main ():
    # partone()
    parttwo()


if __name__ == '__main__':
    main()
