from itertools import permutations
from collections import defaultdict

test = "100-200*300-500+20"

#print((100-200)*(300-(500+20)))


# 연산 배열 생성
cal = ["+","-","*"]
cal_ = list(permutations(cal,3))


def sol(expression):
    a=""
    semi = []
    for i in range(len(expression)):
        if expression[i] in cal:
            semi.append(int(a))
            semi.append(expression[i])
            a = ""
        else:
            a = a + expression[i]
            
        if i == len(expression)-1:
            semi.append(int(a))
    
    dic_op = {}
    dic_num = {}
    for i in range(len(semi)):
        if semi[i] in cal:
            dic_op[i] = semi[i]
        else:
            dic_num[i] = semi[i]
    

print(sol("100-200*300-500+20"))
#[100, '-', 200, '*', 300, '-', 500, '+', 20]

def calculate(dic_op,dic_num, cal):
    return 0

def op(a,b,OP):
    if OP == "+":
        return a + b
    elif OP == "-":
        return a - b
    elif OP == "*":
        return a*b
    return



semi = [100, '-', 200, '*', 300, '-', 500, '+', 20]
dic_op = {}
dic_num = {}
for i in range(len(semi)):
    if semi[i] in cal:
        dic_op[i] = semi[i]
    else:
        dic_num[i] = semi[i]
print(cal)
print(dic_op)
print(dic_num)

def calculate(dic_op,dic_num, cal):
    if len(dic_num) == 1:
        return dic_num
    
    new_dict_num = {}
    
    for i in cal:
        for j in dic_op:
            if i == dic_op[j]:
                #계산 해서 new_dic에 추가
            else:
                new_dict_num[]
    
    return calculate()

a = {1: '-', 3: '*', 5: '-', 7: '+'}

print(list(a.items())[3][1])


