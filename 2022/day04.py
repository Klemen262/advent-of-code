from input04 import data

sum1 = 0
sum2 = 0
for line in data.split("\n"):
    a, b, c, d = [int(x) for x in line.replace(",", "-").split("-")]
    if a <= c and b >= d or a >= c and b <= d:
        sum1 += 1
    if not b < c and not a > d:
        sum2 += 1
print(sum1)
print(sum2)
