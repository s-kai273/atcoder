from itertools import combinations

n = int(input())
e_list = [list() for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    e_list[u - 1].append(v - 1)
    e_list[v - 1].append(u - 1)


c_list = list(map(int, input().split()))

target_v_list = set()
for i in range(n):
    if len(e_list[i]) == 1:
        target_v_list.add(i)

distv_dict = dict()
visited = set()
max_dist = -1


def dfs(sv: int, tv: int) -> int:
    visited.add(sv)
    for v in e_list[sv]:
        if v in visited:
            continue
        if v == tv:
            return 1
        result = dfs(v, tv)
        if result > 0:
            return result + 1
    return -1


for u, v in combinations(target_v_list, 2):
    visited = set()
    dist = dfs(u, v)
    distv_dict.setdefault(dist, list()).append((u, v))
    max_dist = max(max_dist, dist)

answer = 0
for u, v in distv_dict[max_dist]:
    if c_list[u] == c_list[v]:
        answer += 1

print(answer)
