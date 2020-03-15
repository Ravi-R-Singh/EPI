def is_palindrome_number (num: int) -> bool:
    reversedNum = 0
    originalNum = num
    if num <= 0:
        return num == 0
    else:
        while originalNum > 0:
            reversedNum *= 10
            reversedNum += originalNum%10
            originalNum  //= 10
    return reversedNum == num

print (is_palindrome_number(0))
print (is_palindrome_number(1))
print (is_palindrome_number(7))
print (is_palindrome_number(11))
print (is_palindrome_number(121))
print (is_palindrome_number(333))
print (is_palindrome_number(-1))
print (is_palindrome_number(214567))
print (is_palindrome_number(891209120))
print (is_palindrome_number(78126217))
