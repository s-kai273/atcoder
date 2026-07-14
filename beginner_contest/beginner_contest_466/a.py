n = int(input())
x_list = list(map(int, input().split()))
answer = "Yes"
for x in x_list:
    if x >= 0:
        answer = "No"
        break
print(answer)
