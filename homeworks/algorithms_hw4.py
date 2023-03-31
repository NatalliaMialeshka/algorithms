#Your input is a list of integers, and you have to reorder its entries so that
# the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
def even_first(arr):
    even_arr = []
    odd_arr = []
    for i in arr:
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
    return even_arr + odd_arr

my_arr = [1, 2, 5, 8, 4, 6]
print(even_first(my_arr))

#Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.

def plus_one(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits