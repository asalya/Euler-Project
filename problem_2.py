# dist = [1, 2]
# wist = []

# for i in range(3, 33):
#     r = dist[-2] + dist[-1]
#     dist.append(r)

# for k in dist:
#     if k % 2 == 0:
#         wist.append(k)
    
# print(sum(wist))

ans = 0
a = 1
b = 1
while a <= 4000000:
	if a % 2 == 0:
		ans += a
	a, b = b, a + b
print(ans)
