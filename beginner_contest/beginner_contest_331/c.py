N = int(input())
A_list = [int(x) for x in input().split()]

sorted_A_list = sorted(A_list)
answer_list = list()
answer_dict = dict()

for i in range(N):
    if A_list[i] in answer_dict:
        answer = answer_dict[A_list[i]]
        answer_list.append(str(answer))
        continue
    index = -(sorted_A_list[::-1].index(A_list[i]) + 1)
    answer = sum(sorted_A_list[index + 1:]) if index < -1 else 0
    answer_dict[A_list[i]] = answer
    answer_list.append(str(answer))

print(" ".join(answer_list))
