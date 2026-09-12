n = int(input())
a_list = map(int, input().split())
one_count = 0
ten_count = 0
hundred_count = 0

for a in a_list:
    bill = (a // 1000 + 1) * 1000 if a % 1000 != 0 else a
    change = bill - a
    hundred = change // 100
    ten = (change - hundred * 100) // 10
    one = change - hundred * 100 - ten * 10
    hundred_count += hundred
    ten_count += ten
    one_count += one

print(f"{one_count} {ten_count} {hundred_count}")
