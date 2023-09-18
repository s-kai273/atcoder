N = int(input())
S = input()
Q = int(input())

t_prev = 0
lower_or_upper_index_list = []
t1_i_list = list()
t1_x_list = list()
t1_c_list = list()
t2_i_list = list()
t3_i_list = list()

for i in range(Q):
    vals = input().split()
    t = int(vals[0])
    x = int(vals[1])
    c = vals[2]

    if t == 1:
        t1_i_list.append(i)
        t1_x_list.append(x)
        t1_c_list.append(c)
    elif t == 2:
        t2_i_list.append(i)
    else:
        t3_i_list.append(i)

S_c_list = list(S)

operation_done_index_list = []
t1_i_list = list(reversed(t1_i_list))
t1_x_list = list(reversed(t1_x_list))
t1_c_list = list(reversed(t1_c_list))
t2_and_t3_i_list = sorted(t2_i_list + t3_i_list, reverse=True)

i = 0
j = 0
while i < len(t2_and_t3_i_list) and j < len(t1_i_list):
    lu_i = t2_and_t3_i_list[i]
    c_i = t1_i_list[j]
    if c_i > lu_i:
        if t1_x_list[j] in operation_done_index_list:
            continue
        if i == 0:
            S_c_list[t1_x_list[j] - 1] = t1_c_list[j]
        else:
            S_c_list[t1_x_list[j] - 1] = t1_c_list[j].lower() \
                if t2_and_t3_i_list[0] in t2_i_list  \
                else t1_c_list[j].upper()
        operation_done_index_list.append(t1_x_list[j])
        j += 1
    else:
        i += 1

for i in range(N):
    if i + 1 in t1_x_list:
        continue
    S_c_list[i] = S_c_list[i].lower() \
        if t2_and_t3_i_list[0] in t2_i_list \
        else S_c_list[i].upper()

print(''.join(S_c_list))
