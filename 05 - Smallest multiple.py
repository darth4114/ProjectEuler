test = False
nums = [i for i in range(3,21)]
test_num = 10

while not test:
    for num in nums:
        if test_num%num != 0:
            test_num += 10
            break
        elif test_num%num == 0
            test = True

print(test_num)

# i = 1
# for k in (range(1, 21)):
#   if i % k > 0:
#     for j in range(1, 21):
#       if (i*j) % k == 0:
#         i *= j
#         break
#
# print(i)
