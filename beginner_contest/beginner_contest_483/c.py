n, m = map(int, input().split())
vote_pair_dict = dict()
vote_count = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    vote_pair_dict.setdefault(a, dict())
    vote_pair_dict[a][b] = vote_pair_dict[a].get(b, 0) + 1
    vote_count[a] += 1

vote_keys = list()
for i in range(1, n + 1):
    vote_keys.append((vote_count[i], i))

vote_keys.sort(key=lambda x: (-x[0], x[1]))

for k in range(1, n + 1):
    max_i = vote_keys[0][1] if k != vote_keys[0][1] else vote_keys[1][1]
    max_vote = vote_keys[0][0] if k != vote_keys[0][1] else vote_keys[1][0]
    if k in vote_pair_dict.keys():
        for b in vote_pair_dict[k].keys():
            cur_count = vote_count[b] + vote_pair_dict[k][b]
            if (max_vote, -max_i) < (cur_count, -b):
                max_i = b
                max_vote = cur_count
    print(max_i)
