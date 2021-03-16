number = 0

while True:
    number += 140
    dist = []
    for num in range(2, 21):
        if number % num == 0:
            dist.append(num)
    if len(dist) == 9:
        break

print(number)
