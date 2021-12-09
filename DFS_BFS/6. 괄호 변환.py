input_string = input()

temp_lst = [input_string[0]]
answer_lst = []
lefthead_count, righthead_count = 0, 0

while input_string:
    a = input_string.pop(0)
    if a == "(":
        lefthead_count += 1
    elif a == ")":
        righthead_count += 1