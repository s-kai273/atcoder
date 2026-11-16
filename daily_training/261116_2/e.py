n, m = map(int, input().split())
a_list = list(map(int, input().split()))

fi = 0
answer = list()

for i in range(1, n + 1):
    while i > a_list[fi]:
        fi += 1
    print(a_list[fi] - i)
