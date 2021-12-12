N, K = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort(reverse=True)

answerlst = list1[K:] + list2[:K]
print(sum(answerlst))