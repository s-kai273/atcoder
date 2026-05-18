s = input()
answer = 0
len_s = len(s)
for i in range(len_s):
    if s[i] == "C":
        answer += min(i + 1, len_s - i)
print(answer)
