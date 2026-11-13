l1, r1, l2, r2 = map(int, input().split())

sl, sr = l1, r1
ll, lr = l2, r2

if l1 > l2:
    sl, sr = l2, r2
    ll, lr = l1, r1


answer = -1

if sr < ll:
    answer = 0
elif sr >= ll and sr <= lr:
    answer = sr - ll
else:
    answer = lr - ll

print(answer)
