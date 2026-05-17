n, k = map(int, input().split())
a_list = list(map(int, input().split()))

left = 1
right = 10**18 + 2 * 10**5 * 10**18


def can(target: int):
    count = 0
    for i in range(len(a_list)):
        a = a_list[i]
        if target > a:
            count += (target - a + i) // (i + 1)
            if count > k:
                return False
    return True


while right - left > 1:
    mid = (left + right) // 2
    if can(mid):
        left = mid
    else:
        right = mid

print(left)
