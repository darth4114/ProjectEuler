def isprime(n):

    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

num = 3
counter = 2

while counter < 10001:
    num += 2
    if isprime(num):
        counter += 1

print(num)

print(isprime(num))
