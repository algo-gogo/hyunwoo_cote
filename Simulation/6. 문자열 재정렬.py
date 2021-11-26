''' 입력 예시
K1KA5CB7 => ABCKK13
AJKDLSI412K4JSJ9D => ADDIJJJKKLSS20
'''

string = input()

alpha, number = [], []
for i in string:
    if i >= "A" and i <= "Z":
        alpha.append(i)
    else:
        number.append(int(i))

alpha.sort()
print("".join(alpha) + str(sum(number)))