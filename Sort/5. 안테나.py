''' 입력 예시
4
5 1 7 9

=> 5
'''

N = int(input())

house_lst = list(map(int, input().split()))
house_lst.sort()

print(house_lst[(N - 1) // 2])