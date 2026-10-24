n, m, s, t = map(int, input().split())

adj_list = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)

for adj in adj_list:
    adj.sort()

visited = set()
min_fuel_dict = dict()


def dfs(planet) -> int:
    if planet in visited:
        return -1
    visited.add(planet)
    if planet in min_fuel_dict:
        return min_fuel_dict[planet]
    if planet == t:
        return 0
    min_result = -1
    for i, next in enumerate(adj_list[planet]):
        result = dfs(next)
        if result > -1:
            result = result if i == 0 else result + 1
            if min_result == -1:
                min_result = result
            else:
                min_result = min(min_result, result)
            visited.discard(next)
    min_fuel_dict[planet] = min_result
    if min_result == -1:
        visited.discard(planet)
    return min_result


fuel = dfs(s)
print(fuel)
