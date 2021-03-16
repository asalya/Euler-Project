number = 0

while True:
    number += 92378
    dist = 0
    for num in range(2, 21):
        if number % num == 0:
            dist += 1
    if dist == 19:
        break

print(number)
