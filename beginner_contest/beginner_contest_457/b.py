n = int(input())
a_list = list()
for _ in range(n):
    arr = list(map(int, input().split()))
    a_list.append(arr[1:])
arr = list(map(int, input().split()))
x, y = arr[0], arr[1]
print(a_list[x - 1][y - 1])
