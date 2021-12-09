import copy
from itertools import permutations

def calculate(operation_lst):
    if operation_lst[1] == "+":
        return operation_lst[0] + operation_lst[2]
    elif operation_lst[1] == "-":
        return operation_lst[0] - operation_lst[2]
    if operation_lst[1] == "*":
        return operation_lst[0] * operation_lst[2]
    if operation_lst[1] == "/":
        if operation_lst[0] < 0:
            return (abs(operation_lst[0]) // operation_lst[2]) * -1
        return operation_lst[0] // operation_lst[2]

N = int(input())
number_lst = list(map(int, input().split()))
plus, minus, multi, div = input().split()

plus_lst = ["+"] * int(plus)
minus_lst = ["-"] * int(minus)
multi_lst = ["*"] * int(multi)
div_lst = ["/"] * int(div)

operation_lst = plus_lst + minus_lst + multi_lst + div_lst

operation_combi = list(permutations(operation_lst, len(operation_lst)))

sentence_lst = []

for j in operation_combi:
    temp_number = copy.deepcopy(number_lst)
    temp_lst = []
    j = list(j)
    for i in range(len(number_lst) + len(operation_lst)):
        if i % 2 == 0:
            number = temp_number.pop(0)
            temp_lst.append(number)
        else:
            operation = j.pop(0)
            temp_lst.append(operation)


    sentence_lst.append(temp_lst)

for i in sentence_lst:
    while len(i) != 1:
        temp_lst = []
        for _ in range(3):
            temp_lst.append(i.pop(0))
        
        i.insert(0, calculate(temp_lst))
    
# print(sentence_lst)
print(max(sentence_lst)[0])
print(min(sentence_lst)[0])