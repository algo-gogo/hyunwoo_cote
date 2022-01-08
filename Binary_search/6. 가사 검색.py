## 효율성 Fail 시간초과
def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        for word in words:
            if len(word) != len(query):
                continue
            query_flag = 0
            for i in range(len(query)):
                if query[i] == "?":
                    continue
                if word[i] != query[i]:
                    query_flag = 1
                    break
            if query_flag == 0:
                count += 1
        answer.append(count)
    return answer

## 효율성 Fail 시간초과
import re
def solution(words, queries):
    answer = []

    for query in queries:
        this_query = ""
        for i in query:
            if i == "?":
                this_query += "\w"
            else:
                this_query += i
        
        count = 0
        for word in words:
            if len(query) != len(word):
                continue
            x = re.findall(this_query, word)
            if x:
                count += 1
        answer.append(count)
            
    return answer