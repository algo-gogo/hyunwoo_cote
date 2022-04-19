''' 입력 예시
5 3 
1 2 5 4 3
5 5 6 6 5

=> 26
'''

N, K = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort(reverse=True)

answerlst = list1[K:] + list2[:K]
print(sum(answerlst))