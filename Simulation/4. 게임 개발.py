아직
''' 입력 예시
a1 => 2
c2 => 6
'''

alp_to_num = {"a" : 1, "b" : 2, "c" : 3, "d" : 4,
              "e" : 5, "f" : 6, "g" : 7, "h" : 8,}

# n = input()
n = 'd4'
n = [alp_to_num[n[0]], int(n[1])]

steps = [[-2,-1], [-1,-2], [-2,1], [-1,2],
        [2,-1], [1,-2], [2,1], [1,2]]

cnt = 0
for step in steps:
    temp = copy.deepcopy(n)
    temp[0] += step[0]
    temp[1] += step[1]
    if (temp[0] < 1 or temp[0] > 8 or
        temp[1] < 1 or temp[1] > 8):
        continue
    cnt += 1
print(cnt)