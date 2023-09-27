N = int(input())
A_list = [int(x) for x in input().split()]

count = 0
while True:
    isOver = False
    for i in range(len(A_list)):
        if A_list[i] % 2 != 0:
            isOver = True
            break
        A_list[i] /= 2
    if isOver:
        break
    count += 1

print(count)
