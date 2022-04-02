"""
money	costs	                    result (문제의 답)
4578	[1, 4, 99, 35, 50, 1000]	2308
1999	[2, 11, 20, 100, 200, 600]	2798
"""

def solution(money, costs):

    money_dict = {
        1 : costs[0],
        5 : costs[1],
        10 : costs[2],
        50 : costs[3],
        100 : costs[4],
        500 : costs[5]
    }

    money_per_dict = {
        1 : costs[0],
        5 : costs[1] / 5,
        10 : costs[2] / 10,
        50 : costs[3] / 50,
        100 : costs[4] / 100,
        500 : costs[5] / 500
    }

    money_list = []
    for coin, cost in money_per_dict.items():
        money_list.append((cost, coin))

    money_list.sort()
    answer = 0

    for _, coin in money_list:
        div_res = money // coin
        money -= div_res * coin
        answer += div_res * money_dict[coin]
    
    print(answer)
            
# case 1
money = 4578
costs = [1, 4, 99, 35, 50, 1000]

# case 2
money = 1999
costs = [2, 11, 20, 100, 200, 600]

solution(money, costs)