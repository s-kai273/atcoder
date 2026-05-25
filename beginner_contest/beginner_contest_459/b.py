n = int(input())
s_list = input().split()
c_list = list()
for s in s_list:
    if s[0] in {"a", "b", "c"}:
        c_list.append(2)
    elif s[0] in {"d", "e", "f"}:
        c_list.append(3)
    elif s[0] in {"g", "h", "i"}:
        c_list.append(4)
    elif s[0] in {"j", "k", "l"}:
        c_list.append(5)
    elif s[0] in {"m", "n", "o"}:
        c_list.append(6)
    elif s[0] in {"p", "q", "r", "s"}:
        c_list.append(7)
    elif s[0] in {"t", "u", "v"}:
        c_list.append(8)
    elif s[0] in {"w", "x", "y", "z"}:
        c_list.append(9)
print("".join([str(c) for c in c_list]))
