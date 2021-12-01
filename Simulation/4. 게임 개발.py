# 다시 풀기
''' 입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
=> 6
'''

n, m = map(int, input().split())
character = list(map(int,input().split()))
game_map = []
for _ in range(m):
    game_map.append(list(input().split()))

direction = {0: [0,-1], 1: [1,0], 2: [0,1], 3: [-1,0]}

cnt = 0
while(True):
    if game_map[character[0] + direction[character[2] % 4][0], character[1] + direction[character[2] % 4][1]] == 0:
        pass
    else:
        character 
    

print(cnt)