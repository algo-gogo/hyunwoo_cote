from copy import deepcopy

# key = [
#     [0, 0, 0],
#     [1, 0, 0],
#     [0, 1, 1]
# ]
# lock = [
#     [1, 1, 1],
#     [1, 1, 0],
#     [1, 0, 1]
# ]
key = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lock = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def rotate_90_right(key):
    N = len(key)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = key[r][c]
    return ret

def check_middle_all_one(new_lock):
    new_lock_len = len(new_lock) // 3
    for i in range(new_lock_len, new_lock_len * 2):
        for j in range(new_lock_len, new_lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True

# print(rotate_90_right(key))
lock_len = len(lock)
key_len = len(key)

new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]

for i in range(lock_len):
    for j in range(lock_len):
        new_lock[i + lock_len][j + lock_len] = lock[i][j]

for _ in range(4): # 한번씩 90도 씩 돌려보기
    key = rotate_90_right(key)
    for x in range(lock_len * 2):
        for y in range(lock_len * 2):
            temp_new_lock = deepcopy(new_lock)

            ## 끼워넣는 과정
            for i in range(key_len):
                for j in range(key_len):
                    temp_new_lock[x + i][y + j] += key[i][j]
            
            if check_middle_all_one(temp_new_lock):
                print(True)
            
print(False)
