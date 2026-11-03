a_list = sorted(map(int, input().split()))
answer = "Yes" if a_list[0] * a_list[1] == a_list[2] else "No"
print(answer)
