# ## 효율성 Fail 시간초과
# def solution(words, queries):
#     answer = []
#     for query in queries:
#         count = 0
#         for word in words:
#             if len(word) != len(query):
#                 continue
#             query_flag = 0
#             for i in range(len(query)):
#                 if query[i] == "?":
#                     continue
#                 if word[i] != query[i]:
#                     query_flag = 1
#                     break
#             if query_flag == 0:
#                 count += 1
#         answer.append(count)
#     return answer

# ## 효율성 Fail 시간초과
# import re
# def solution(words, queries):
#     answer = []

#     for query in queries:
#         this_query = ""
#         for i in query:
#             if i == "?":
#                 this_query += "\w"
#             else:
#                 this_query += i
        
#         count = 0
#         for word in words:
#             if len(query) != len(word):
#                 continue
#             x = re.findall(this_query, word)
#             if x:
#                 count += 1
#         answer.append(count)
            
#     return answer

## 답지
from bisect import bisect_left, bisect_right

def count_by_range(array, left_val, right_val):
    right_idx = bisect_right(array, right_val)
    left_idx = bisect_left(array, left_val)
    return right_idx - left_idx

# 길이마다 나누어서 저장하는 리스트
array = [[] for _ in range(10001)]

# 뒤집어서 저장하는 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        word_len = len(word)
        array[word_len].append(word)
        reversed_array[word_len].append(word[::-1])

    for i in range(10001):
        if len(array[i]) != 0:
            array[i].sort()
        if len(reversed_array[i]) != 0:
            reversed_array[i].sort()

    for q in queries:
        if q[0] != "?": #끝쪽에 와일드카드 (물음표)가 붙은 경우
            res = count_by_range(array[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))
        answer.append(res)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))