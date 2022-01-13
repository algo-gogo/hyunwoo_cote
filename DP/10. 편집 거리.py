# string_a = input()
# string_b = input()

string_a = "sunday"
string_b = "saturday"


answer_table = []
for i in range(len(string_a) + 1):
    if i == 0:
        answer_table.append(list(range(len(string_b) + 1)))
    else:
        answer_table.append([i] + [5001] * len(string_b))


for i_ind, i_val in enumerate(answer_table):
    for j_ind, j_val in enumerate(i_val):
        if (i_ind - 1) < 0 or (j_ind - 1) < 0:
            continue
        else:
            if string_a[i_ind - 1] == string_b[j_ind - 1]:
                answer_table[i_ind][j_ind] = answer_table[i_ind - 1][j_ind - 1]
            else:
                answer_table[i_ind][j_ind] = 1 + min(answer_table[i_ind - 1][j_ind - 1], answer_table[i_ind][j_ind - 1], answer_table[i_ind - 1][j_ind])

# for i in answer_table:
#     print(i)

print(answer_table[-1][-1])
