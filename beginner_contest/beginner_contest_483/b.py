n, q = map(int, input().split())
k_list = list(map(int, input().split()))

card_list = [i + 1 for i in range(n)]

for k in k_list:
    card_list = [-1 * card_list[i] for i in range(k - 1, -1, -1)] + card_list[k:]

for c in card_list:
    print(c)
