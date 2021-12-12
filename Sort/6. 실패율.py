def solution(N, stages):
    stage_lst = []
    length = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
        
        stage_lst.append((i, fail))
        length -= cnt
    
    stage_lst.sort(key=lambda x: x[1], reverse=True)
    stage_lst = [i[0] for i in stage_lst]
    # print(stage_lst)
    return stage_lst