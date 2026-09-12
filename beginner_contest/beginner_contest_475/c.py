# C1 5 C2 2 C3 4 C4 1 C5 6 C6
# C1 2 C2 3 C3 4 C4 4 C5 3 C6 5 C7 1 C8

n, s, l = map(int, input().split())
a_list = list(map(int, input().split()))

left, right = 1, s
left_dist = sum(a_list[left - 1 : s - 1])
right_dist = sum(a_list[s - 1 : right - 1])

answer = 0
while left <= s and right <= n:
    city_count = right - left + 1
    dist = min(2 * left_dist + right_dist, left_dist + 2 * right_dist)
    if dist <= l and city_count > answer:
        answer = city_count
    if dist > l:
        left_dist -= a_list[left - 1]
        left += 1
    else:
        right_dist += a_list[right - 1] if right < n else 0
        right += 1

print(answer)
