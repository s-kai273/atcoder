n = int(input())
a_list = list(map(int, input().split()))
a_list = filter(lambda a: a % 2 == 0, a_list)
print(*a_list)
