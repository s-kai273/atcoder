s11, s12 = input()
s21, s22 = input()

expected = ["A", "D"]
if (
    sorted([s11, s12]) == expected
    or sorted([s11, s21]) == expected
    or sorted([s12, s22]) == expected
    or sorted([s21, s22]) == expected
):
    print("Yes")
else:
    print("No")
