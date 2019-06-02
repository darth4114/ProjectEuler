num = 1
for x in range(1,21):
    if num % x > 0:
        for y in range(1,21):
            if (num * y) % x == 0:
                num *= y
                break

print(num)

# i = 1
# for k in (range(1, 21)):
#   if i % k > 0:
#     for j in range(1, 21):
#       if (i*j) % k == 0:
#         i *= j
#         break
#
# print(i)
