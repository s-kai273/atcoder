n, m = map(int, input().split())
s_list = list()
s_dict = dict()
t_list = list()
for _ in range(n):
    s = input()
    s_list.append(s)
    s_dict[s] = 0

for _ in range(m):
    t = input()
    if t in s_dict:
        s_dict[t] += 1
    else:
        candidate = None
        for s in s_dict.keys():
            if len(t) != len(s):
                continue
            diff_count = 0
            for i in range(len(t)):
                if s[i] != t[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count == 1 and candidate is None:
                candidate = s
            elif diff_count == 1 and candidate:
                candidate = None
                break
        if candidate:
            s_dict[candidate] += 1
for i in range(n):
    print(s_dict[s_list[i]])
