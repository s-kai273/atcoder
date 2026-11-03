n = int(input())
a_list = [0] + list(map(int, input().split()))

answer = [""] * (n + 1)
i_list = list()
current = 1

while True:
    i_list.append(current)

    if current == a_list[current]:
        for i in i_list:
            answer[i] = str(current)
        prev = current
        for i in range(i_list[0], n + 1):
            if answer[i] == "":
                current = i
                break
        i_list = list()
        if current == prev:
            break
    else:
        current = a_list[current]

print(" ".join(answer[1:]))
