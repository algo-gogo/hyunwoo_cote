''' 입력 예시
123402 => LUCKY
7755 => READY
'''

score = input()
score_length = len(score)

left_sum, right_sum = 0, 0
for i in range(score_length):
    if i < score_length / 2:
        left_sum += int(score[i])
    else:
        right_sum += int(score[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")