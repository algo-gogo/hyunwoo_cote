"""
width	height	diagonals	    result
2	    2	    [[1,1],[2,2]]	12
51	    37	    [[17,19]]	    3225685
"""


import math

def solution(width, height, diagonals):
    answer = 0
    for diag in diagonals:
        diag_x, diag_y = diag

        start_diag_pt = (diag_x - 1, diag_y)
        end_diag_pt = (diag_x , diag_y - 1)

        zero_to_start_diag = find((0,0), start_diag_pt)
        zero_from_end_diag = find(end_diag_pt, (width, height))
        zero_with_diag = (zero_to_start_diag * zero_from_end_diag) % 10000019
        answer = (answer + zero_with_diag) % 10000019

        start_diag_pt, end_diag_pt = end_diag_pt, start_diag_pt
        zero_to_start_diag = find((0,0), start_diag_pt)
        zero_from_end_diag = find(end_diag_pt, (width, height))
        zero_with_diag = (zero_to_start_diag * zero_from_end_diag) % 10000019
        answer = (answer + zero_with_diag) % 10000019

    return answer


### 가로 2 세로 3 이면 (3 + 2)! / (3! * 2!)
def find(start_pt, end_pt):
    w = end_pt[0] - start_pt[0]
    h = end_pt[1] - start_pt[1]
    return int(math.factorial(w+h) / (math.factorial(w) * math.factorial(h))) % 10000019