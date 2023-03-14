#Compute the sum of digits in all numbers from 1 to n
def sum_of_digits(n: int):
    result = 0
    for i in range(0, n + 1):
        result += i
    print(result)

sum_of_digits(101)

#Find the max number
def find_max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num3:
        print(num2)
    else:
        print(num3)

find_max_num(12, 5, 25)

#Count odd and even numbers
def count_odd_and_even_digits(num):
    count_odd = 0
    count_even = 0
    origin_num = num
    while num != 0:
        temp = num % 10
        num = num // 10
        if temp % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f'{origin_num} number where {count_odd} odd and {count_even} even digits')

count_odd_and_even_digits(34560)