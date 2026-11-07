n, m = map(int, input().split())
vote_change_dict = [{} for _ in range(n + 1)]
vote_count = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    vote_change_dict[a][b] = vote_change_dict[a].get(b, 0) + 1
    vote_count[a] += 1

ranking = sorted(range(1, n + 1), key=lambda i: (-vote_count[i], i))

for k in range(1, n + 1):
    winner = ranking[0] if k != ranking[0] else ranking[1]
    max_vote = vote_count[winner]
    for b in vote_change_dict[k].keys():
        cur_count = vote_count[b] + vote_change_dict[k][b]
        if (max_vote, -winner) < (cur_count, -b):
            winner = b
            max_vote = cur_count
    print(winner)
