# count = 1
# ARC
# CRA
#
# count = 2
# CRARARC

# count = 4
# ARARCRC
# ARCRARC
# CRARARC
# CRARCRA
# CRCRARA
#
# count = 9
# ARARARCRCRC
# ARARCRARCRC
# ARCRARARCRC
# ARCRARCRARC
# CRARARCRARC
# CRARARCRCRA
# CRARCRARCRA
# CRCRARARCRA
# CRCRARCRARA
# CRCRCRARARA
#
# count = 2
# ARARC
# ARCRA
# CRARA
#
# count = 3
# ARARARC
# ARARCRA
# ARCRARA
# CRARARA
#
# count = 6
# ARARARCRC
# ARARCRARC
# ARCRARARC
# CRARARARC
# CRARARCRA
# CRARCRARA
# CRCRARARA
#
# count = 9
# ARARARCRCRC
#
# count = 7
# 2 x 2 = 4
# ARARCRC
# 3 x 3 = 9
# ARARARCRCRC
#
# count = 547
# 23 x 23 = 529 => 46 + 45 = 91
# 24 x 24 = 576 => 48 + 47 = 95
# 25 x 25 = 625 => 50 + 49 = 99

x = int(input())
target_sqrt = 1
for i in range(1, 26):
    if i**2 >= x:
        target_sqrt = i
        break
diff = target_sqrt**2 - x
q = diff // target_sqrt
r = diff % target_sqrt
s_parts = list()
if target_sqrt == 1:
    if x == 0:
        s_parts = ["CRC"]
    else:
        s_parts = ["ARC"]
else:
    if r == 0:
        s_parts = (
            ["CR"] * q + ["AR"] * target_sqrt + ["CR"] * (target_sqrt - q - 1) + ["C"]
        )
    else:
        s_parts = (
            ["CR"] * q
            + ["AR"] * (target_sqrt - r)
            + ["CR"]
            + ["AR"] * r
            + ["CR"] * (target_sqrt - q - 2)
            + ["C"]
        )
answer = "".join(s_parts)
print(answer)

