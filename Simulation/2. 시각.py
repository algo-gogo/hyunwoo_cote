''' 입력 예시
5 => 11475
'''

# n = int(input())
n = 5

cnt = 0
for hour in range(0, n+1):
    for minute in range(0, 60):
        for second in range(0, 60):
            temp = str(hour) + str(minute) + str(second)
            if "3" in temp:
                cnt += 1
            
print(cnt)