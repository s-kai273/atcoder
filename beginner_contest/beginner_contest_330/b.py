N, L, R = [int(x) for x in input().split()]
A_list = [int(x) for x in input().split()]

answer = list()
answer_dict = dict()

for A in A_list:
    if A in list(range(L, R + 1)):
        answer.append(str(A))
    elif abs(A - L) > abs(A - R):
        answer.append(str(R))
    else:
        answer.append(str(L))
print(" ".join(answer))
