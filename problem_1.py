dist = []

for num in range(1, 1000):
    if (num % 3 == 0) or (num % 5 == 0):
        dist.append(num)

print(sum(dist))
