


class valve:
    label:str
    flow_rate:int
    neighbors:list[str]
    marked:bool
    open:bool
    def __init__(self,label,flow_rate,neighbors=[]):
        self.label = label 
        self.flow_rate = flow_rate 
        self.neighbors = neighbors 
        self.marked = False 
        
        self.open = False
    def best_yield(self,valves,minute)->list:
        li = []
        for i in valves :
            if total_yield(valves,self,valves[i],minute) > 0 and not valves[i].open:
                li.append([i,total_yield(valves,self,valves[i],minute)])
        max = ['',0]
        for i in li :
            if i[1] > max[1] : 
                max = i
                print(i)
        print(self.label,max)
        return max
def all_open(valves):
    for i in valves:
        if not valves[i].open and valves[i].flow_rate>0:
            return False
    return True

def traverse(valves):
    min = 1
    total= 0
    cur = valves['AA']
    while not all_open(valves) and min<30:
        b = cur.best_yield(valves,min);
        if b[0]=='': print(total)
        min+=shortest_path(valves,cur,valves[b[0]])
        total += b[1]
        cur = valves[b[0]]
        cur.open=True
    print(total)

def bfs(valves):
    cur = valves['AA']
    queue = [] 
    queue.append('AA')
    cur_total = 0
    max_total = 0
    while len(queue)>0:
        cur = queue.pop()
        [ queue.append(valves[f]) for f in cur.neighbors if f.open]
        if cur.open and cur.flow_rate>0 : 
            cur_total += traverse()





def total_yield(valves,cur:valve,target:valve,cur_minute):
    if target.flow_rate==0: return 0
    if target.open : return 0
    wait = 30 - cur_minute
    mul_wait = wait - shortest_path(valves,cur,target) 
    flow = target.flow_rate
    mul_wait *= flow
    return mul_wait

def shortest_path(valves,cur:valve,target:valve):
    for i in valves:
        valves[i].marked = False
    queue = []
    queue.append(cur.label)
    cur.marked=True
    d_list:dict[str,int]={}
    d_list[str(cur.label)]=0
    while len(queue)>0:
        cur = valves[queue.pop(0)]
        cur.marked=True
        for i in cur.neighbors :
            if not valves[i].marked :
                queue.append(i)
                x=int(d_list[str(cur.label)])+1
                d_list[str(valves[i].label)]=x
    return d_list[target.label]-1

def parse():
    valves:dict = {}
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r :
            i=i[:i.index('\n')]
            label:str = i[6:8]
            print(label)
            neighbors = []
            flow_rate = int(i[i.index('=')+1:i.index(';')])
            f = i[i.index('ve')+4:]
            f = f[f.index('ve')+4:]
            print(f)
            if ','  not in i : 
                print(i)
                neighbors.append(i[len(i)-2:])
            else:
                while ',' in f :
                    neighbors.append(f[:f.index(',')])
                    f=f[f.index(',')+2:]
                    print(f)
                neighbors.append(f[:2])
            print(neighbors)
            v = valve(label,flow_rate,neighbors)

            valves[v.label] = v
    return valves
def main():
    valves = parse()
    traverse(valves)

if __name__ == '__main__':
    main()
