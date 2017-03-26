def is_palindrome(num):
    strNum = str(num)
    for i in range(0, len(strNum)/2):
        if strNum[i] != strNum[-(i + 1)]:
            return False
    return True

largest = 0

for i in range (999, 100, -1):
    for j in range (999, 100, -1):
        if is_palindrome(i*j):
            if (i*j) > largest:
                largest = i*j

print largest