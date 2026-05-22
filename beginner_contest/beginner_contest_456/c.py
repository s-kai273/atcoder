s = input()
answer = 1
left = 0
for right in range(1, len(s)):
    if s[right] == s[right - 1]:
        left = right
        answer += 1
    else:
        answer += right - left + 1
print(answer % 998244353)
