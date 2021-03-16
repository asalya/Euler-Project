num = 0
result_plus = 0
result_mult = 0

while num < 100:
    num += 1
    result_plus += num ** 2
    result_mult += num

print(result_mult**2 - result_plus)
