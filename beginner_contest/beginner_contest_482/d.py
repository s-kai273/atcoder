n = int(input())
x_list = list(map(int, input().split()))
answer = list()

for k in range(n):
    if k == 0 or k == n - 1:
        answer.append(abs(x_list[0] - x_list[-1]) // 2)
        continue
    tls = (x_list[k] - x_list[k - 1]) // 2
    tle = (x_list[k - 1] - x_list[0]) // 2
    trs = (x_list[k + 1] - x_list[k]) // 2
    tre = (x_list[-1] - x_list[k + 1]) // 2
    answer.append(min(max(tls + tle, tls + trs + tre), max(trs + tre, trs + tls + tle)))

for t in answer:
    print(t)
