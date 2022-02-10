from itertools import combinations

vowels = ("a", "e", "i", "o", "u")
l, c = map(int, input().split())

array = input().split()
array.sort()

for password in combinations(array, l):
    vowel_count = 0
    for i in password:
        if i in vowels:
            vowel_count += 1
    if vowel_count >= 1 and vowel_count <= l - 2:
        print("".join(password))