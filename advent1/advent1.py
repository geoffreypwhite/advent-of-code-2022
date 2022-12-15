

caloriesPerElf:list[int] = []
with open('input1.txt','r',encoding='utf-8') as _input:
    calorieCount:int=0;
    for i in _input:
        if i=="\n":
            caloriesPerElf.append(calorieCount)
            calorieCount = 0;
        else:
            calorieCount+=int(i)

caloriesPerElf.sort()
print (caloriesPerElf[len(caloriesPerElf)-1])
#part one

n = caloriesPerElf[len(caloriesPerElf)-1] + caloriesPerElf[len(caloriesPerElf)-2]  + caloriesPerElf[len(caloriesPerElf)-3]

print(str(n))



