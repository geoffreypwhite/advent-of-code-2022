



class cycle:
    instruction:int
    count: int
    queue:list[int]
    def __init__(self):
         self.instruction = 0
         self.count = 1
         self.queue = []
    def cycle(self):
        x = self.queue.pop(0)
        # print(x)
        if x is not None:
            self.count+=x
        self.instruction+=1
    def read_instruction(self,string):
        if 'addx' in string:
            num = int(string[string.index(' ')+1:])
            # print(num)
            self.queue.append(0)
            self.queue.append(num)
        else:
            self.queue.append(0)








def main():
    partone()
    parttwo()



# 340
# 720
# 3400
# 4200
# 1260
# 4620

def partone():
    cyc = cycle()
    sum = 0
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r : 
            cyc.read_instruction(i)
            cyc.cycle()
            if cyc.instruction in [19,59,99,139,179,219]:
                sum+=(cyc.count * (1+cyc.instruction))
        while len(cyc.queue) > 1 :
            cyc.cycle()
            if cyc.instruction in [19,59,99,139,179,219]:
                sum+= (cyc.count * (1+cyc.instruction))
    print(sum) 


def parttwo():
    CRT =  ['........................................'
           ,'........................................'
           ,'........................................'
           ,'........................................'
           ,'........................................'
           ,'........................................']
    cyc = cycle()
    with open('input.txt','r',encoding='utf-8') as r :
        for i in r : 
            if cyc.instruction <=40 :
                if abs(cyc.instruction-cyc.count) <= 1:
                    CRT[0] = CRT[0][:cyc.instruction] + '#' + CRT[0][cyc.instruction+1:]
            if cyc.instruction > 39 and cyc.instruction <=80:
                if abs(cyc.instruction-cyc.count-40) <= 1:
                    CRT[1] = CRT[1][:cyc.instruction-40] + '#' + CRT[1][cyc.instruction-40+1:]
            if cyc.instruction > 79 and cyc.instruction <=120:
                if abs(cyc.instruction-cyc.count-80) <= 1:
                    CRT[2] = CRT[2][:cyc.instruction-80] + '#' + CRT[2][cyc.instruction-80+1:]

            if cyc.instruction > 119 and cyc.instruction <=160:
                if abs(cyc.instruction-cyc.count-120) <= 1:
                    CRT[3] = CRT[3][:cyc.instruction-120] + '#' + CRT[3][cyc.instruction-120+1:]

            if cyc.instruction > 159 and cyc.instruction <=200:
                if abs(cyc.instruction-cyc.count-160) <= 1:
                    CRT[4] = CRT[4][:cyc.instruction-160] + '#' + CRT[4][cyc.instruction-160+1:]
            if cyc.instruction > 199 and cyc.instruction <=240:
                if abs(cyc.instruction-cyc.count-200) <= 1:
                    CRT[5] = CRT[5][:cyc.instruction-200] + '#' + CRT[5][cyc.instruction-200+1:]
            cyc.read_instruction(i)
            cyc.cycle()
        while len(cyc.queue) > 1 :
            if cyc.instruction <=40 :
                if abs(cyc.instruction-cyc.count) <= 1:
                    CRT[0] = CRT[0][:cyc.instruction] + '#' + CRT[0][cyc.instruction+1:]
            if cyc.instruction > 39 and cyc.instruction <=80:
                if abs(cyc.instruction-cyc.count-40) <= 1:
                    CRT[1] = CRT[1][:cyc.instruction-40] + '#' + CRT[1][cyc.instruction-40+1:]
                
            if cyc.instruction > 79 and cyc.instruction <=120:
                if abs(cyc.instruction-cyc.count-80) <= 1:
                    CRT[2] = CRT[2][:cyc.instruction-80] + '#' + CRT[2][cyc.instruction-80+1:]

            if cyc.instruction > 119 and cyc.instruction <=160:
                if abs(cyc.instruction-cyc.count-120) <= 1:
                    CRT[3] = CRT[3][:cyc.instruction-120] + '#' + CRT[3][cyc.instruction-120+1:]

            if cyc.instruction > 159 and cyc.instruction <=200:
                # print(cyc.count * cyc.instruction-160)
                if abs(cyc.instruction-cyc.count-160) <= 1:
                    CRT[4] = CRT[4][:cyc.instruction-160] + '#' + CRT[4][cyc.instruction-160+1:]
            if cyc.instruction > 199 and cyc.instruction <=240:
                if abs(cyc.instruction-cyc.count-200) <= 1:
                    CRT[5] = CRT[5][:cyc.instruction-200] + '#' + CRT[5][cyc.instruction-200+1:]
            cyc.cycle()
    for i in CRT :
        print (i)






if __name__=='__main__':
    main()
