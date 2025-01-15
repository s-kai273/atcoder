X = int(input())
answer = 0
for i in range(1, 10):
    for j in range(1, 10):
        if X != i * j:
            answer += i * j
print(answer)