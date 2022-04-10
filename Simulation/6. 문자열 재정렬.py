''' 입력 예시
K1KA5CB7 => ABCKK13
AJKDLSI412K4JSJ9D => ADDIJJJKKLSS20
'''

string = input()

alpha, number = [], []
for i in string:
    if i.isnumeric():
        number.append(int(i))
    elif i.isalpha():
        alpha.append(i)
    else:
        continue

alpha.sort()
print("".join(alpha) + str(sum(number)))