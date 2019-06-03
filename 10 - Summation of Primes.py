def isprime(n):

    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

num = 1
total = 2

while num < (2000000-1):
    num += 2
    if isprime(num):
        total += num

print(total)
