directories:dict = {}
curpath = '/'

class file:
    name: str
    size: int
    def __init__(self,name,size):
        self.name = name 
        self.size = size




class directory: 
    files:list[file]
    children: list[str]
    pathname: str
    def __init__(self,pathname):
        self.pathname = pathname
        self.children = []
        self.files = []

    def get_size(self):
        sum = 0
        for i in self.files:
            sum+= i.size
        for i in self.children:
            newpath = self.pathname + i + '/'
            sum+= directories[newpath].get_size()
        return sum


home = directory('/')
directories[home.pathname] = home
cur = home
with open('input.txt','r',encoding='utf-8') as r:

    for i in r:
        
        if '$' in i and 'cd /\n' in i:
            curpath ='/'
    
        elif '$' in i and 'cd ..' in i:
            if i.count('/') == 2:
                curpath = '/'
            curpath = curpath[::-1]
            curpath = curpath[1:]
            curpath = curpath[curpath.index('/'):]
            curpath = curpath[::-1]
            
        elif '$' in i and 'cd ' in i:
            
            curpath += i[i.index('cd ')+3:i.index('\n')] + '/'
            
        elif '$' in i and 'ls' in i:
            None
            print(curpath)
        elif 'dir ' in i :
            directories[curpath + i[i.index('dir ') + 4:i.index('\n')] + '/'] = directory(curpath+i[i.index('dir ' )+ 4:i.index('\n')] + '/')
            print(directories[curpath])
            print(directories)
            directories[curpath].children.append(i[i.index('dir ') + 4 :i.index('\n')])
        else:
            newfilename = i[i.index(' ')+1:i.index('\n')]
            newfilesize = int(i[:i.index(' ')])
            directories[curpath].files.append(file(newfilename,newfilesize))

s = 0
for i in directories:
    x = directories[i].get_size()
    if x <= 100000 :
        s+= x
print(s)

         

used = directories['/'].get_size()
available = 70000000 - used 
print (available)
needed = 30000000 - available 
smallestOverNeeded = directories['/'].get_size()
for i in directories: 
    if directories[i].get_size() > needed and directories[i].get_size() < smallestOverNeeded :
        smallestOverNeeded = directories[i].get_size()
print (smallestOverNeeded)


