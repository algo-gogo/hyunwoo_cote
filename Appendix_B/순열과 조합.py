## 순열 permutations
from itertools import permutations
data = [1, 2]
for x in permutations(data, 2):
    print(list(x))
    
## 조합 combinations
from itertools import combinations
data = [1, 2]
for x in combinations(data, 2):
    print(list(x))