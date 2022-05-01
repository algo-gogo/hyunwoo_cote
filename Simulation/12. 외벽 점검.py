from itertools import permutations
def solution(n, weak, dist):
    weak_len, dist_len = len(weak), len(dist)
    answer_lst = []
    weak_point = weak + [w + n for w in weak]  # 1 5 6 10 => 1 5 6 10 13 18 19 22

    for ind, start in enumerate(weak):
        for friends in permutations(dist, dist_len):  # 순열 이용
            # print(friends)
            count = 1
            position = start
            # 친구 조합 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달 못했을 때
                if position < weak_point[ind + weak_len - 1]:
                    count += 1  # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    temp = [] 
                    for w in weak_point[ind + 1 : ind + weak_len]:
                        if w > position:
                            temp.append(w)
                    position = temp[0]
                    # position = [w for w in weak_point[ind + 1 : ind + weak_len]
                    #             if w > position][0]
                    print(position)
                else:  # 끝 포인트까지 도달
                    answer_lst.append(count)
                    break

    if answer_lst:
        return min(answer_lst)    
    return -1

n1 = 12
weak1 = [1, 5, 6, 10]
dist1 = [1, 2, 3, 4]

n2 = 12
weak2 = [1, 3, 4, 9, 10]
dist2 = [3, 5, 7]

print(solution(n2, weak2, dist2))