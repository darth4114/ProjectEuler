sum = 0

for num in range(1, 10001):
    if num % 3 == 0 or num % 5 == 0:
        sum += num

print(sum)
