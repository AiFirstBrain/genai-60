# Day 3: 5 HackerRank problems, all accepted

# 1. sWAP cASE
def swap_case(s):
    result = ""
    for ch in s:
        if ch.isupper():
            result += ch.lower()
        else:
            result += ch.upper()
    return result

# 2. String Split and Join
def split_and_join(line):
    a = line.split()
    return "-".join(a)

# 3. Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# 4. Find the Runner-Up Score
# n = int(input())
# arr = map(int, input().split())
# scores = sorted(set(arr))
# print(scores[-2])

# 5. Finding the percentage
# query_scores = student_marks[query_name]
# avg = sum(query_scores) / len(query_scores)
# print(f"{avg:.2f}")