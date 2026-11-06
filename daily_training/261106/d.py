n, a = map(int, input().split())
t_list = list(map(int, input().split()))

end_time = 0

for t in t_list:
    end_time = max(end_time, t) + a
    print(end_time)
