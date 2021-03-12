dist = []
for i in range(100, 1000):
    for k in range(100, 1000):
        result = i * k
        if str(result) == str(result)[::-1]:
            dist.append(result)

print(max(dist))