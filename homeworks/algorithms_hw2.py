#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.

def split_string(s):
    n = len(s)
    m = n // 2
    if n % 2 == 0:
        first_part = s[:m]
        second_part = s[m:]
    else:
        first_part = s[:m+1]
        second_part = s[m+1:]
    return second_part + first_part

str_example = 'aaazbbb'
print(split_string(str_example))

#HW 2
def has_unique_chars(s):
    char_set = set()
    for i in s:
        if i in char_set:
            return False
        char_set.add(i)
    return True

s1 = "abcdefg"
s2 = "hello"
print(has_unique_chars(s1))  # Output: True
print(has_unique_chars(s2))  # Output: False
