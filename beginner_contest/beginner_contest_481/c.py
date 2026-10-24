q = int(input())
account_dict = dict()
count = 0
for _ in range(q):
    query = input()
    if query not in account_dict:
        count += 1
        account_dict[query] = count
    print(account_dict[query])
