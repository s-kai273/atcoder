answer = 0

for i in range(12):
    i += 1
    S = input()
    if len(S) == i:
        answer += 1

print(answer)