monkeys = []
div_big = 1
class monkey:
    number_inspections:int=0
    starting_items:list[int] = [] 
    operation:str
    operation_other:str
    id: int 
    divisible_test_quotient:int 
    monkey_if_true:int
    monkey_if_false:int
    def __init__(self,items,operation,operation_other,id,quotient,monkey_if_true,monkey_if_false):
        self.operation_other = operation_other
        self.id = id
        self.starting_items = items
        self.operation = operation 
        self.divisible_test_quotient = quotient
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false

    def inspect_and_test_items(self):
        if len(self.starting_items)==0:
            return
        while(len(self.starting_items)>0):
            # self.number_inspections+=1
            # print(self.starting_items)
            self.inspect()
            b = self.test_at_zero()
            if(b[0]):
                monkeys[self.monkey_if_true].starting_items.append(b[1] % div_big)
                self.starting_items.pop(0)
            else:
                monkeys[self.monkey_if_false].starting_items.append(b[1] % div_big)
                self.starting_items.pop(0)
        # print(self.starting_items)
        # print('lsit')
    def inspect(self):
        if self.operation == '+':
            if 'old' in self.operation_other:
                self.starting_items[0]*=2 
            else:
                self.starting_items[0]+=int(self.operation_other)
        elif self.operation == '*':
            if 'old' in self.operation_other:
                self.starting_items[0]*=self.starting_items[0]
            else:
                self.starting_items[0]*=int(self.operation_other)

        


    def test_at_zero(self):
        worry_level = self.starting_items[0]
        return [0 == worry_level % self.divisible_test_quotient,worry_level]


monkeys = []
with open('input.txt','r',encoding='utf-8') as r :
    monkey_stats = []
    current_monkey = []
    monkey_id:int = 0
    starting_items = [] 
    operation:str = ''
    operation_other:str = ''
    test:int = 0
    monkey_if_true:int = 0 
    monkey_if_false:int = 0 

    for i in r :

        if 'Monkey ' in i :
             
            # monkey_stats.append(current_monkey)
            current_monkey = []
            new_monkey = monkey(starting_items,operation,operation_other,monkey_id,test,monkey_if_true,monkey_if_false)
            monkeys.append(new_monkey)
            monkey_id = int((i[i.index(':')-1:i.index(':')]))

        if 'Starting items' in i :
            current_monkey.append(i)
            starting_items = [] 
            string = i[i.index(":")+2:]
            while ',' in string:

                num:int = int(string[:string.index(",")])
                string = string[string.index(",")+2:]
                starting_items.append(num) 
            starting_items.append(int(string))


        if 'Operation' in i :
            current_monkey.append(i)
            if "+" in i:
                operation="+" 
                operation_other = i[i.index('+')+1:i.index('\n')]
            elif "*" in i :
                operation="*"
                operation_other = i[i.index('*')+1:i.index('\n')]




        if 'Test' in i :
            current_monkey.append(i)
            test = int(i[i.index('by ')+3:i.index('\n')])

        if 'true' in i :
            current_monkey.append(i)
            monkey_if_true = int(i[i.index('y')+2:i.index('\n')])
        if 'false' in i :
            current_monkey.append(i)
            monkey_if_false = int(i[i.index('y')+2:i.index('\n')])
    new_monkey = monkey(starting_items,operation,operation_other,monkey_id,test,monkey_if_true,monkey_if_false)
    monkeys.append(new_monkey)
    monkeys.pop(0)
        


for i in monkeys:
    div_big*=i.divisible_test_quotient
    # print(i.id)
    # print(i.operation_other)
    # print(i.divisible_test_quotient)
    # print(i.monkey_if_true)
    # print(i.monkey_if_false)
    # print(i.starting_items)
    # print('\n')



for i in range(10000) :
    for j in range(8):
        monkeys[j].number_inspections+=len(monkeys[j].starting_items)
        monkeys[j].inspect_and_test_items()

max1 = 0
max2 = 0
for i in monkeys:
    print(i.number_inspections)
    if i.number_inspections > max1:
        max2 = max1 
        max1 = i.number_inspections
    elif i.number_inspections > max2:
        max2 = i.number_insepctions
print(max1*max2)


