def isPalindrome(num):
    pat = str(num)
    return pat == pat[::-1]

palindrome = 0

for x in range(100,1000,1):
    for y in range(x,1000,1):
        if isPalindrome(x*y) and x*y > palindrome:
            palindrome = x*y

print(palindrome)
