input_string = input()

if len(input_string) == 0:
    print(0)

temp_lst = [input_string[0]]
answer_lst = []
lefthead_count = input_string.count('(')
righthead_count = input_string.count(')')

if lefthead_count != righthead_count:
    input_string = "(" + input_string

while input_string:
    a = input_string.pop(0)
    if a == "(":
        lefthead_count += 1
    elif a == ")":
        righthead_count += 1