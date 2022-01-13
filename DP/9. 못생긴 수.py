n = int(input())

def factorization(x): 
    d = 2 
    temp_lst = []
    while d <= x:
        if x % d == 0:
            temp_lst.append(d) 
            x = x / d 
        else: 
            d = d + 1
    return list(set(temp_lst))

ugly_lst = []
end_count, count = 0, 1
while True:
    if end_count == n:
        print(ugly_lst[n - 1])
        break
    temp_lst = factorization(count)
    if 2 in temp_lst:
        temp_lst.remove(2)
    if 3 in temp_lst:
        temp_lst.remove(3)
    if 5 in temp_lst:
        temp_lst.remove(5)
    
    if len(temp_lst) == 0:
        ugly_lst.append(count)
        end_count += 1
    
    count += 1
